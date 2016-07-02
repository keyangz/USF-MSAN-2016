from filter import *

def laplace(data):
    return data[1] + data[3] + data[5] + data[7] - 4 * data[4]

def minus(A, B):
    copyOfA = A.copy()
    width, height = A.size
    mat1 = copyOfA.load()
    mat2 = A.load()
    mat3 = B.load()
    for x in range(width):
        for y in range(height):
            mat1[x, y] = mat2[x, y] - mat3[x, y]
    return copyOfA


img = open(sys.argv)
img.show()
edges = filter(img, laplace)
sharp = minus(img, edges)
sharp.show()