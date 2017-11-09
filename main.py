import os

import draw_palette
import get_images


user = ['design.travel.cats',
        'deshudiosh',
        'lofot.love',
        'tworczywo',
         'matowe_spojrzenie'][0]


# get_images.by_username(user)
# get_images.by_username_external(user)


# draw_palette.get_rows('design.travel.cats')
draw_palette.get_whole(user, 600, 2, 4)


# def draw_color_for_img(file_name, color):
#     image = Image.new("RGB", (100, 100), color).save(file_name)

# for file_id in itertools.chain.from_iterable(weeks.values()):
#     ct = ColorThief('{}/{}.jpg'.format(user_folder, file_id))
#     draw_color_for_img('{}/_{}.jpg'.format(user_folder, file_id), ct.get_color())