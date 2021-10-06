import math

from OpenGL.GL import glMultMatrixf

def scale(x, y, z):
    matrix = [
        [x,     0,      0,      0],
        [0,     y,      0,      0],
        [0,     0,      z,      0],
        [0,     0,      0,      1],
    ]

    glMultMatrixf(matrix)


def translate(x, y, z):
    matrix = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, z, 1],
    ] 

    glMultMatrixf(matrix)

def rotate(angle, x, y, z):
    translate(x, y, z)

    angleRadians = math.radians(angle)
    cos = math.cos(angleRadians)
    sin = math.sin(angleRadians)

    if x:
        matrix = [
            [1,   0,    0,     0],
            [0,   cos,  -sin,  0],
            [0,   sin,  cos,   0],
            [0,   0,    0,     1],
        ]
    elif y:
        matrix = [
            [cos,  0,   sin,  0],
            [0,    1,   0,    0],
            [-sin, 0,   cos,  0],
            [0,    0,   0,    1],
        ]
    elif z:
        matrix = [
            [cos,  sin,  0,   0],
            [-sin, cos,  0,   0],
            [0,    0,    1,   0],
            [0,    0,    0,   1],
        ]
    else:
        return print('Axis was not selected')

    glMultMatrixf(matrix)
    #translate(-x, -y, -z)