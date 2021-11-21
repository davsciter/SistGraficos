import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL import glMultMatrixf

#pos_luz = [20, 5, -3, 1]
pos_luz = [20, 8, -5, 1]

def renderLight():
	glEnable(GL_LIGHT0)
	glEnable(GL_LIGHTING)

	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
	
	glShadeModel(GL_SMOOTH)
	
	glEnable(GL_COLOR_MATERIAL)
	glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
	glEnable(GL_TEXTURE_2D)
	specReflection = [1.0, 1.0, 1.0, 1.0]
	glMaterialfv(GL_FRONT, GL_SPECULAR, specReflection)
	glMateriali(GL_FRONT, GL_SHININESS, 30)
	glLightfv(GL_LIGHT0, GL_POSITION, pos_luz)
    

def Point():
    glPointSize(10)

    glBegin(GL_POINTS)
    glColor(1,1,1)
    glVertex3f(pos_luz[0], pos_luz[1], pos_luz[2])
    glEnd()


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
