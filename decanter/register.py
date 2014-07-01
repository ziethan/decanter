from __future__ import absolute_import, print_function

import requests
import json
import getpass

from decanter import config


def Register(**kwargs):
    email = raw_input('Email: ')
    password = getpass.getpass('Password:')
    confirm_password = getpass.getpass('Confirm:')
    
    if password != confirm_password:
        print('Password did not match')
        return False
    
    user = json.dumps({
        'username': email,
        'password': password,
        'company': kwargs.get('company')
    })
    headers = {'Content-Type': 'application/json'}
    r = requests.post('{0}/api/register'.format(config.get('defaults', 'registry_server')), data=user, headers=headers)
    print(json.loads(r.text).get('result').get('message'))