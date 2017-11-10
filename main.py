import os

import draw_palette
import get_images
import timing


def main():
    user = ['design.travel.cats',
            'deshudiosh',
            'lofot.love',
            'tworczywo',
            'matowe_spojrzenie'][0]

    timing.init()

    # get_images.by_username(user)

    # draw_palette.make_rows(user, 1200, 9, 3)

    draw_palette.whole_from_rows(user)


if __name__ == '__main__':
    main()
