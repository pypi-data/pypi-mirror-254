import numpy as np
import pandas as pd


class LinearRegressor():
    """
    Ordinary Least Squares Linear Regressor

    LinearRegressor will fit a linear model with coefficients w = (w1, w2, ..., wn)
    to minimize Residual Sum of Squares (RSS) between the observed targets values
    in the dataset, and the targets predicted by the linear approximation for the
    examples in the dataset.
    """
    def __init__(self):
        self.coef = None
        pass

    def fit(self, X, y, lambda_reg=0.1):
        X_np = np.array(X)
        y_np = np.array(y)

        # Check if dimensions of both matrices are correct
        if X_np.ndim != 2:
            raise ValueError("X should be a 2D array.")
        if y_np.ndim != 1:
            raise ValueError("y should be a 1D array.")

        # Check if the number of samples in X and y match
        if X_np.shape[0] != y_np.shape[0]:
            raise ValueError("The number of examples in X and y should be equal.")

        if X_np.shape[0] < X_np.shape[1]:
            raise ValueError("The number of examples in X should be greater than the number of features.")

        # Add a column of ones for the intercept term
        X_np = np.hstack((np.ones((X_np.shape[0], 1)), X_np))

        # Fit OLS with regularization (you can adjust the regularization parameter)
        self.coef = np.linalg.inv(X_np.T @ X_np + lambda_reg * np.eye(X_np.shape[1])) @ X_np.T @ y_np

        return self.coef

    def predict(self, X):
        """
        Predicts target values using the fitted linear model.
        
        Parameters
        ----------
        X : array-like matrix of shape (n_samples, n_features)
            Feature values that will be used to make predictions.
        
        Returns
        -------
        predictions : array-like matrix of shape (n_samples, n_targets)
            Predicted target values for the input feature values.
        """
        if self.coef is None:
            raise ValueError("Model not fitted. Call fit first.")

        X = np.array(X)

        # Check if dimensions of X are correct
        if X.ndim != 2:
            raise ValueError("X should be a 2D array.")

        # Check if the number of features in X equals to the number of coefficients
        if X.shape[1] != len(self.coef)-1:
            raise ValueError("The number of features in X should be equal to the number of coefficients.")
        
        # Check if non-numeric values exist in input
        if not np.issubdtype(X.dtype, np.number):
            raise ValueError("Input contains non-numeric values.")
            
        # Check if NaN values exist in input
        if np.isnan(X).any():
            raise ValueError("Input contains NaN values.")
        
        # check if infinite values exist in input
        if not np.isfinite(X).all():
            raise ValueError("Input contains infinite values.")

        X = np.hstack((np.ones((X.shape[0], 1)), X))

        pred = X @ self.coef
        return pred


    def score(self, X, y):
        """
        Calculates the coefficient of determination R^2 for the prediction.

        Parameters
        ----------
        X : array-like matrix, shape (n_samples, n_features)
            Feature dataset.

        y : array-like matrix, shape (n_samples, )
            True target values.

        Returns
        -------
        r2_score : float
            Coefficient of determination R^2.
        """
        # Ensure y is a numpy array
        y_true = np.array(y)

        # Predict the y values using the model
        y_pred = self.predict(X)

        # Calculate the mean of the true y values
        y_true_mean = np.mean(y_true)

        # Calculate the Total Sum of Squares (SST)
        SST = np.sum((y_true - y_true_mean) ** 2)

        # Calculate the Sum of Squared Errors (SSE)
        SSE = np.sum((y_true - y_pred) ** 2)

        # Calculate R^2
        r2 = 1 - (SSE / SST)

        return r2
