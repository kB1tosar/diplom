import os
import math
from PIL import Image
from django.conf import settings


# source path
def tile_work(uploaded_image, tiles_name):
    img_path = uploaded_image

    # tile size
    tile_size = 128

    # tile directory
    tile_path = tiles_name

    def adjust_bounds(src_img):
        # get size of original image
        src_width, src_height = src_img.size

        # calculate size of target image (background)
        target_width = src_width + (tile_size - src_width % tile_size)
        target_height = src_height + (tile_size - src_height % tile_size)

        # create transparent background
        target_img = Image.new('RGBA', (target_width, target_height))

        # combine original image and background
        target_img.paste(src_img, (0, 0))

        return target_img

    img = Image.open(img_path)
    w, h = img.size[0], img.size[1]

    # calculate max zoom level
    max_zoom = int(math.ceil(math.log((max(w, h) / tile_size), 2)))
    for z in range(max_zoom, -1, -1):

        adjusted_image = adjust_bounds(img)

        numcolumns = adjusted_image.size[0] / tile_size
        numrows = adjusted_image.size[1] / tile_size

        for x in range(int(numcolumns)):

            # create z/x/ directory
            path = os.path.join(
                settings.MEDIA_ROOT,
                'Image/Maps',
                tile_path,
                str(z),
                str(x)
            )
            if not os.path.isdir(path):
                os.makedirs(path)

            for y in range(int(numrows)):
                bounds = (x * tile_size, y * tile_size, (x + 1) * tile_size,
                          (y + 1) * tile_size)
                tile = adjusted_image.crop(bounds)
                tile.save('%s/%s.png' % (path, y))

        w, h = img.size[0], img.size[1]
        img = img.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)
