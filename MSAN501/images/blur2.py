from filter import *

def avg(data):
    return sum(data) / len(data)

img = open(sys.argv)
img.show()
img = filter(img, avg)
img.show()
