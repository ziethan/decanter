from __future__ import absolute_import, print_function

import argparse

from install import Install
from uninstall import Uninstall
from register import Register
from add import Add
from remove import Remove

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='commands', help='Select an operation')

parse_install = subparsers.add_parser('install', help='Install a component')
install_group = parse_install.add_argument_group('install')
install_group.set_defaults(func=Install)
install_group.add_argument('package', help='Name of the package you would like to install')
install_group.add_argument('-v', '--version', help='Package version (default=latest)')

parse_uninstall = subparsers.add_parser('uninstall', help='Uninstall a component')
uninstall_group = parse_uninstall.add_argument_group('uninstall')
uninstall_group.set_defaults(func=Uninstall)
uninstall_group.add_argument('package', help='Name of the package you would like to install')
uninstall_group.add_argument('-v','--version', help='Package version (default=latest)')

parse_register = subparsers.add_parser('register', help='Sign up for read/write access to the Decanter registry')
register_group = parse_register.add_argument_group('register')
register_group.set_defaults(func=Register)
register_group.add_argument('email', help='Email address of the account')
register_group.add_argument('password', help='You can figure this one out')
register_group.add_argument('-c', '--company', help='Company name helps with official package verification')

parse_add = subparsers.add_parser('add', help='Add a component to the Decanter registry')
add_group = parse_add.add_argument_group('add')
add_group.set_defaults(func=Add)
add_group.add_argument('email', help='Email address associated with your account')
add_group.add_argument('password', help='You can figure this one out')
add_group.add_argument('package', help='Name of the package you would like to install')
add_group.add_argument('-v', '--version', help='Package version (default=latest)')
add_group.add_argument('-o', '--official', help='Use if you are the package\'s creator')

parse_remove = subparsers.add_parser('remove', help="Remove a component from the Decanter registry")
remove_group = parse_remove.add_argument_group('remove')
remove_group.set_defaults(func=Remove)
remove_group.add_argument('email', help='Email address associated with your account')
remove_group.add_argument('password', help='You can figure this one out')
remove_group.add_argument('package', help='Name of the package you would like to install')
remove_group.add_argument('-v', '--version', help='Package version (default=latest)')

args = parser.parse_args()
print(vars(args))
args.func(**vars(args))