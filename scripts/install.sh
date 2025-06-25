#!/bin/bash

# This file is used to install necessary software and set some default programs
#
# All files are run in the user directory
# First, check if the user's computer is running Linux or macOS
# Then check if brew or apt-get and git are installed
# If not, install brew or apt-get and git
# The core software is python3 and python3 rich

INSTALL_DIR=$HOME/.ccroot
TOOL_DIR=$(dirname $(realpath $0))
host_os=$(uname -s)
force_install=false
remove=false

while [ "$1" != "" ]; do
    case $1 in
        -f | --force )
        force_install=true
        ;;
    esac
    shift
done


check_command() {
    name=$1
    if [ -x "$(command -v "$name")" ]; then
        echo "$name is already installed."
    else
        if [ -x "$(command -v apt)" ]; then
            sudo apt install "$name"
        elif [ -x "$(command -v brew)" ]; then
            brew install "$name"
        else
            echo "apt-get and brew not found, please install apt-get or brew first"
        fi
    fi
}

check_command "python3"
check_command "git"

# check if the user has installed the necessary software in [python3, git, rich]

if [ -x "$(command -v python3)" ] && [ -x "$(command -v git)" ]; then
    echo "All necessary software is installed."
else
    echo "Please install the necessary software first."
    exit 1
fi

# now export ccroot bin path to path environment & try to add export path to .bashrc or .zshrc
# the ccrpot bin path is the path of the bin directory in current file's directory

script_path=$(dirname "$0")
ccroot_path=$(cd "$script_path" && cd .. && pwd)
ccroot_bin_path="$ccroot_path/bin"

if [ -d "$ccroot_bin_path" ]; then
  if [ -f ~/.bashrc ]; then
    echo "export PATH=$ccroot_bin_path:\$PATH" >>~/.bashrc
  elif [ -f ~/.zshrc ]; then
    echo "export PATH=$ccroot_bin_path:\$PATH" >>~/.zshrc
  elif [ -f ~/.bash_profile ]; then
    echo "export PATH=$ccroot_bin_path:\$PATH" >>~/.bash_profile
  elif [ -f ~/.profile ]; then
    echo "export PATH=$ccroot_bin_path:\$PATH" >>~/.profile
  elif [ -f ~/.zprofile ]; then
    echo "export PATH=$ccroot_bin_path:\$PATH" >>~/.zprofile
  fi
fi



