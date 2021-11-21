from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time


def breseham(x1, y1, x2, y2, z):
    dx = abs(x2 - x1)
    dy = int(abs(y2 - y1))
    x, y = x1, y1 
    try:
        inclinacao = dy/float(dx)
        if inclinacao > 1:
            dx, dy = dy, dx
            x, y = y, x
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        p = 2 * dy - dx
        coords =[[x,y]]
        for k in range(dx):
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2*(dy - dx)
            else:
                p = p + 2*dy

            x = x + 1 if x < x2 else x - 1
            coords.append([x,y])
    except:
        inclinacao = dx/float(dy)
        if inclinacao > 1:
            dx, dy = dy, dx
            x, y = y, x
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        p = 2 * dx - dy
        coords =[[x,y]]
        for k in range(dy):
            if p > 0:
                x = x + 1 if x < x2 else x - 1
                p = p + 2*(dx - dy)
            else:
                p = p + 2*dx
            y = y + 1 if y < y2 else y - 1
            coords.append([x,y])

    for i,j in coords:
        glVertex3f(i, j, z)
