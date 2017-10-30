import itertools
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.request import urlretrieve

import requests
from PIL import Image
from colorthief import ColorThief


def draw_color_for_img(file_name, color):
    image = Image.new("RGB", (100, 100), color).save(file_name)


def get_images(user_name):
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

    for file_id in itertools.chain.from_iterable(weeks.values()):
        ct = ColorThief('{}/{}.jpg'.format(user_folder, file_id))
        draw_color_for_img('{}/_{}.jpg'.format(user_folder, file_id), ct.get_color())


get_images('design.travel.cats')
get_images('deshudiosh')

