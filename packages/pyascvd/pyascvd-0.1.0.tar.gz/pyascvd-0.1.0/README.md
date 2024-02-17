# PyASCVD :anatomical_heart:

###### 2013 ASCVD (Atherosclerotic and Cardiovascular Disease) risk estimator plus calcualtor

![Python- 3.7 --> 3.12](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)

## Introduction
The PyASCVD package implements the [American College of Cardiology's Risk Estimator Plus Equation ](https://tools.acc.org/ascvd-risk-estimator-plus/#!/calculate/estimate/) in python. It's a mixed Rust and Python
module, leveraging the speed of Rust for equation implementation and the flexibility of Python for ease of use.

## Installation
**Requirements:**
- Python 3.7 to 3.12 on a Silicon Mac / Linux system (more compatibility coming soon)


To install the package, pip install using:
```bash
pip install pypascvd
```

## TL;DR

```python
import pyascvd

pyascvd.ascvd(
        age=40,
        sex="male",
        race="white",
        systolic_blood_pressure=120,
        total_cholesterol=213,
        hdl_cholesterol=50,
        diabetes=False,
        smoker=False,
        on_hypertension_treatment=False,
)
```

## Examples
Coming soon

## Program Structure

This is a mixed [Rust](https://www.rust-lang.org/) and Python module.

The rust source code is used to implement the equations. This is a lower level language that requires compilation prior to being run -- and thus is many times faster than pure python.

The rust source code is located in the /src directory.

The python source is located in the /pyascvd directory.

Unit tests are implemented in the /tests directory using [slash](https://getslash.github.io/slash/).