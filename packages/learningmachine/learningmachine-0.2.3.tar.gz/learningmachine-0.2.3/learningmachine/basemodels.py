import numpy as np
import sklearn.metrics as skm
from subprocess import run
from rpy2.robjects import r
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import (
    FloatMatrix,
    FloatVector,
    IntVector,
    StrVector,
)
from sklearn.base import RegressorMixin, ClassifierMixin
from .base import Base

base = importr("base")
stats = importr("stats")
utils = importr("utils")


class BaseRegressor(Base, RegressorMixin):
    """
    Base Regressor.
    """

    def __init__(self):
        """
        Initialize the model.
        """
        super().__init__()
        self.type_fit = "regression"
        self.obj = r("learningmachine::BaseRegressor$new()")

    def fit(self, X, y):
        """
        Fit the model according to the given training data.
        """
        self.obj["fit"](
            r.matrix(
                FloatVector(X), byrow=True, nrow=X.shape[0], ncol=X.shape[1]
            ),
            FloatVector(y),
        )
        return self

    def predict(self, X):
        """
        Predict using the model.
        """
        return np.asarray(
            self.obj["predict"](
                r.matrix(
                    FloatMatrix(X), byrow=True, nrow=X.shape[0], ncol=X.shape[1]
                )
            )
        )

    def score(self, X, y, scoring=None, **kwargs):
        """Score the model on test set features X and response y.

        Parameters:

            X: {array-like}, shape = [n_samples, n_features]
                Training vectors, where n_samples is the number
                of samples and n_features is the number of features

            y: array-like, shape = [n_samples]
                Target values

            scoring: str
                must be in ('explained_variance', 'neg_mean_absolute_error',
                            'neg_mean_squared_error', 'neg_mean_squared_log_error',
                            'neg_median_absolute_error', 'r2')

            **kwargs: additional parameters to be passed to scoring functions

        Returns:

        model scores: {array-like}

        """

        preds = self.predict(X)

        if type(preds) == tuple:  # if there are std. devs in the predictions
            preds = preds[0]

        if scoring is None:
            scoring = "neg_mean_squared_error"

        # check inputs
        assert scoring in (
            "explained_variance",
            "neg_mean_absolute_error",
            "neg_mean_squared_error",
            "neg_mean_squared_log_error",
            "neg_median_absolute_error",
            "r2",
        ), "'scoring' should be in ('explained_variance', 'neg_mean_absolute_error', \
                           'neg_mean_squared_error', 'neg_mean_squared_log_error', \
                           'neg_median_absolute_error', 'r2')"

        scoring_options = {
            "explained_variance": skm.explained_variance_score,
            "neg_mean_absolute_error": skm.median_absolute_error,
            "neg_mean_squared_error": skm.mean_squared_error,
            "neg_mean_squared_log_error": skm.mean_squared_log_error,
            "neg_median_absolute_error": skm.median_absolute_error,
            "r2": skm.r2_score,
        }

        return scoring_options[scoring](y, preds, **kwargs)


class BaseClassifier(Base, ClassifierMixin):
    """
    Base Classifier.
    """

    def __init__(self):
        """
        Initialize the model.
        """
        super().__init__()
        self.type_fit = "classification"
        self.obj = r("learningmachine::BaseClassifier$new()")

    def fit(self, X, y):
        """
        Fit the model according to the given training data.
        """
        self.obj["fit"](
            r.matrix(
                FloatMatrix(X), byrow=True, nrow=X.shape[0], ncol=X.shape[1]
            ),
            base.as_factor(IntVector(y)),
        )
        self.classes_ = np.unique(y)
        return self

    def predict(self, X):
        """
        Predict classes using the model.
        """
        return np.asarray(
            self.obj["predict"](
                r.matrix(
                    FloatMatrix(X), byrow=True, nrow=X.shape[0], ncol=X.shape[1]
                )
            )
        )

    def predict_proba(self, X):
        """
        Predict probabilities using the model.
        """
        return np.asarray(
            self.obj["predict_proba"](
                r.matrix(
                    FloatMatrix(X), byrow=True, nrow=X.shape[0], ncol=X.shape[1]
                )
            )
        )

    def score(self, X, y, scoring=None, **kwargs):
        """Score the model on test set features X and response y.

        Parameters:

            X: {array-like}, shape = [n_samples, n_features]
                Training vectors, where n_samples is the number
                of samples and n_features is the number of features

            y: array-like, shape = [n_samples]
                Target values

            scoring: str
                must be in ('accuracy', 'average_precision',
                           'brier_score_loss', 'f1', 'f1_micro',
                           'f1_macro', 'f1_weighted',  'f1_samples',
                           'neg_log_loss', 'precision', 'recall',
                           'roc_auc')

            **kwargs: additional parameters to be passed to scoring functions

        Returns:

            model scores: {array-like}

        """

        preds = self.predict(X)

        if scoring is None:
            scoring = "accuracy"

        # check inputs
        assert scoring in (
            "accuracy",
            "average_precision",
            "brier_score_loss",
            "f1",
            "f1_micro",
            "f1_macro",
            "f1_weighted",
            "f1_samples",
            "neg_log_loss",
            "precision",
            "recall",
            "roc_auc",
        ), "'scoring' should be in ('accuracy', 'average_precision', \
                           'brier_score_loss', 'f1', 'f1_micro', \
                           'f1_macro', 'f1_weighted',  'f1_samples', \
                           'neg_log_loss', 'precision', 'recall', \
                           'roc_auc')"

        scoring_options = {
            "accuracy": skm.accuracy_score,
            "average_precision": skm.average_precision_score,
            "brier_score_loss": skm.brier_score_loss,
            "f1": skm.f1_score,
            "f1_micro": skm.f1_score,
            "f1_macro": skm.f1_score,
            "f1_weighted": skm.f1_score,
            "f1_samples": skm.f1_score,
            "neg_log_loss": skm.log_loss,
            "precision": skm.precision_score,
            "recall": skm.recall_score,
            "roc_auc": skm.roc_auc_score,
        }

        return scoring_options[scoring](y, preds, **kwargs)
