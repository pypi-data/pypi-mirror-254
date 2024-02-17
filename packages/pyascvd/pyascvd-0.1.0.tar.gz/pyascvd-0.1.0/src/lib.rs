mod ascvd;
mod covariates;

use crate::ascvd::{calculate_10_yr_ascvd, calculate_10_yr_ascvd_rust_parallel_np};
use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
fn _pyascvd(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_10_yr_ascvd, m)?)?;
    m.add_function(wrap_pyfunction!(calculate_10_yr_ascvd_rust_parallel_np, m)?)?;
    Ok(())
}
