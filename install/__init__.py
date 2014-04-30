from __future__ import absolute_import, print_function

import requests

def Install(package, version='latest', **kwargs):
    print('Installing {0} {1}'.format(package, version))