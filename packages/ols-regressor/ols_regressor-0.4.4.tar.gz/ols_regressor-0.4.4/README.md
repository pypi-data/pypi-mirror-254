# OLS_Regressor

[![Documentation Status](https://readthedocs.org/projects/olsregressor/badge/?version=latest)](https://olsregressor.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![PyPI](https://img.shields.io/pypi/v/OLS_regressor.svg)](https://olsregressor.readthedocs.io/en/latest/?badge=latest%2F)
[![ci-cd](https://github.com/UBC-MDS/PyXplor/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/OLS_regressor/actions/workflows/ci-cd.yml)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![version](https://img.shields.io/github/v/release/UBC-MDS/OLS_regressor) 
![release](https://img.shields.io/github/release-date/UBC-MDS/OLS_regressor)

<p align="center">
  <img src="/docs/logo.jpg" width="400" height="400">
</p>

## 📌 About

The OLS Regression Package is a Python library designed to streamline the process of performing Ordinary Least Squares (OLS) regression analysis. Whether you're a data scientist, researcher, or analyst, this package aims to provide a simple and efficient tool for fitting linear models to your data. It will fit a linear model with coefficients w = (w1, w2, ..., wn) to minimize Residual Sum of Squares (RSS) between the observed targets values in the dataset, and the targets predicted by the linear approximation for the examples in the dataset.


## 💻 Installation
### Install the package from PyPi
Run this command to install the `ols_regressor` package from PyPi

```bash
pip install ols_regressor
```


### Install the package from GitHub
Run the following commands to install from GitHub if the installation is unsuccessful from PyPi.

**Clone the repository**
Open your terminal, navigate to where you would like the repository to be cloned and run the following command:
```bash
$ git clone git@github.com:UBC-MDS/OLS_regressor.git
```

**Create the conda environment and activate it**
Run the following command to create the conda environment which will include the necessary Python and Poetry versions and dependencies:
```bash
conda env create --name ols_regressor python=3.9 poetry==1.7.1 -y
```

Next, run the following command to activate the conda environment we created:
```bash
conda activate `ols_regressor`
```

**Install the package using Poetry**
Run the following command to install the package `ols_regressor`:
```bash
poetry install
```

## 💡 Functions

- `fit`: Fits the linear model according to the OLS mechanism.
- `predict`: Predicts target values using the fitted linear model.
- `score`: Calculates the coefficient of determination R-squared value for the prediction.
- `cross_validate`: Performs cross-validated Ordinary Least Squares (OLS) regression.

## ⭐ Usage

This guide provides a quick start to using the OLS_Regressor package, specifically the LinearRegressor class, to perform linear regression analysis. The package offers simple-to-use methods for fitting the model, making predictions, and evaluating the performance. For more details about the package, please see the [vingette](https://olsregressor.readthedocs.io/en/latest/?badge=latest) for detailed usage.

### Importing the LinearRegressor

```Python
from OLS_Regressor.regressor import LinearRegressor
from Ols_regressor.cross_validate import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
```

### Fitting the Model

To fit the linear regression model, you need to have your dataset ready, typically split into features (X) and the target variable (y). Here's how you can fit the model:

```Python
# Assuming X and y are your features and target variable respectively
regressor = LinearRegressor()
regressor.fit(X, y)
```

### Making Predictions

Once the model is trained, you can make predictions on new data:

```Python
# Assuming X_new represents new data
predictions = regressor.predict(X_new)
```

### Evaluating the Model

To evaluate the performance of your model, you can use the score method, which by default provides the R-squared value of the predictions:

```Python
# Evaluating the model on test data
r_squared = regressor.score(X_test, y_test)
print(f"R-squared: {r_squared}")
```

### Cross-Validation

The OLS_Regressor package provides a cross_validate function to help evaluate the model's performance across different partitions of the dataset, ensuring a more robust assessment than using a single train-test split.

To use cross_validate, you must first import it from the package, then provide it with your dataset and the model you wish to evaluate. Here's an example:

```Python
# Creating an instance of LinearRegressor
model = LinearRegressor()

# Performing cross-validation
results = cross_validate(model, X, y, cv=5)  # cv is the number of folds

# Printing the results
print("Cross-validation results:", results)
```

## 🧪 Auto-test

To run the auto-test supported by `pytest`, simply run the following command in the terminal or commandline tools:

```bash
pytest tests/
```

## ✅ `OLS_Regressor` use in Python ecosystem

The OLS Regression Package seamlessly integrates into the rich Python ecosystem, offering a specialized solution for Ordinary Least Squares (OLS) regression analysis. While various Python libraries provide general-purpose machine learning and statistical functionalities, our package focuses specifically on the simplicity and efficiency of linear regression. scikit-learn is a widely used machine learning library that encompasses regression among its many capabilities [`scikit-learn`](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning). Our package distinguishes itself by providing a lightweight and user-friendly interface tailored for users seeking a straightforward solution for OLS regression without the overhead of extensive machine learning or statistical functionalities. If you find that your needs align more closely with a broader set of machine learning tools or comprehensive statistical modeling, scikit-learn or statsmodels may be suitable alternatives. As of [2024-01-12], no existing package caters specifically to OLS regression with our package's emphasis on simplicity and ease of use.

## 🤝 Contributors

- Xia Yimeng (@YimengXia)
- Sifan Zhang (@Sifanzzz)
- Charles Xu (@charlesxch)
- Waleed Mahmood (@WaleedMahmood1)

## 🌏 Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## 📗 License

`OLS_Regressor` is licensed under the terms of the MIT license.

## 👏 Credits

`OLS_Regressor` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## 🖇️ References
Giriyewithana, N. (2023). Australian Vehicle Prices [Data set]. Kaggle. https://www.kaggle.com/datasets/nelgiriyewithana/australian-vehicle-prices

Michael, B. (2023, February 23). How Does Linear Regression Really Work. Towards Data Science. https://towardsdatascience.com/how-does-linear-regression-really-work-2387d0f11e8

scikit-learn: Machine Learning in Python. https://scikit-learn.org/stable/

pandas: A Foundational Python Library for Data Analysis and Statistics. https://pandas.pydata.org/

pytest: helps you write better programs https://pytest.org/


