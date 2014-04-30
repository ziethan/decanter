from __future__ import absolute_import, print_function

import requests

def Remove(package, version='latest', **kwargs):
    print('Removing {0} {1} from registry.'.format(package, version))