from configparser import ConfigParser
import os


def readConfig(section, key ,file_path="configurationData/config.ini"):
    config = ConfigParser(interpolation=None)
    config.read(file_path)
    return config.get(section, key)




