from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def build_lr_baseline():
    """
    Build basic baseline using a Logistic Regression.

    Returns
    -------
    sklearn.pipeline.Pipeline
        Pipeline of the classifier
    """
    return Pipeline([
        ("classifier", LogisticRegression(
            solver="lbfgs",
            max_iter=100,
            random_state=42,
            n_jobs=-1,
        )),
    ])


def build_rf_baseline():
    """
    Build basic baseline using a Random Forest Classifier.

    Returns
    -------
    sklearn.pipeline.Pipeline
        Pipeline of the classifier
    """
    return Pipeline([
        ("classifier", RandomForestClassifier(
            n_estimators=300,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1,
        )),
    ])