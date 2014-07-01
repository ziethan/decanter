from __future__ import absolute_import, print_function

import tarfile
import json
import yaml
import os
import errno
import requests
import xml.etree.ElementTree as ET
from  xml.etree.ElementTree import ParseError

from decanter import config


def InstallFromFile(**kwargs):
    if kwargs.get('path') is None:
        exts = ['package.json', 'package.yaml', 'package.yml', 'package.xml']
        for x in exts:
            result = file_check(x)
            if result is not None:
                break
    else:
        result = kwargs.get('path')
    
    try:
        f = open(result, 'r')
    except TypeError, IOError:
        f = None

    if f is None:
        print('No package file provided')
        return False

    if result.endswith('.json'):
        data = json.loads(f.read())
    elif result.endswith('.yaml') or result.endswith('.yml'):
        data = yaml.load(f.read())
    else:
        try:
            package = ET.fromstring(f.read())
            data = {}
            for i in range(0, package.__len__()):
                data[package.findall('package')[i].get('name')] = package.findall('package')[i].get('version')
        except ParseError:
            print('Error parsing XML package file')
            return False
        
    if not os.path.exists('components') or not os.path.isdir('components'):
        mkdir('components')
    
    if data is None:
        print('No data in package file')
        return False
    
    for x in data:
        get_package(x, data[x])
    

def Install(**kwargs):
    if kwargs.get('package') is None:
        InstallFromFile(**kwargs)
        return False
    if kwargs.get('version') is None:
        Warning('Using latest version.')
        kwargs['version'] = 'latest'
    
    if os.path.exists('components') and os.path.isdir('components'):
        get_package(kwargs['package'], kwargs['version'])
    else:
        mkdir('components')
        get_package(kwargs['package'], kwargs['version'])

def file_check(f):
    try:
        open(f, 'r')
        return f
    except IOError:
        return None
    
def mkdir(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def get_package(package, version):
    p_data = json.dumps({'package': package, 'version': version})
    headers = {'Content-Type': 'application/json'}
    r = requests.get('{0}/api/package'.format(config.get('defaults', 'registry_server')), data=p_data, headers=headers)
    
    response = json.loads(r.text)
    if r.status_code != 200:
        print(response['error'], '::: {0} {1}'.format(package, version))
        return False
    
    url = response['result']['data']['package']['url']
    
    if os.path.exists('/tmp/decanter') and os.path.isdir('/tmp/decanter'):
        tarball = download_package(url, package, version)
    else:
        mkdir('/tmp/decanter')
        tarball = download_package(url, package, version)
    
    if not tarball:
        return False
    
    t = tarfile.open('/tmp/decanter/{0}-{1}.tar.gz'.format(package, version))
    t.extractall(path="components")
    t.close()
    
def download_package(url, package, version):
    with open('/tmp/decanter/{0}-{1}.tar.gz'.format(package, version), 'wb') as handle:
        response = requests.get(url, stream=True)
        
        if not response.ok:
            print('Failed to get package ::: {0} {1}'.format(package, version))
            return False
            
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
        
        return True
    
#     print('else if package exists but not the right version')
#     print('warn that the supplied version does not exist')
#     print('install latest package')
#     print('else if package does not exist at all')
#     print('raise exception saying package does not exist')