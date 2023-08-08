from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from utils.general import load_config, create_folder, model_trainer
from src import data_loader


def main():
    X_train, X_test, y_train, y_test = data_loader()

    config = load_config("config.yaml")
    create_folder(config["model_directory"])

    print("Training Decision Tree Model")
    clf_DT = DecisionTreeClassifier()
    dt_params = {"ccp_alpha": [0.1, 0.01], "max_depth": [5, 7]}
    model_trainer(clf_DT, dt_params, X_train, y_train, "decision_tree")

    print("Training Support Vector Model")
    clf_SVM = svm.SVC()
    svm_params = {"C": [0.1, 10], "gamma": [0.1, 0.01]}
    model_trainer(clf_SVM, svm_params, X_train, y_train, "support_vector_machine")

    print("Working on Random Forest Model")
    clf_RF = RandomForestClassifier()
    rf_params = {"max_depth": list(range(10, 12)), "n_estimators": [50, 100]}
    model_trainer(clf_RF, rf_params, X_train, y_train, "random_forest")


if __name__ == "__main__":
    main()
