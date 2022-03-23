from io import BytesIO
import json
import os
import re
import shutil
import sys
from zipfile import ZipFile
import urllib3

project_url = 'https://gitlab.com/Jabbah/open-composite-acc'
api_url = 'https://gitlab.com/api/v4/projects/32868264/releases/'

if os.path.exists('tmp'):
    shutil.rmtree('tmp')

http = urllib3.PoolManager()

response = http.request('GET', api_url)
parsed_response = json.loads(response.data)
latest_release = parsed_response[0]

tag_name = latest_release['tag_name']
description = latest_release['description']

version = re.search('(?P<version>[0-9\.]+)', tag_name).group('version')
asset_url = re.search('\(\/(?P<url>uploads\/[A-Za-z0-9\/_\.]+)\)', description).group('url')

file_response = http.request('GET', f'{project_url}/{asset_url}')
zipfile = ZipFile(BytesIO(file_response.data))
zipfile.extractall('tmp/')

item_name = 'OCXR_WMR_ACC'
versioned_item_name = f'{item_name}_{tag_name}'
source_dir = f'tmp/{item_name}'
target_dir = f'{source_dir}/bin'

for dirname, dirnames, filenames in os.walk(source_dir):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    if dirname == source_dir:
        for filename in filenames:
            shutil.move(os.path.join(dirname, filename), target_dir)
        continue

    relative = os.path.relpath(dirname,source_dir)
    if relative == 'D3DCompiler_47':
        for filename in filenames:
            shutil.move(os.path.join(dirname, filename), target_dir)
        os.rmdir(dirname)
        continue

    new_dir = os.path.join(target_dir, relative)
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    for filename in filenames:
        shutil.move(os.path.join(dirname, filename), os.path.join(new_dir, filename))

    os.rmdir(dirname)

version_file = os.path.join('tmp', 'VERSION.txt')

with open(version_file, 'w') as v:
    v.write(version)

versioned_dir = f'{source_dir}_{tag_name}'
shutil.move(source_dir, versioned_dir)

print(versioned_item_name)
print(tag_name)
