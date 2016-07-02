from filter import *

def laplace(data):
    return data[1] + data[3] + data[5] + data[7] - 4 * data[4]

img = open(sys.argv)
img.show()
edges = filter(img, laplace)
edges.show()