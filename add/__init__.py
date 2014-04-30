from __future__ import absolute_import, print_function

import requests

def Add(url, version='latest', **kwargs):
    print('Adding package {0} to registry'.format(url, version))