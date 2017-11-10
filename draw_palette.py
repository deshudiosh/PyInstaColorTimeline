import os
from functools import partial
from multiprocessing.pool import Pool
from pathlib import Path

import more_itertools
from PIL import Image, ImageDraw
from colorthief import ColorThief


#TODO: use 'center fill' html equivalent
def _resize_fill(img: Image) -> Image:
    pass


def _make_row(username: str, width: int, img_per_row: int, image_samples: int, row_items: list):

    row_num = row_items.pop()
    size = int(width / (img_per_row + 1))

    out_img = Image.new('RGB', (width, size), color='white')
    draw = ImageDraw.Draw(out_img)

    i = 0

    for idx, path in enumerate(row_items):
        resized = Image.open(path).resize((size, size), Image.ANTIALIAS)
        out_img.paste(resized, box=(size * idx, 0))

        rect_h = size / image_samples / img_per_row

        for color in ColorThief(path).get_palette(color_count=image_samples):
            sx = size * img_per_row
            ex = width
            sy = rect_h * i
            ey = sy + rect_h
            draw.rectangle([sx, sy, ex, ey], fill=color)
            i += 1

    path = './users/{}/rows/'.format(username)
    Path(path).mkdir(exist_ok=True)
    out_img.save((path + '{}.jpg'.format(row_num)))
    out_img.close()


def make_rows(username: str, width: int = 600, img_per_row: int = 3, image_samples: int = 3):
    # TODO: read filenames from json
    # TODO: sort by date

    path = "./users/{}/".format(username)
    img_paths = [path + s for s in os.listdir(path) if str(s).endswith('.jpg')]
    rows = list(more_itertools.chunked(img_paths, img_per_row))

    # put row_index into row_list as last item for later popping in mapped function
    for idx, row in enumerate(rows):
        row.append(idx)

    pool = Pool()
    func = partial(_make_row, username, width, img_per_row, image_samples)
    pool.map(func, rows)


def whole_from_rows(username: str):
    path = './users/{}/rows/'.format(username)
    # Path(path).mkdir(exist_ok=True)

    img_paths = [s[:-4] for s in os.listdir(path) if str(s).endswith('.jpg')]  # collect
    img_paths = sorted(img_paths, key=int)  # sort
    img_paths = [path + s + '.jpg' for s in img_paths]  # 'pathize'

    images = list(map(Image.open, img_paths))
    widths, heights = zip(*(i.size for i in images))

    total_height = sum(heights)
    max_width = max(widths)

    out_img = Image.new('RGB', (max_width, total_height))

    y_offset = 0
    for img in images:
        out_img.paste(img, box=(0, y_offset))
        y_offset += img.size[1]

    out_img.save('./users/{}.jpg'.format(username))

