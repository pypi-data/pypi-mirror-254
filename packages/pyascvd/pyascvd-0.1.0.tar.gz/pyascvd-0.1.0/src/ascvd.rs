use crate::covariates::Covariates;
use numpy::{PyArray, PyReadonlyArrayDyn};
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use rayon::prelude::*;
use std::f64;

#[derive(Debug)]
enum Sex {
    Male,
    Female,
}

#[derive(Debug)]
enum Race {
    White,
    AfricanAmerican,
}

fn parse_sex(input: &str) -> Option<Sex> {
    match input.to_lowercase().as_str() {
        "male" => Some(Sex::Male),
        "female" => Some(Sex::Female),
        _ => None,
    }
}

fn parse_race(input: &str) -> Option<Race> {
    match input.to_lowercase().as_str() {
        "white" => Some(Race::White),
        "african american" | "aa" => Some(Race::AfricanAmerican),
        _ => None,
    }
}

fn get_gender_and_race_covariates(sex: &str, race: &str) -> PyResult<Covariates> {
    match (parse_sex(sex), parse_race(race)) {
        (Some(Sex::Male), Some(Race::White)) => Ok(Covariates::white_male()),
        (Some(Sex::Female), Some(Race::White)) => Ok(Covariates::white_female()),
        (Some(Sex::Male), Some(Race::AfricanAmerican)) => Ok(Covariates::african_american_male()),
        (Some(Sex::Female), Some(Race::AfricanAmerican)) => {
            Ok(Covariates::african_american_female())
        }
        _ => Err(PyErr::new::<PyValueError, _>("Invalid input")),
    }
}

pub fn validate_input(
    age: f64,
    total_cholesterol: f64,
    hdl_cholesterol: f64,
    systolic_bp: f64,
) -> Result<(), String> {
    if !(40.0..=79.0).contains(&age) {
        return Err("Age must be between 40 and 79".to_string());
    }

    if !(130.0..=320.0).contains(&total_cholesterol) {
        return Err("Total cholesterol must be between 130 and 320".to_string());
    }
    if !(20.0..=100.0).contains(&hdl_cholesterol) {
        return Err("HDL cholesterol must be between 20 and 100".to_string());
    }
    if !(90.0..=200.0).contains(&systolic_bp) {
        return Err("Systolic blood pressure must be between 90 and 200".to_string());
    }
    Ok(())
}

pub fn calculate_ascvd(
    age: f64,
    sex: &str,
    race: &str,
    systolic_blood_pressure: f64,
    total_cholesterol: f64,
    hdl_cholesterol: f64,
    diabetes: bool,
    smoker: bool,
    on_hypertension_treatment: bool,
) -> Result<f64, String> {
    validate_input(
        age,
        total_cholesterol,
        hdl_cholesterol,
        systolic_blood_pressure,
    )?;

    let ln_age = age.ln();
    let ln_total_cholesterol = total_cholesterol.ln();
    let ln_hdl_cholesterol = hdl_cholesterol.ln();
    let ln_systolic_blood_pressure = systolic_blood_pressure.ln();

    let ln_age_squared = ln_age.powi(2);
    let ln_age_total_cholesterol = ln_age * ln_total_cholesterol;
    let ln_age_hdl_cholesterol = ln_age * ln_hdl_cholesterol;
    let ln_age_systolic_blood_pressure = ln_age * ln_systolic_blood_pressure;

    let covariates = get_gender_and_race_covariates(sex, race).unwrap();

    let individual_sum: f64 = vec![
        ln_age * covariates.age,
        ln_age_squared * covariates.age_squared,
        ln_total_cholesterol * covariates.total_cholesterol,
        ln_age_total_cholesterol * covariates.age_total_cholesterol,
        ln_hdl_cholesterol * covariates.hdl_cholesterol,
        ln_age_hdl_cholesterol * covariates.age_hdl_cholesterol,
        ln_systolic_blood_pressure
            * (if on_hypertension_treatment {
                covariates.treated_systolic_blood_pressure
            } else {
                covariates.untreated_systolic_blood_pressure
            }),
        ln_age_systolic_blood_pressure
            * (if on_hypertension_treatment {
                covariates.age_treated_systolic_blood_pressure
            } else {
                covariates.age_untreated_systolic_blood_pressure
            }),
        if smoker {
            covariates.current_smoker
        } else {
            0.0
        },
        if smoker {
            ln_age * covariates.age_current_smoker
        } else {
            0.0
        },
        if diabetes { covariates.diabetes } else { 0.0 },
    ]
    .iter()
    .sum();

    let exponent = (individual_sum - covariates.mean_coefficient_value).exp();
    let result = (1.0 - covariates.base_survival.powf(exponent)) * 100.0;
    // println!("{}", rounded_individual_sum);
    Ok(result)
}

#[pyfunction]
pub fn calculate_10_yr_ascvd(
    age: f64,
    sex: String,
    race: String,
    systolic_blood_pressure: f64,
    total_cholesterol: f64,
    hdl_cholesterol: f64,
    diabetes: bool,
    smoker: bool,
    on_hypertension_treatment: bool,
) -> PyResult<f64> {
    match calculate_ascvd(
        age,
        &sex,
        &race,
        systolic_blood_pressure,
        total_cholesterol,
        hdl_cholesterol,
        diabetes,
        smoker,
        on_hypertension_treatment,
    ) {
        Ok(result) => Ok(result),
        Err(e) => Err(PyErr::new::<PyValueError, _>(e)),
    }
}

type RiskCalcFn = fn(
    f64,  // age
    &str, // sex
    &str, // race
    f64,  // systolic_bp
    f64,  // total_cholesterol
    f64,  // hdl_cholesterol
    bool, // has_diabetes
    bool, // current_smoker
    bool, // on_htn_meds
) -> Result<f64, String>;

pub fn calculate_risk_rust_parallel_np(
    py: Python,
    data: PyReadonlyArrayDyn<f64>,
    risk_calc_fn: RiskCalcFn,
) -> PyResult<PyObject> {
    let shape = data.shape();
    if shape.len() != 2 || shape[1] != 9 {
        return Err(PyValueError::new_err("Array shape must be (n, 11)"));
    }

    let rows = data
        .as_array()
        .outer_iter()
        .map(|row| {
            (
                row[0],                                        // age
                if row[1] == 1.0 { "male" } else { "female" }, // Convert numeric to "male" or "female"
                if row[2] == 1.0 { "aa" } else { "white" },    // Convert numeric to "aa" or "white"
                row[3],                                        // systolic bp
                row[4],                                        // total_cholesterol
                row[5],                                        // hdl cholesterol
                row[6] != 0.0,                                 // Convert float to bool // diabetes
                row[7] != 0.0,                                 // Convert float to bool // smoker
                row[8] != 0.0, // Convert float to bool // htn_treatment
            )
        })
        .collect::<Vec<_>>();

    let results: Vec<_> = rows
        .into_par_iter()
        .map(
            |(
                age,
                sex,
                race,
                systolic_blood_pressure,
                total_cholesterol,
                hdl_cholesterol,
                diabetes,
                smoker,
                on_hypertension_treatment,
            )| {
                risk_calc_fn(
                    age,
                    sex,
                    race,
                    systolic_blood_pressure,
                    total_cholesterol,
                    hdl_cholesterol,
                    diabetes,
                    smoker,
                    on_hypertension_treatment,
                )
                .unwrap_or(f64::NAN) // Handle error by returning NaN
            },
        )
        .collect();

    Ok(PyArray::from_vec(py, results).to_object(py))
}

#[pyfunction]
pub fn calculate_10_yr_ascvd_rust_parallel_np(
    py: Python,
    data: PyReadonlyArrayDyn<f64>,
) -> PyResult<PyObject> {
    calculate_risk_rust_parallel_np(py, data, calculate_ascvd)
}
