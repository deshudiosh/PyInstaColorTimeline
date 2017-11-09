import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.request import urlretrieve

from instagram_scraper import InstagramScraper
import requests


def by_username(user_name):
    user_folder = Path('./users/{}/'.format(user_name))
    user_folder.mkdir(parents=True, exist_ok=True)

    url = 'https://www.instagram.com/{}/?__a=1'.format(user_name)
    r = requests.get(url)
    data = json.loads(r.text)
    nodes = data['user']['media']['nodes']

    weeks = defaultdict(list)

    for node in nodes:
        urlretrieve(node['display_src'], '{}/{}.jpg'.format(user_folder, node['id']))

        week = datetime.utcfromtimestamp(node['date']).strftime("%W")
        weeks[week].append(node['id'])

    with open(('{}/info.json'.format(user_folder)), 'w') as f:
        json.dump(weeks, f, indent=4, sort_keys=True)


# def by_username_external(username: str):
#     default_attr = dict(username='', usernames=[], filename=None,
#                         login_user=None, login_pass=None, login_only=False,
#                         destination='./', retain_username=False,
#                         quiet=False, maximum=0, media_metadata=False, latest=False,
#                         media_types=['image', 'video', 'story'], tag=False, location=False,
#                         search_location=False, comments=False, verbose=0, include_location=False, filter=None)
#
#     default_attr['username'] = username
#
#     user_folder = Path('./users/{}/'.format(username))
#     user_folder.mkdir(parents=True, exist_ok=True)
#     default_attr['destination'] = user_folder
#
#     scraper = InstagramScraper(**default_attr)
#     scraper.scrape()


