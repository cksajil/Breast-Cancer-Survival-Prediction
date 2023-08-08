from src import data_loader
from utils.general import load_config


def main():
    config = load_config("config.yaml")
    X_train, X_test, y_train, y_test = data_loader()


if __name__ == "__main__":
    main()
