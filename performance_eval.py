import joblib
import numpy as np
from os import path
from src import data_loader
from sklearn import metrics
from utils.general import load_config, performance_metrics
from sklearn.model_selection import cross_val_score


def main():
    config = load_config("config.yaml")
    X_train, X_test, y_train, y_test = data_loader()
    for properties in config["models"].values():
        clf = joblib.load(path.join(config["model_directory"], properties["filename"]))
        y_pred = clf.predict(X_test)
        acc = cross_val_score(clf, X_train, y_train, cv=5)
        accuracy_score = (
            str(np.round(acc.mean(), 4)) + " +/- " + str(np.round(acc.std(), 4))
        )
        scores = performance_metrics(y_test, y_pred)
        print(accuracy_score)
        print(scores)


if __name__ == "__main__":
    main()
