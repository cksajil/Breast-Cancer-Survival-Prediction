from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from utils.general import load_config, create_folder, model_trainer
from src import data_loader


def main():
    model_classes = {
        "Decision Tree Classifier": DecisionTreeClassifier,
        "Random Forest Classifier": RandomForestClassifier,
        "Support Vector Classifier": SVC,
    }

    X_train, X_test, y_train, y_test = data_loader()

    config = load_config("config.yaml")
    create_folder(config["model_directory"])

    for properties in config["models"].values():
        params = properties["param_grid"]
        classifier = model_classes[properties["name"]]
        clf = classifier()
        model_trainer(clf, params, X_train, y_train, properties)


if __name__ == "__main__":
    main()
