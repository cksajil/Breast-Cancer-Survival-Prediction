import numpy as np
import pandas as pd
from os import path
from sklearn import svm
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from utils.general import load_config, create_folder, model_trainer


def main():
    print("Reading configuration file")
    config = load_config("config.yaml")
    location = config["data_directory"]
    mutation_file = config["mutation_data"]

    print("Read data file")
    data = pd.read_csv(path.join(location, mutation_file), low_memory=False)

    data = data.drop(["death_from_cancer"], axis=1)
    data = data.dropna()

    print("Separate features and labels")
    y = data["overall_survival"].values
    data = data.drop(["overall_survival"], axis=1)

    numerical_feats = data.select_dtypes("number").columns
    categorical_feats = data.select_dtypes("object").columns

    catdata = data[categorical_feats]
    numdata = data[numerical_feats]

    numdata_scaled = preprocessing.scale(numdata)

    print("Encoding categorical data")
    encoder = OneHotEncoder(handle_unknown="ignore")
    encoder.fit(catdata)
    catendata = encoder.transform(catdata).toarray()

    X = np.concatenate((numdata_scaled, catendata), axis=1)

    print("Performing Train-Test Split")
    (X_train, X_test, y_train, y_test) = train_test_split(
        X, y, test_size=0.30, random_state=42
    )

    create_folder(config["model_directory"])

    # print("Training Logistic Regression Model")
    # clf_LR = LogisticRegression()
    # lr_params = {"C": np.logspace(0.01, 2, 3), "penalty": ["l1", "l2"]}
    # model_trainer(clf_LR, lr_params, X_train, y_train, "logistic_regression")

    # print("Training Decision Tree Model")
    # clf_DT = DecisionTreeClassifier()
    # dt_params = {"ccp_alpha": [0.1, 0.01, 0.001], "max_depth": [5, 6, 7, 8, 9]}
    # model_trainer(clf_DT, dt_params, X_train, y_train, "decision_tree")

    print("Training Support Vector Model")
    clf_SVM = svm.SVC()
    svm_params = {"C": [0.1, 1, 10], "gamma": [1, 0.1, 0.01]}
    model_trainer(clf_SVM, svm_params, X_train, y_train, "support_vector_machine")


if __name__ == "__main__":
    main()
