# this script is used to load the configuration file
# and set, change the configuration of the project and packages


import os
import json
import sys
from rich.console import Console

from tools.env import prepare_project

console = Console()


class CCConfig:
    def __init__(self):
        config_file_dir = os.path.dirname(__file__)
        self.configs = json.load(open(config_file_dir + '/../configs/ccroot.json'))
        self.lang = self.configs["lang"]


def cc_root_init():
    prepare_project(cc_root_get_project_dir())
    # there are two main mode of the cc_root, source mode and library mode


def cc_root_get_project_dir():
    if os.getenv("CC_PROJ_ROOT_DIR") is not None:
        return os.getenv("CC_PROJ_ROOT_DIR")
    else:
        return os.getcwd()


def cc_root_get_project_cc_dir():
    return cc_root_get_project_dir() + "/cc_root"


def cc_root_get_project_config_file():
    return cc_root_get_project_cc_dir() + "/cc_root_project.json"


def cc_root_check_project():
    # check if a .cc_root_project.json file exists
    # in the current directory (shell running directory) or not
    # if not, return False
    # if exists, return True

    # check if the .cc_root_project.json file exists in pwd directory
    if os.path.exists(cc_root_get_project_config_file()):
        return True
    else:
        return False


def cc_root_config():
    if not cc_root_check_project():
        console.print("No project configuration file found in [ " + os.getcwd() + " ]")
        console.print("Do you want to init as a new project? (y/n)")
        # ask user if they want to init as a new project

        user_input = input()
        if user_input == "y":
            cc_root_init()
        elif user_input == "n":
            print("No valid config found")
            sys.exit(0)
        else:
            # ask again
            cc_root_config()
    else:
        # load the project configuration file
        console.print("Project configuration file found in [ " + os.getcwd() + " ]")
        project = json.load(open(os.getcwd() + "/cc_root/cc_root_project.json"))
        console.print(json.dumps(project, indent=4))


def cc_root_get_config():
    cc_config = CCConfig()
    return cc_config.configs
