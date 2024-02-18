# OLS_Regressor

[![Documentation Status](https://readthedocs.org/projects/olsregressor/badge/?version=latest)](https://olsregressor.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![PyPI](https://img.shields.io/pypi/v/OLS_regressor.svg)](https://olsregressor.readthedocs.io/en/latest/?badge=latest%2F)
![ci-cd](https://github.com/UBC-MDS/OLS_regressor/actions/workflows/ci-cd.yml/badge.svg)
![version](https://img.shields.io/github/v/release/UBC-MDS/OLS_regressor) 
![release](https://img.shields.io/github/release-date/UBC-MDS/OLS_regressor)
[![ci-cd](https://github.com/UBC-MDS/PyXplor/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/OLS_regressor/actions/workflows/ci-cd.yml)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)


## About
The OLS Regression Package is a Python library designed to streamline the process of performing Ordinary Least Squares (OLS) regression analysis. Whether you're a data scientist, researcher, or analyst, this package aims to provide a simple and efficient tool for fitting linear models to your data. It will fit a linear model with coefficients w = (w1, w2, ..., wn) to minimize Residual Sum of Squares (RSS) between the observed targets values in the dataset, and the targets predicted by the linear approximation for the examples in the dataset.

## Installation

```bash
$ pip install ols_regressor
```

## Functions

- `fit`: Fits the linear model according to the OLS mechanism.
- `predict`: Predicts target values using the fitted linear model.
- `score`: Calculates the coefficient of determination R-squared value for the prediction.
- `cross_validate`: Performs cross-validated Ordinary Least Squares (OLS) regression.

## `OLS_Regressor` use in Python ecosystem
The OLS Regression Package seamlessly integrates into the rich Python ecosystem, offering a specialized solution for Ordinary Least Squares (OLS) regression analysis. While various Python libraries provide general-purpose machine learning and statistical functionalities, our package focuses specifically on the simplicity and efficiency of linear regression. scikit-learn is a widely used machine learning library that encompasses regression among its many capabilities [`scikit-learn`](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning). Our package distinguishes itself by providing a lightweight and user-friendly interface tailored for users seeking a straightforward solution for OLS regression without the overhead of extensive machine learning or statistical functionalities. If you find that your needs align more closely with a broader set of machine learning tools or comprehensive statistical modeling, scikit-learn or statsmodels may be suitable alternatives. As of [2024-01-12], no existing package caters specifically to OLS regression with our package's emphasis on simplicity and ease of use.

## Contributors
- Xia Yimeng (@YimengXia)
- Sifan Zhang (@Sifanz)
- Charles Xu (@charlesxch)
- Waleed Mahmood (@WaleedMahmood1)

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`OLS_Regressor` is licensed under the terms of the MIT license.

## Credits

`OLS_Regressor` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
