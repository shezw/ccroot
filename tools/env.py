# this file is used to set the environment of the cc_root
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
