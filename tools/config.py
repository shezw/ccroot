# this script is used to load the configuration file
# and set, change the configuration of the project and packages


import os
import json
import sys


class CCConfig:
    def __init__(self):
        config_file_dir = os.path.dirname(__file__)
        self.configs = json.load(open(config_file_dir + '/../configs/ccroot.json'))
        self.lang = self.configs["lang"]

