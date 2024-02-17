import numpy as np
import pandas as pd


def _prepare_df_for_batch(
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
    # Default column names
    column_mapping = {
        "age": age,
        "sex": sex,
        "race": race,
        "systolic_bp": systolic_bp,
        "total_cholesterol": total_cholesterol,
        "hdl_cholesterol": hdl_cholesterol,
        "diabetes": diabetes,
        "smoker": smoker,
        "on_hypertension_treatment": on_hypertension_treatment,
    }

    # Update column names with mappings from kwargs if provided
    column_mapping.update(kwargs)

    # Ensure all required column names exist in the DataFrame
    for key, col in column_mapping.items():
        if col not in df.columns:
            raise ValueError(
                f"Column '{col}' for parameter '{key}' not found in DataFrame."
            )

    reordered_df = df[[column_mapping[key] for key in column_mapping]].copy()

    sex_col = column_mapping["sex"]
    reordered_df[sex_col] = (
        reordered_df[sex_col].str.lower().map({"female": 0, "male": 1})
    )

    sex_col = column_mapping["race"]
    reordered_df[sex_col] = (
        reordered_df[sex_col]
        .str.lower()
        .map({"aa": 1, "african american": 1, "white": 0})
    )

    # Convert boolean columns to integers based on the column names from column_mapping
    bool_cols = [
        column_mapping["diabetes"],
        column_mapping["smoker"],
        column_mapping["on_hypertension_treatment"],
    ]
    reordered_df[bool_cols] = reordered_df[bool_cols].astype(int)
    return reordered_df.values.astype(np.float64)


def _report_any_null_values(result: np.ndarray) -> None:
    null_rows = np.isnan(result).sum()
    if null_rows > 0:
        print(
            f"WARNING: {null_rows} patients were unable to have the score calculated"
            f"as their input parameters were out of the range."
        )
