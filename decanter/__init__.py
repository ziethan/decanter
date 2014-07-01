#!/usr/bin/env python
from __future__ import absolute_import, print_function

import sys
import argparse
from ConfigParser import ConfigParser
from pkg_resources import Requirement, resource_filename

config_filename = resource_filename(Requirement.parse("decanter"), "config/config")
config = ConfigParser()
config.readfp(open(config_filename))

from decanter.install import Install, InstallFromFile
from decanter.register import Register
from decanter.add import Add
from decanter.remove import Remove


commands = ['install', 'uninstall', 'add', 'remove', 'register']

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands', help='Select an operation')

parse_install = subparsers.add_parser('install', help='Install a component')
install_group = parse_install.add_argument_group('install packages')
install_group.set_defaults(func=Install)
install_group.add_argument('-p', '--package', help='Name of the package you would like to install')
install_group.add_argument('-v', '--version', help='Package version (default=latest)')
install_group.add_argument('-f', '--package-file', help='Package file path (default=current working directory)')

parse_register = subparsers.add_parser('register', help='Sign up for read/write access to the Decanter registry')
register_group = parse_register.add_argument_group('register')
register_group.set_defaults(func=Register)
register_group.add_argument('-c', '--company', help='Company name helps with official package verification')

parse_add = subparsers.add_parser('add', help='Add a component to the Decanter registry')
add_group = parse_add.add_argument_group('add')
add_group.set_defaults(func=Add)
add_group.add_argument('package', help='Name of the package you would like to install')
add_group.add_argument('source', help='The url of the package. Must point to tarball')
add_group.add_argument('-v', '--version', help='Package version (default=latest)')
# add_group.add_argument('-o', '--official', help='Use if you are the package official creator')

parse_remove = subparsers.add_parser('remove', help="Remove a component from the Decanter registry")
remove_group = parse_remove.add_argument_group('remove')
remove_group.set_defaults(func=Remove)
remove_group.add_argument('package', help='Name of the package you would like to install')
remove_group.add_argument('-v', '--version', help='Package version (default=latest)')

def main():
    args = parser.parse_args()
    args.func(**vars(args))