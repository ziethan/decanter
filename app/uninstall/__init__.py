from __future__ import absolute_import, print_function

import requests

def Uninstall(package, version='latest', **kwargs):
    print('Uninstalling {0} {1}.'.format(package, version))