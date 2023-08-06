from os import path
from utils.general import load_config


def main():
    config = load_config("config.yaml")
    print(config["data_url"])


if __name__ == "__main__":
    main()


# kaggle datasets download -d raghadalharbi/breast-cancer-gene-expression-profiles-metabric
