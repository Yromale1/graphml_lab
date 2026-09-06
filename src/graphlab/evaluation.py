from sklearn.metrics import (
    average_precision_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
)


def evaluate_binary_classifier(model, X, y):
    y_pred = model.predict(X)
    y_proba = model.predict_proba(X)[:, 1]

    return {
        "pr_auc": average_precision_score(y, y_proba),
        "roc_auc": roc_auc_score(y, y_proba),
        "classification_report": classification_report(
            y, y_pred
        ),
        "confusion_matrix": confusion_matrix(y, y_pred),
    }