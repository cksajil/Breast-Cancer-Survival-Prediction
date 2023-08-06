import pandas as pd
from os import path
from utils.general import load_config


def main():
    config = load_config("config.yaml")
    location = config["data_directory"]
    mutation_file = config["mutation_data"]
    data = pd.read_csv(path.join(location, mutation_file))
    print(data)


if __name__ == "__main__":
    main()
