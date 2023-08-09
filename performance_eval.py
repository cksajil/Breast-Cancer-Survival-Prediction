import joblib
import numpy as np
import pandas as pd
from os import path
from src import data_loader
from sklearn import metrics
from utils.general import load_config, performance_metrics
from sklearn.model_selection import cross_val_score


def main():
    config = load_config("config.yaml")
    X_train, X_test, y_train, y_test = data_loader()
    results = pd.DataFrame(
        columns=[
            "Model",
            "Accuracy",
            "AUC",
            "Sensitivity",
            "Specificity",
            "FPR",
        ]
    )
    print("Evaluating models on test data")
    for properties in config["models"].values():
        clf = joblib.load(path.join(config["model_directory"], properties["filename"]))
        y_pred = clf.predict(X_test)
        acc, roc, sen, spec, fpr = performance_metrics(y_test, y_pred)
        results.loc[len(results)] = [properties["name"], acc, roc, sen, spec, fpr]

    print(results)


if __name__ == "__main__":
    main()
