# this script is used to manager packages in the project
# include add, remove and list packages
import os

CC_ROOT_PACKAGES_DIR = os.getenv("CC_ROOT_PACKAGES_DIR")
VALID_VERSION_SYMBOL = ['@', ':', '==', ' ']


def search_package(search_package_name):
    global CC_ROOT_PACKAGES_DIR

    package_name = search_package_name
    package_ver = ''
    # search package json in the package index directory
    # get the first char of the package name
    # and find the package json file in the directory

    # check package name has version symbol
    # if it has, remove the version symbol and version
    for symbol in VALID_VERSION_SYMBOL:
        if symbol in search_package_name:
            package_name = search_package_name.split(symbol)[0]
            package_ver = search_package_name.split(symbol)[1]
            break

    package_index_dir = CC_ROOT_PACKAGES_DIR + '/index/' + package_name[0].lower()

    # check the package folder is existed
    # and then check the {version}.json file is existed

    # package folder is package_index_dir/{package_name}
    package_dir = package_index_dir + '/' + package_name
    if not os.path.exists(package_dir):
        print("Package not found")
        return
    else:
        if package_ver == '':
            # means the package name has no version symbol
            # list all the versions of the package
            for package_ver in os.listdir(package_dir):
                if package_ver.endswith('.json'):
                    print(package_ver.split('.json')[0])
            return
        else:
            # check the {version}.json file is existed
            if not os.path.exists(package_dir + '/' + package_ver + '.json'):
                print("Package version not found")
                return
            else:
                # print the package information
                package_info = open(package_dir + '/' + package_ver + '.json').read()
                print(package_info)
                return


class CC_Package:
    def __init__(self):
        pass

    def add_package(self, package_name):
        pass

    def remove_package(self, package_name):
        pass

    def list_packages(self):
        pass
