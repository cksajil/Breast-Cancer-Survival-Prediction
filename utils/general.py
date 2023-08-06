import os
import yaml
import pandas as pd


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
