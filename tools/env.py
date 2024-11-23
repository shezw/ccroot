# this file is used to set the environment of the cc_root
import json
import os


def prepare_env():

    CC_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
    CC_ROOT_BIN_DIR = CC_ROOT_DIR + "/bin"
    CC_ROOT_CONFIGS_DIR = CC_ROOT_DIR + "/configs"
    CC_ROOT_SCRIPTS_DIR = CC_ROOT_DIR + "/scripts"
    CC_ROOT_TOOLS_DIR = CC_ROOT_DIR + "/tools"
    CC_ROOT_PACKAGES_DIR = CC_ROOT_DIR + "/packages"
    CC_ROOT_HOST_DIR = CC_ROOT_DIR + "/host"
    CC_ROOT_BUILD_DIR = CC_ROOT_DIR + "/build"
    CC_ROOT_TARGET_DIR = CC_ROOT_DIR + "/target"

    init_all_dirs = [
        CC_ROOT_DIR,
        CC_ROOT_BIN_DIR,
        CC_ROOT_CONFIGS_DIR,
        CC_ROOT_SCRIPTS_DIR,
        CC_ROOT_TOOLS_DIR,
        CC_ROOT_PACKAGES_DIR,
        CC_ROOT_HOST_DIR,
        CC_ROOT_BUILD_DIR,
        CC_ROOT_TARGET_DIR
    ]

    # export all CC_ROOT variables to the environment
    os.environ["CC_ROOT_DIR"] = CC_ROOT_DIR
    os.environ["CC_ROOT_BIN_DIR"] = CC_ROOT_BIN_DIR
    os.environ["CC_ROOT_CONFIGS_DIR"] = CC_ROOT_CONFIGS_DIR
    os.environ["CC_ROOT_SCRIPTS_DIR"] = CC_ROOT_SCRIPTS_DIR
    os.environ["CC_ROOT_TOOLS_DIR"] = CC_ROOT_TOOLS_DIR
    os.environ["CC_ROOT_PACKAGES_DIR"] = CC_ROOT_PACKAGES_DIR
    os.environ["CC_ROOT_HOST_DIR"] = CC_ROOT_HOST_DIR
    os.environ["CC_ROOT_BUILD_DIR"] = CC_ROOT_BUILD_DIR
    os.environ["CC_ROOT_TARGET_DIR"] = CC_ROOT_TARGET_DIR

    for cc_root_directory in init_all_dirs:
        if not os.path.exists(cc_root_directory):
            os.makedirs(cc_root_directory)


def prepare_project(project_dir):
    CC_PROJ_ROOT_DIR = project_dir + "/cc_root"
    CC_PROJ_HOST_DIR = CC_PROJ_ROOT_DIR + "/host"
    CC_PROJ_HOST_BIN_DIR = CC_PROJ_HOST_DIR + "/bin"
    CC_PROJ_HOST_LIB_DIR = CC_PROJ_HOST_DIR + "/lib"
    CC_PROJ_HOST_INCLUDE_DIR = CC_PROJ_HOST_DIR + "/include"

    CC_PROJ_BUILD_DIR = CC_PROJ_ROOT_DIR + "/build"
    CC_PROJ_TARGET_DIR = CC_PROJ_ROOT_DIR + "/target"
    CC_PROJ_OUT_DIR = CC_PROJ_ROOT_DIR + "/out"

    # save all the project directories to the environment and cc_root_project.json
    os.environ["CC_PROJ_ROOT_DIR"] = CC_PROJ_ROOT_DIR
    os.environ["CC_PROJ_HOST_DIR"] = CC_PROJ_HOST_DIR
    os.environ["CC_PROJ_HOST_BIN_DIR"] = CC_PROJ_HOST_BIN_DIR
    os.environ["CC_PROJ_HOST_LIB_DIR"] = CC_PROJ_HOST_LIB_DIR
    os.environ["CC_PROJ_HOST_INCLUDE_DIR"] = CC_PROJ_HOST_INCLUDE_DIR
    os.environ["CC_PROJ_BUILD_DIR"] = CC_PROJ_BUILD_DIR
    os.environ["CC_PROJ_TARGET_DIR"] = CC_PROJ_TARGET_DIR
    os.environ["CC_PROJ_OUT_DIR"] = CC_PROJ_OUT_DIR

    cc_root_project_config = {
        "CC_PROJ_ROOT_DIR": CC_PROJ_ROOT_DIR,
        "CC_PROJ_HOST_DIR": CC_PROJ_HOST_DIR,
        "CC_PROJ_HOST_BIN_DIR": CC_PROJ_HOST_BIN_DIR,
        "CC_PROJ_HOST_LIB_DIR": CC_PROJ_HOST_LIB_DIR,
        "CC_PROJ_HOST_INCLUDE_DIR": CC_PROJ_HOST_INCLUDE_DIR,
        "CC_PROJ_BUILD_DIR": CC_PROJ_BUILD_DIR,
        "CC_PROJ_TARGET_DIR": CC_PROJ_TARGET_DIR,
        "CC_PROJ_OUT_DIR": CC_PROJ_OUT_DIR
    }

    if not os.path.exists(CC_PROJ_ROOT_DIR):
        os.makedirs(CC_PROJ_ROOT_DIR)
    if not os.path.exists(CC_PROJ_HOST_DIR):
        os.makedirs(CC_PROJ_HOST_DIR)
    if not os.path.exists(CC_PROJ_HOST_BIN_DIR):
        os.makedirs(CC_PROJ_HOST_BIN_DIR)
    if not os.path.exists(CC_PROJ_HOST_LIB_DIR):
        os.makedirs(CC_PROJ_HOST_LIB_DIR)
    if not os.path.exists(CC_PROJ_HOST_INCLUDE_DIR):
        os.makedirs(CC_PROJ_HOST_INCLUDE_DIR)
    if not os.path.exists(CC_PROJ_BUILD_DIR):
        os.makedirs(CC_PROJ_BUILD_DIR)
    if not os.path.exists(CC_PROJ_TARGET_DIR):
        os.makedirs(CC_PROJ_TARGET_DIR)
    if not os.path.exists(CC_PROJ_OUT_DIR):
        os.makedirs(CC_PROJ_OUT_DIR)

    # save the project config to the .cc_root_project.json
    with open(CC_PROJ_ROOT_DIR + "/cc_root_project.json", "w") as f:
        f.write(json.dumps(cc_root_project_config, indent=4))

    print("Project initialized successfully")
