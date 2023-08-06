import yaml
from os import path


def load_config(config_name):
    """
    A function to load and return config file in YAML format
    """
    CONFIG_PATH = "./config/"
    with open(path.join(CONFIG_PATH, config_name)) as file:
        config = yaml.safe_load(file)

    return config
