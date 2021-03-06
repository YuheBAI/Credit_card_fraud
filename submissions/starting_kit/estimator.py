import numpy as np
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from imblearn import over_sampling, under_sampling


class Uniform(BaseEstimator): # dummy estimator to test ramp
    def __init__(self, value=0):
        self.value = value

    def fit(self, X, y):
        assert len(X) == len(y), f"Wrong dimensions (len(X): {len(X)}, len(y): {len(y)})."
        return self
    
    def predict(self, X):
        #############################################################
        # Return a (n_samples,2) array with probs for each class    #
        # (with sklearn classifier it corresponds to predict_proba) #
        # In practice, if you have y_pred a (n_samples,) array of   #
        # 0s and 1s or of probabilities of being 1, just return     #
        # something like ***np.array([1 - y_pred, y_pred]).T***     #
        #############################################################
        y_pred = np.ones((X.shape[0],)) * self.value
        return np.array([1 - y_pred, y_pred]).T


def get_estimator():
    estimator = Uniform(value=1)
    pipeline = Pipeline(steps=[('estimator', estimator)])
    return pipeline
