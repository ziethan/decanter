from __future__ import absolute_import, print_function, unicode_literals

import requests
import json
import getpass

from app import config

def Add(email, package, source, **kwargs):
    password = getpass.getpass('Password:')
    print('Adding package {0} to registry'.format(package, kwargs.get('version')))
    
    if kwargs.get('version') is None:
        kwargs['version'] = 'latest'
    
    package = json.dumps({
        'username': email,
        'password': password,
        'package_name': package,
        'package_url': source,
        'package_version': kwargs['version']
    })
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post('{0}/api/add'.format(config.get('defaults', 'registry_server')), data=package, headers=headers)
    print(json.loads(r.text).get('result').get('message'))