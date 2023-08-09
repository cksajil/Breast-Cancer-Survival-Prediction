import os
import yaml
import pandas as pd
from os import path
from time import time
from joblib import dump
from sklearn import metrics
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
        model_name = args[-1]["name"]
        t1 = time()
        result = myfunc(*args, **kwargs)
        t2 = time()
        print(f"{model_name} model trained in {(t2-t1):.4f}s")
        return result

    return wrapper_function


@timer_function
def model_trainer(clf, params, X_train, y_train, properties):
    """
    A function to train given model using training data
    and do the hyperparament optimization using gridsearch
    """
    config = load_config("config.yaml")
    clf = GridSearchCV(clf, params, cv=5, scoring="roc_auc", refit=True)
    clf.fit(X_train, y_train)
    dump(clf, path.join(config["model_directory"], properties["filename"]))


def performance_metrics(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    for i in range(len(y_hat)):
        if y_actual[i] == y_hat[i] == 1:
            TP += 1
        if y_hat[i] == 1 and y_actual[i] != y_hat[i]:
            FP += 1
        if y_actual[i] == y_hat[i] == 0:
            TN += 1
        if y_hat[i] == 0 and y_actual[i] != y_hat[i]:
            FN += 1
    acc = (TP + TN) / (TP + FP + TN + FN)
    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)
    fpr = FP / (FP + TN)
    (fp_rate, tp_rate, thresholds) = metrics.roc_curve(y_actual, y_hat)
    roc_auc = metrics.auc(fp_rate, tp_rate)
    return acc, roc_auc, sensitivity, specificity, fpr
