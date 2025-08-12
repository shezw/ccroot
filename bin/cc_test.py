import json
import sys
import os
import argparse

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tools.env import prepare_env

prepare_env()

from tools.MenuSelection import MenuSelection
from tools.Menu import display_menu

args = sys.argv

if len(args) < 2:
    print("Usage: 'cc_test {testcase} {--options}'")

if args[1] == "menu":

    json_file = os.getenv("CC_ROOT_CONFIGS_DIR") + "/target_sys.json"
    valid_sys = json.load(open(json_file))

    options_form_json = [MenuSelection(sys['id'], sys['title'], sys['value'], sys['comment']) for sys in valid_sys]

    selection = display_menu("Please select target system", options_form_json)

    print(selection)
