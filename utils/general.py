import os
import yaml
import pandas as pd
from os import path
from time import time
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
    """
    Function to convert list of json content to dataframe
    """
    df = pd.DataFrame.from_dict(json_content, orient="columns")
    return df


def create_folder(directory):
    """Function to create a folder in a location if it does not exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)


def timer_function(myfunc):
    """
    A decorator function to count model training
    and hyper parameter optimization time
    """

    def wrapper_function(*args, **kwargs):
        t1 = time()
        result = myfunc(*args, **kwargs)
        t2 = time()
        print(f"{args[-1]} model trained in {(t2-t1):.4f}s")
        return result

    return wrapper_function


@timer_function
def model_trainer(clf, params, X_train, y_train, label):
    """
    A function to train given model using training data
    and do the hyperparament optimization using gridsearch
    """
    config = load_config("config.yaml")
    clf = GridSearchCV(clf, params, cv=5, scoring="roc_auc", refit=True)
    clf.fit(X_train, y_train)
    print(clf.best_params_)
    dump(clf, path.join(config["model_directory"], label + ".joblib"))
