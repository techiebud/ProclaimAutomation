from enum import Enum
import configparser


class ProclaimAction(Enum):
    Authenticate = 1
    NextSlide = 2
    PreviousSlide = 3

    # Method to read config file settings


def read_config():
    config = configparser.ConfigParser()
    config.read('configurations.ini')
    return config
