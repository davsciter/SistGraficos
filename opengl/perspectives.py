import numpy as np

from OpenGL.GL import glMultMatrixf, glLoadIdentity

# https://lmb.informatik.uni-freiburg.de/people/reisert/opengl/doc/glFrustum.html
def frustum(left, right, bottom, top, near, far):
    glLoadIdentity()

    A = (right + left)/(right - left)
    B = (top + bottom)/(top - bottom)
    C = -(far + near)/(far - near)
    D = -(2 * far * near)/(far - near)

    rightLeft = (2 * near)/(right - left)
    topBottom = (2 * near)/(top - bottom)

    matrix = [
        [rightLeft, 0, A, 0],
        [0, topBottom, B, 0],
        [0, 0, C, D],
        [0, 0, -1, 0],
    ]

    matrix = np.transpose(matrix)

    glMultMatrixf(matrix)

def ortho(left, right, bottom, top, near, far):
    glLoadIdentity()

    tx = (right + left)/(right - left)
    ty = (top + bottom)/(top - bottom)
    tz = (far + near)/(far - near)

    rightLeft = 2/(right - left)
    topBottom = 2/(top - bottom)
    farNear = 2/(far - near)

    matrix = [
        [rightLeft, 0, 0, tx],
        [0, topBottom, 0, ty],
        [0, 0, farNear, tz],
        [0, 0, 0, 1],
    ]

    matrix = np.transpose(matrix)

    glMultMatrixf(matrix)
