import os
import yaml
import pandas as pd
from os import path
from joblib import dump
from sklearn.model_selection import GridSearchCV


def load_config(config_name):
    """
    A function to load and return config file in YAML format
    """
    CONFIG_PATH = "./config/"
    with open(os.path.join(CONFIG_PATH, config_name)) as file:
        config = yaml.safe_load(file)

    return config


def json_to_df(json_content):
    df = pd.DataFrame.from_dict(json_content, orient="columns")
    return df


def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def model_trainer(clf, params, X_train, y_train, label):
    config = load_config("config.yaml")
    clf = GridSearchCV(clf, params, cv=5, scoring="roc_auc", refit=True)
    clf.fit(X_train, y_train)
    print(clf.best_params_)
    dump(clf, path.join(config["model_directory"], label + ".joblib"))
