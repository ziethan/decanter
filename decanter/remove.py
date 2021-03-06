from __future__ import absolute_import, print_function

import requests
import json
import getpass

from decanter import config


def Remove(package, **kwargs):
    email = raw_input('Email: ')
    password = getpass.getpass('Password:')
    print('Removing package {0} from registry'.format(package))
    
    if kwargs.get('version') is None:
        kwargs['version'] = 'latest'
    
    package = json.dumps({
        'username': email,
        'password': password,
        'package_name': package,
        'package_version': kwargs['version']
    })
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.delete('{0}/api/remove'.format(config.get('defaults', 'registry_server')), data=package, headers=headers)
    print(json.loads(r.text).get('result').get('message'))