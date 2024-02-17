import numpy as np

import pyascvd
import slash
import pandas as pd


def test_white_female() -> None:
    test_patient = {
        "age": 55,
        "sex": "female",
        "race": "white",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    r = pyascvd.ascvd(**test_patient)
    slash.assert_almost_equal(r, 2.1, delta=0.1)


def test_white_male() -> None:
    test_patient = {
        "age": 55,
        "sex": "male",
        "race": "white",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    r = pyascvd.ascvd(**test_patient)
    slash.assert_almost_equal(r, 5.4, delta=0.1)


def test_african_american_male() -> None:
    test_patient = {
        "age": 55,
        "sex": "male",
        "race": "aa",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    r = pyascvd.ascvd(**test_patient)
    slash.assert_almost_equal(r, 6.1, delta=0.1)


def test_african_american_female() -> None:
    test_patient = {
        "age": 55,
        "sex": "female",
        "race": "aa",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    r = pyascvd.ascvd(**test_patient)
    slash.assert_almost_equal(r, 3.0, delta=0.1)


def test_invalid_age() -> None:
    test_patient = {
        "age": 101,
        "sex": "female",
        "race": "aa",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    with slash.assert_raises(ValueError):
        pyascvd.ascvd(**test_patient)


def test_invalid_total_cholesterol():
    test_patient = {
        "age": 55,
        "sex": "female",
        "race": "aa",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 10,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    with slash.assert_raises(ValueError):
        pyascvd.ascvd(**test_patient)


def test_invalid_hdl_cholesterol():
    test_patient = {
        "age": 55,
        "sex": "female",
        "race": "aa",
        "systolic_blood_pressure": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 300,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    with slash.assert_raises(ValueError):
        pyascvd.ascvd(**test_patient)


def test_invalid_systolic_bp():
    test_patient = {
        "age": 55,
        "sex": "female",
        "race": "aa",
        "systolic_blood_pressure": 400,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    with slash.assert_raises(ValueError):
        pyascvd.ascvd(**test_patient)


def test_invalid_sex():
    test_patient = {
        "age": 55,
        "sex": "unknown",
        "race": "aa",
        "systolic_blood_pressure": 400,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }
    with slash.assert_raises(ValueError):
        pyascvd.ascvd(**test_patient)


def test_batch():
    test_patient = {
        "age": 55,
        "sex": "male",
        "race": "aa",
        "systolic_bp": 120,
        "total_cholesterol": 213,
        "hdl_cholesterol": 50,
        "diabetes": False,
        "smoker": False,
        "on_hypertension_treatment": False,
    }

    data_list = [test_patient for _ in range(10)]
    df = pd.DataFrame(data_list)
    r = pyascvd.batch_calculate_10_yr_ascvd_risk(df)
    expected = np.array([6.075816886803742] * 10)

    assert np.array_equal(r, expected)

