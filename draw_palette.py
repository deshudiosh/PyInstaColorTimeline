from typing import Sequence

from PIL import Image, ImageDraw
from colorthief import ColorThief


def from_three(images: Sequence[str], width: int = 600):
    '''
    get three images
    get dominant color per image
    merge images into one image
    add rect per image
    '''
    size = int(width / 4)

    thumbnails = []

    for img_str in images:
        i = Image.open(img_str)  # type: Image.Image
        i = i.resize((size, size))
        thumbnails.append(i)

    out_img = Image.new('RGB', (width, size))
    out_img.paste(thumbnails[0])
    out_img.paste(thumbnails[1], box=(size, 0))
    out_img.paste(thumbnails[2], box=(size*2, 0))

    draw = ImageDraw.Draw(out_img)
    draw.rectangle([size*3, 0, size*4, size/3], fill=ColorThief(images[0]).get_color())
    draw.rectangle([size*3, size/3, size*4, size/1.5], fill=ColorThief(images[1]).get_color())
    draw.rectangle([size*3, size/1.5, size*4, size], fill=ColorThief(images[2]).get_color())


    out_img.show()


