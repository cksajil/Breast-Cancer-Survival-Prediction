import joblib
from os import path
from src import data_loader
from sklearn import metrics
from utils.general import load_config


def main():
    config = load_config("config.yaml")
    X_train, X_test, y_train, y_test = data_loader()
    for properties in config["models"].values():
        clf = joblib.load(path.join(config["model_directory"], properties["filename"]))
        y_pred = clf.predict(X_test)
        accuracy = metrics.accuracy_score(y_test, y_pred)
        print(accuracy)


if __name__ == "__main__":
    main()
