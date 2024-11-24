# this script is used to load the configuration file
# and set, change the configuration of the project and packages
import argparse
import os
import json
import string
import sys
from rich.console import Console

from tools.env import prepare_project
from tools.i18n import i18n
from tools.Menu.Menu import display_menu
from tools.Menu.MenuOption import MenuOption

console = Console()


class CCConfig:
    def __init__(self):
        config_file_dir = os.path.dirname(__file__)
        self.configs = json.load(open(config_file_dir + '/../configs/ccroot.json'))
        self.lang = self.configs["lang"]


def cc_root_init():
    prepare_project(cc_root_get_project_dir())
    # there are two main mode of the cc_root, source mode and library mode


def cc_root_config_platform(input_platform: string = None):
    console.print("Setting the platform for the project", style="bold green")
    json_file = os.getenv("CC_ROOT_CONFIGS_DIR") + "/target_sys.json"
    valid_sys = json.load(open(json_file))

    if input_platform == "help" or input_platform == "list":
        platform_help = ("Valid platform options are: \n"
                         "") + ", ".join([sys_opt['title'] for sys_opt in valid_sys])
        console.print(platform_help, style="bold")
        sys.exit(0)

    options_form_json = [MenuOption(sys_opt['id'], sys_opt['title'], sys_opt['value'], sys_opt['comment']) for sys_opt
                         in valid_sys]

    selection = display_menu("Please select target system", options_form_json)

    if selection:
        config = cc_root_get_project_config()
        # set the platform object in the project configuration with json format
        config["platform"] = selection.to_json()
        cc_root_save_project_config(config)


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


def cc_root_get_project_config():
    # check if the project configuration file exists
    # if exists, load the file and return the content
    # if not, return None
    if cc_root_check_project():
        return json.load(open(cc_root_get_project_config_file()))
    else:
        return None


def cc_root_save_project_config(config):
    # save the project configuration to the project configuration file
    with open(cc_root_get_project_config_file(), "w") as f:
        json.dump(config, f, indent=4)


def cc_root_config():
    # read command line arguments
    parser = argparse.ArgumentParser(description=i18n("description"))
    parser.add_argument("config", help="Config basic command")

    project = {}

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

    # now check if user input options in [ --platform --toolchain ]
    # read all valid platform and toolchain from the configuration file
    # and display them to the user

    parser.add_argument("--platform", nargs='?', const="list", default=None)
    # parser.add_argument("--toolchain", help="Set the toolchain for the project")
    args = parser.parse_args()

    if args.platform:
        # set the platform for the project
        cc_root_config_platform(args.platform)
        pass


def cc_root_get_config():
    cc_config = CCConfig()
    return cc_config.configs
