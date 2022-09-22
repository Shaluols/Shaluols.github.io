# https://www.gaitubao.com/tools/pixel2cm.html
# this web link is used to check the relation of length and pixel
# the next seciton is the code used to adjust the photo size/pixel

import PIL
from PIL import Image

def transfer(infile, outfile):
    im = Image.open(infile)
    reim=im.resize((500, 333), PIL.Image.ANTIALIAS)

    width, height = reim.size

    left = 80
    top = 40
    right = 370
    bottom = 300

    im1 = reim.crop((left, top, right, bottom))

    im1.save(outfile, dpi=(500,500))

if __name__ == '__main__':
    infil=r"/home/sha/Pictures/image_SELFI.JPG"
    outfile=r"/home/sha/Pictures/resized_selfi.JPG"
    transfer(infil, outfile)