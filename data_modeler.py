import numpy as np
import pandas as pd
from os import path
from sklearn import preprocessing
from utils.general import load_config
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split


def main():
    config = load_config("config.yaml")
    location = config["data_directory"]
    mutation_file = config["mutation_data"]
    data = pd.read_csv(path.join(location, mutation_file), low_memory=False)

    data = data.drop(["death_from_cancer"], axis=1)
    data = data.dropna()

    y = data["overall_survival"].values
    data = data.drop(["overall_survival"], axis=1)

    numerical_feats = data.select_dtypes("number").columns
    categorical_feats = data.select_dtypes("object").columns

    catdata = data[categorical_feats]
    numdata = data[numerical_feats]

    numdata_scaled = preprocessing.scale(numdata)

    encoder = OneHotEncoder(handle_unknown="ignore")
    encoder.fit(catdata)
    catendata = encoder.transform(catdata).toarray()

    X = np.concatenate((numdata_scaled, catendata), axis=1)

    (X_train, X_test, y_train, y_test) = train_test_split(
        X, y, test_size=0.30, random_state=42
    )

    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)


if __name__ == "__main__":
    main()
