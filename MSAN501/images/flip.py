import sys
from PIL import Image

def flip(img):
    width, height = img.size
    imgcopy = img.copy()
    mat1 = img.load()
    mat2 = imgcopy.load()
    for i in range(height):
        for j in range(width):
            mat2[j, i] = mat1[width - j - 1, i]
    return imgcopy


if len(sys.argv) <= 1:
    print "missing image filename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

flipimage = flip(img)

flipimage.show()