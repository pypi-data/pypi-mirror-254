pub(crate) struct Covariates {
    pub(crate) age: f64,
    pub(crate) age_squared: f64,
    pub(crate) total_cholesterol: f64,
    pub(crate) age_total_cholesterol: f64,
    pub(crate) hdl_cholesterol: f64,
    pub(crate) age_hdl_cholesterol: f64,
    pub(crate) treated_systolic_blood_pressure: f64,
    pub(crate) age_treated_systolic_blood_pressure: f64,
    pub(crate) untreated_systolic_blood_pressure: f64,
    pub(crate) age_untreated_systolic_blood_pressure: f64,
    pub(crate) current_smoker: f64,
    pub(crate) age_current_smoker: f64,
    pub(crate) diabetes: f64,
    pub(crate) base_survival: f64,
    pub(crate) mean_coefficient_value: f64,
}

impl Covariates {
    pub(crate) fn white_female() -> Covariates {
        Covariates {
            age: -29.799,
            age_squared: 4.884,
            total_cholesterol: 13.540,
            age_total_cholesterol: -3.114,
            hdl_cholesterol: -13.578,
            age_hdl_cholesterol: 3.149,
            treated_systolic_blood_pressure: 2.019,
            age_treated_systolic_blood_pressure: 0.0,
            untreated_systolic_blood_pressure: 1.957,
            age_untreated_systolic_blood_pressure: 0.0,
            current_smoker: 7.574,
            age_current_smoker: -1.665,
            diabetes: 0.661,
            base_survival: 0.96652,
            mean_coefficient_value: -29.18,
        }
    }

    pub(crate) fn african_american_female() -> Covariates {
        Covariates {
            age: 17.1141,
            age_squared: 0.0,
            total_cholesterol: 0.9396,
            age_total_cholesterol: 0.0,
            hdl_cholesterol: -18.9196,
            age_hdl_cholesterol: 4.4748,
            treated_systolic_blood_pressure: 29.2907,
            age_treated_systolic_blood_pressure: 6.4321,
            untreated_systolic_blood_pressure: 27.8197,
            age_untreated_systolic_blood_pressure: -6.0873,
            current_smoker: 0.6908,
            age_current_smoker: 0.0,
            diabetes: 0.8738,
            base_survival: 0.95334,
            mean_coefficient_value: 86.61,
        }
    }

    pub(crate) fn white_male() -> Covariates {
        Covariates {
            age: 12.344,
            age_squared: 0.0,
            total_cholesterol: 11.853,
            age_total_cholesterol: -2.664,
            hdl_cholesterol: -7.990,
            age_hdl_cholesterol: 1.769,
            treated_systolic_blood_pressure: 1.797,
            age_treated_systolic_blood_pressure: 0.0,
            untreated_systolic_blood_pressure: 1.764,
            age_untreated_systolic_blood_pressure: 0.0,
            current_smoker: 7.837,
            age_current_smoker: -1.795,
            diabetes: 0.658,
            base_survival: 0.91436,
            mean_coefficient_value: 61.18,
        }
    }

    pub(crate) fn african_american_male() -> Covariates {
        Covariates {
            age: 2.469,
            age_squared: 0.0,
            total_cholesterol: 0.302,
            age_total_cholesterol: 0.0,
            hdl_cholesterol: -0.307,
            age_hdl_cholesterol: 0.0,
            treated_systolic_blood_pressure: 1.916,
            age_treated_systolic_blood_pressure: 0.0,
            untreated_systolic_blood_pressure: 1.809,
            age_untreated_systolic_blood_pressure: 0.0,
            current_smoker: 0.549,
            age_current_smoker: 0.0,
            diabetes: 0.645,
            base_survival: 0.89536,
            mean_coefficient_value: 19.54,
        }
    }
}
