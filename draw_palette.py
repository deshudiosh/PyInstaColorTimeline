import os
from typing import Sequence

import more_itertools
from PIL import Image, ImageDraw
from colorthief import ColorThief


def get_rows(username: str, width: int = 600, img_per_row: int = 3, image_samples: int = 3):
    # TODO: read filenames from json
    # TODO: sort by date
    path = "./users/{}/".format(username)
    img_paths = [path + s for s in os.listdir(path) if str(s).endswith('.jpg')]  # type: Sequence[str]

    size = int(width / (img_per_row + 1))
    rows = more_itertools.chunked(img_paths, img_per_row)
    palettes = []

    for row in rows:
        out_img = Image.new('RGB', (width, size), color='white')
        draw = ImageDraw.Draw(out_img)

        i = 0

        for idx, path in enumerate(row):
            resized = Image.open(path).resize((size-1, size))
            out_img.paste(resized, box=(size*idx, 0))

            rect_h = size/image_samples/img_per_row

            for color in ColorThief(path).get_palette(image_samples):
                sx = size*img_per_row
                ex = width
                sy = rect_h*i
                ey = sy + rect_h
                draw.rectangle([sx, sy, ex, ey], fill=color)
                i += 1

        palettes.append(out_img)
        # yield out_img

    return palettes

def get_whole(username:str, width: int = 600, img_per_row: int = 3, image_samples: int = 3):
    rows = get_rows(username, width, img_per_row, image_samples)
    row_height = int(width / (img_per_row + 1))
    total_height = row_height * len(rows)

    palette = Image.new('RGB', (width, total_height))

    for i, row in enumerate(rows):
        palette.paste(row, box=(0, row_height*i))

    palette.save('./users/{}.jpg'.format(username))
    # palette.show()






