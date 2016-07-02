import sys
from PIL import Image

def region3x3(image, x, y):
    NW = getpixel(image, x - 1, y - 1)
    N = getpixel(image, x, y - 1)
    NE = getpixel(image, x + 1, y - 1)
    W = getpixel(image, x - 1, y)
    me = getpixel(image, x, y)
    E = getpixel(image, x + 1, y)
    SW = getpixel(image, x - 1, y + 1)
    S = getpixel(image, x, y + 1)
    SE = getpixel(image, x + 1, y + 1)
    return [NW, N, NE, W, me, E, SW, S, SE]

def getpixel(image, x, y):
    width, height = image.size
    if x < 0:
        x = 0
    elif x >= width:
        x = width - 1

    if y < 0:
        y = 0
    elif y >= height:
        y = height - 1
    pixels = image.load()
    return pixels[x, y]

def open(argv):
    if len(argv) <= 1:
        print "missing image filename"
        sys.exit(1)
    img = Image.open(argv[1])
    img = img.convert("L")
    return img

def filter(img, f):
    width, height = img.size
    imgcopy = img.copy()
    pixels = imgcopy.load()
    for x in range(width):
        for y in range(height):
            r = region3x3(img, x, y)
            pixels[x, y] = f(r)
    return imgcopy