import draw_palette
import get_images

# get_images.by_username('design.travel.cats')
# get_images.by_username('deshudiosh')


draw_palette.from_three(['./users/design.travel.cats/1635766188137953828.jpg',
                         './users/design.travel.cats/1635679082459734240.jpg',
                         './users/design.travel.cats/1636339812603496167.jpg'],
                        width=1000)

# draw_palette.get_rows - list of images (for scrollable ui drawing)
# draw_palette.get_whole(per_row=3, ommit_modulo=True)



# def draw_color_for_img(file_name, color):
#     image = Image.new("RGB", (100, 100), color).save(file_name)

# for file_id in itertools.chain.from_iterable(weeks.values()):
#     ct = ColorThief('{}/{}.jpg'.format(user_folder, file_id))
#     draw_color_for_img('{}/_{}.jpg'.format(user_folder, file_id), ct.get_color())