from numpy import random
import numpy as np
import time

def cross_validate(model, X, y, cv=5, random_state=None):
    """
    Perform cross-validated Ordinary Least Squares (OLS) regression.

    Parameters
    ----------
    model : object
        Name of the model to run cross_validate with 
        (it will be OLS in this case)
    
    X : array-like matrix of shape (n_examples, n_features)
        Dataset that will be used as the feature values to train the model.
    
    y : array-like matrix of shape (n_examples, n_targets)
        Dataset that will be used as the target values to train the model.
    
    cv : int, optional
        Number of cross-validation folds. Default is 5.
    
    random_state : int or None, optional 
        Seed for reproducibility. Default is None.

    Returns
    -------
    scores : dict
        A dictionary containing arrays for train and test scores, fit and score times.
        'train_score', 'test_score', 'fit_time', 'score_time'.

    Example
    -------
    from sklearn.linear_model import LinearRegression
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    y = np.array([13, 14, 15, 16])
    model = LinearRegression()
    scores = cross_validate(model, X, y, cv=5)
    print(scores)
    {'train_score': [...], 'test_score': [...], 'fit_time': [...], 'score_time': [...]}
    """
    # exception handling
    if not isinstance(model, object):
        raise TypeError("model is not a valid regression model instance")
    if not hasattr(model, "fit") or not hasattr(model, "score"):
        raise TypeError("model is not a valid regression model instance")
    if not isinstance(X, np.ndarray):
        raise ValueError("X is not a numpy array")
    if not isinstance(y, np.ndarray):
        raise ValueError("y is not a numpy array")
    if X.shape[0] != y.shape[0]:
        raise ValueError(f"The shape of X {X.shape} is not compatible with the shape of y {y.shape}")
    if type(cv) is not int or cv <= 0:
        raise ValueError("cross validation fold must be a positive integer")
    
    # Set seed for reproducibility
    random.seed(random_state)

    # Combine X and y for shuffling
    data_combined = np.column_stack((X, y))
    np.random.shuffle(data_combined)

    # Create batches for cross-validation
    batch_size = data_combined.shape[0] // cv
    batches = [
        data_combined[i: i + batch_size]
        for i in range(0, data_combined.shape[0], batch_size)
    ]

    # Initialize lists to store results
    train_score, test_score = [], []
    fit_time, score_time = [], []

    # Cross-validation loop
    for i in range(len(batches)):
        train_batches = np.vstack(batches[:i] + batches[i+1:])

        # Fit model
        t = time.time()
        model.fit(train_batches[:, :-1], train_batches[:, -1])
        fit_time.append(time.time() - t)
        t = time.time()

        # Score model
        test_score.append(model.score(batches[i][:, :-1], batches[i][:, -1]))
        score_time.append(time.time() - t)
        train_score.append(
            model.score(train_batches[:, :-1], train_batches[:, -1])
        )

    # return results    
    return {
        "train_score": train_score,
        "test_score": test_score,
        "fit_time": fit_time,
        "score_time": score_time,
    }