import pandas as pd
import numpy as np
from typing import Tuple

def load_and_split_features(path: str, path_classes: str, t_val: int = 31, t_test: int = 36) -> Tuple[np.ndarray, list, np.ndarray, list, np.ndarray, list]:
    """
    Load the transactions features dataset and split it into train, validation and test.

    Parameters
    ----------
    path: str
        Path of the transactions features dataset
    path: str
        Path of the transactions classes dataset
    t_val: int
        First time-step for the validation
    t_test: int
        First time_step for test

    Returns
    -------
    X_train : np.ndarray
        Training feature matrix.
    y_train : list
        Training labels.
    X_val : np.ndarray
        Validation feature matrix.
    y_val : list
        Validation labels.
    X_test : np.ndarray
        Test feature matrix.
    y_test : list
        Test labels.
    """
    
    df = pd.read_csv(path)
    df_classes = pd.read_csv(path_classes)
    df.insert(loc=2, column='class', value=df_classes['class'])

    # Keep only licit and illicit labels
    df = df[df["class"] != 3]

    df = df.select_dtypes(include="number")
    df = df.drop(columns=["txId"], errors='ignore')
    df.dropna(inplace=True)

    df_train = df[df["Time step"] < t_val]
    y_train = list(df_train["class"])
    X_train = df_train.drop(columns=["class"], errors='ignore').to_numpy()

    df_val = df[
        (df["Time step"] >= t_val) &
        (df["Time step"] < t_test)
    ]
    y_val = list(df_val["class"])
    X_val = df_val.drop(columns=["class"], errors='ignore').to_numpy()

    df_test = df[t_test <= df["Time step"]]
    y_test = list(df_test["class"])
    X_test = df_test.drop(columns=["class"], errors='ignore').to_numpy()

    return X_train, y_train, X_val, y_val, X_test, y_test