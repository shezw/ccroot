# this script is used to manager packages in the project
# include add, remove and list packages
import json
import os
from rich.console import Console

from tools.config import cc_root_init

console = Console()
cc_root_init()

CC_ROOT_PACKAGES_DIR = os.getenv("CC_ROOT_PACKAGES_DIR")
CC_PROJ_ROOT_DIR = os.getenv("CC_PROJ_ROOT_DIR")
VALID_VERSION_SYMBOL = ['@', ':', '==', ' ']


def search_package(search_package_name):
    global CC_ROOT_PACKAGES_DIR

    package_name = search_package_name
    package_ver = ''
    package = None
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
        # (clearly search failed)
        console.print("Package ["+package_name+"] not found")

        # try matching the package name in index.json
        package_index_file = CC_ROOT_PACKAGES_DIR + '/index.json'
        if os.path.exists(package_index_file):
            package_indexes = json.load(open(package_index_file))

            package_need_select = []

            for package_index in package_indexes:
                if package_name in package_index:
                    package_need_select.append(package_index)

            if len(package_need_select) > 0:
                print("Package ["+package_name+"] not found")
                print("Please select the package:")
                for package_index in package_need_select:
                    print(package_index)
                selected_version = None

                while selected_version not in package_need_select:
                    selected_version = input("Please input the version: ")
                    if selected_version not in package_need_select:
                        print("Invalid version")

                # get the package name and version
                print("Package ["+selected_version+"] selected")

                package_name = selected_version.split('@')[0]
                package_dir = package_index_dir + '/' + package_name
        else:
            print("Package index file not found")
            return None

    if not os.path.exists(package_dir):
        # package folder is not existed, search failed
        console.print("Package ["+package_name+"] not found")
        return None

    else:
        if package_ver == '':
            # means the package name has no version symbol
            # list all the versions of the package
            package_list = []
            for package_ver in os.listdir(package_dir):
                if package_ver.endswith('.json'):
                    package_list.append(package_ver.split('.json')[0])
                    print(package_ver.split('.json')[0])
            return package_list if len(package_list) > 0 else None
        else:
            # check the {version}.json file is existed
            if not os.path.exists(package_dir + '/' + package_ver + '.json'):
                print("Package version ["+package_ver+"] not found")
                return None
            else:
                # print the package information
                package_info = json.load(open(package_dir + '/' + package_ver + '.json'))
                package = package_info

                if 'deps' in package_info and package_info['deps']:
                    print("Dependencies:" + str(package_info['deps']))
                    for dep in package_info['deps']:
                        dep_package = search_package(dep+'@'+package_info['deps'][dep])
                        if dep_package:
                            package['deps'][dep] = dep_package
                        else:
                            print("Dependency ["+dep+"] not found")
                            return None

            return package


def add_package_recurse(package_name, packages: list = None):

    if not packages:
        packages = []

    package = search_package(package_name)

    if isinstance(package, list):
        print("Package ["+package_name+"] has multiple versions")
        print("Please specify the version")

        selected_version = None
        while selected_version not in package:
            selected_version = input("Please input the version: ")
            if selected_version not in package:
                print("Invalid version")
        package_name = package_name + '@' + selected_version
        package = search_package(package_name)

    if not package:
        print("Package ["+package_name+"] not found")
        return None

    # check the package is already in the project or not
    if os.path.exists(CC_ROOT_PACKAGES_DIR + '/' + package_name):
        print("Package ["+package_name+"] is already in the project")
        return None

    if 'deps' in package and package['deps']:
        print("Package ["+package_name+"] has dependencies")
        print("Install dependencies first")

        for dep in package['deps']:
            # print(package['deps'][dep])
            print("Install dependency ["+dep+"@"+package['deps'][dep]['version']+"]")
            dep_package = search_package(dep+'@'+package['deps'][dep]['version'])
            if dep_package:
                packages = add_package_recurse(dep+'@'+package['deps'][dep]['version'], packages)
            else:
                print("Dependency ["+dep+"] not found")
                return None
    if 'deps' in package:
        del package['deps']

    packages.append(package)

    return packages


def get_all_packages():
    global CC_PROJ_ROOT_DIR

    if not os.path.exists(CC_PROJ_ROOT_DIR + '/ccroot_packages.json'):
        print("Packages.json not found")
        return None

    packages = json.load(open(CC_PROJ_ROOT_DIR + '/ccroot_packages.json'))

    return packages



def add_package(package_name):
    global CC_PROJ_ROOT_DIR

    print("Add package ["+package_name+"]")

    packages = get_all_packages()

    if packages is None:
        packages = []

    recurse_packages = add_package_recurse(package_name)

    if recurse_packages is not None and len(recurse_packages) > 0:
        for package in recurse_packages:

            # check if the package is already in the project
            for p in packages:
                if 'name' not in p or 'name' not in package:
                    print("Package is invalid")
                    break
                if p['name'] == package['name'] :
                    print("Package ["+package['name']+"] is already in the project")
                    break

            packages.append(package)

    with open(CC_PROJ_ROOT_DIR + '/ccroot_packages.json', 'w') as f:
        f.write(json.dumps(packages, indent=4))

    print("Package ["+package_name+"] added successfully")

    return packages


def print_package(package,depth=0):
    print("\t" * depth + package['name']+"@"+package['version'])
    if 'deps' in package and package['deps']:
        for dep in package['deps']:
            print("\t" * (depth+1) + dep + "@" + package['deps'][dep])


def list_packages():
    print("List all packages")
    packages = get_all_packages()

    for package in packages:
        package_file = CC_ROOT_PACKAGES_DIR + '/index/' + package['name'][0] + '/' + package['name'] + '/' + package['version'] + '.json'
        if os.path.exists(package_file):
            print_package(json.load(open(package_file)))


def remove_package(package_name,version):
    print("Remove package ["+package_name+"@"+version+"]")


def reset_package(package_name):
    print("Rest package ["+package_name+"]")

