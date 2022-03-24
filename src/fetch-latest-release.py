import json
import re
import urllib3
from urllib.parse import urljoin

project_url = 'https://gitlab.com/Jabbah/open-composite-acc/'
api_url = 'https://gitlab.com/api/v4/projects/32868264/releases/'

http = urllib3.PoolManager()
response = http.request('GET', api_url)
parsed_response = json.loads(response.data)

latest_release = parsed_response[0]
tag_name = latest_release['tag_name']
description = latest_release['description']

version = re.search('(?P<version>[0-9\.]+)', tag_name).group('version')
asset_url = re.search('\(\/(?P<url>uploads\/[A-Za-z0-9\/_\.]+)\)', description).group('url')

release_asset_url = urljoin(project_url, asset_url)

print(tag_name)
print(version)
print(release_asset_url)