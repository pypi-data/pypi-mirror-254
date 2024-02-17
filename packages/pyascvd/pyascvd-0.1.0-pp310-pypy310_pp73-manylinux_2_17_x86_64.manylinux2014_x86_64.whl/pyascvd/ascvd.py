import numpy as np
import pandas as pd

from pyascvd import _pyascvd

from pyascvd.utils import _prepare_df_for_batch, _report_any_null_values


def ascvd(
    age: float,
    sex: str,
    race: str,
    systolic_blood_pressure: float,
    total_cholesterol: float,
    hdl_cholesterol: float,
    diabetes: bool,
    smoker: bool,
    on_hypertension_treatment: bool,
) -> float:
    return _pyascvd.calculate_10_yr_ascvd(
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


def batch_calculate_10_yr_ascvd_risk(
    df: pd.DataFrame,
    age: str = "age",
    sex: str = "sex",
    race: str = "race",
    systolic_bp: str = "systolic_bp",
    total_cholesterol: str = "total_cholesterol",
    hdl_cholesterol: str = "hdl_cholesterol",
    diabetes: str = "diabetes",
    smoker: str = "smoker",
    on_hypertension_treatment: str = "on_hypertension_treatment",
    **kwargs,
) -> np.ndarray:
    """
     Batch calculate the 10-year risk of atherosclerotic cardiovascular disease (ASCVD) for a dataset.

    This function processes a DataFrame with health and lifestyle parameters to estimate
    the 10-year ASCVD risk for each individual in the dataset. The input values must fall
    within specified ranges for the calculation to be valid.

    Parameters:
    - df (pd.DataFrame): DataFrame containing the required data.
    - age (str): Column name for the age of the individuals in years. Must be between 30 and 79. Default 'age'.
    - sex (str): Column name for the sex of the individuals ('male' or 'female'). Case insensitive. Default 'sex'.
    - race (str): Column name for the race of the individuals ('aa' or 'african american' / 'white'). Case insensitive. Default 'race'.
    - systolic_bp (str): Column name for the systolic blood pressure (mmHg). Must be between 90 and 200. Default 'systolic_bp'.
    - total_cholesterol (str): Column name for the total cholesterol level (mg/dL). Must be between 130 and 320. Default 'total_cholesterol'.
    - hdl_cholesterol (str): Column name for the HDL cholesterol level (mg/dL). Must be between 20 and 100. Default 'hdl_cholesterol'.
    - has_diabetes (str): Column name indicating if the individual has diabetes (True or False). Default 'has_diabetes'.
    - current_smoker (str): Column name indicating if the individual is a current smoker (True or False). Default 'current_smoker'.
    - on_htn_meds (str): Column name indicating if the individual is on hypertension medication (True or False). Default 'on_htn_meds'.
    - **kwargs: Optional keyword arguments for custom column mappings.

    Returns:
    numpy.ndarray: A numpy array of estimated 10-year ASCVD risk percentages for each individual in the DataFrame.

    Raises:
    ValueError: If any of the input parameters are outside their valid ranges or if the specified columns are not found in the DataFrame.

    Example:
    >>> df = pd.DataFrame({...})
    >>> risks = batch_calculate_10_yr_ascvd_risk(df, sex='gender', age='patient_age', ...)
    >>> print(risks)
    # Returns: A np.array of estimated 10-year ASCVD risk percentages

    Alternatively, can pass in a dictionary of column mappings
    >>> df = pd.DataFrame({...})
    >>> column_mappings = {
    ...     'age': 'age_column',
    ...     'sex': 'gender_column',
    ...     'race': 'race_column',
    ...     'systolic_bp': 'bp_systolic',
    ...     'total_cholesterol': 'cholesterol_total',
    ...     'hdl_cholesterol': 'cholesterol_hdl',
    ...     'diabetes': 'diabetes_status',
    ...     'smoker': 'smoker_status',
    ...     'on_hypertension_treatment': 'hypertension_meds',
    ... }
    >>> risks = batch_calculate_10_yr_ascvd_risk(df, **column_mappings)
    # Returns: A np.array of estimated 10-year ASCVD risk percentages
    """

    data = _prepare_df_for_batch(
        df=df,
        age=age,
        sex=sex,
        race=race,
        total_cholesterol=total_cholesterol,
        hdl_cholesterol=hdl_cholesterol,
        systolic_bp=systolic_bp,
        diabetes=diabetes,
        smoker=smoker,
        on_hypertension_treatment=on_hypertension_treatment,
        **kwargs,
    )

    # Calculate ASCVD risk for each row
    result = _pyascvd.calculate_10_yr_ascvd_rust_parallel_np(data=data)
    _report_any_null_values(result)
    return result

if __name__ == '__main__':

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
    r = batch_calculate_10_yr_ascvd_risk(df)
    expected = np.array([6.075816886803742] * 10)

    print(np.array_equal(r, expected))