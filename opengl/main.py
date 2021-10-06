from OpenGL.GL import *
from OpenGL.GLUT import *

from perspectives import *
from transformations import *
from forms import *

WINDOW_HEIGHT = Constant('WINDOW_HEIGHT', 600)
WINDOW_WIDTH = Constant('WINDOW_WIDTH', 800)


KEY_W = 115
KEY_A = 97
KEY_S = 119
KEY_D = 100
KEY_Q = 113
KEY_E = 101
KEY_ESC = 27

TRANSLATION = {
    'x': 0,
    'y': 0,
    'z': 0
}

ROTATION = {
    'angle': 0,
    'x': 0,
    'y': 1,
    'z': 0
}



def keyboard(key, x, y):
    key = key[0]

    if (key == KEY_ESC):
        glutDestroyWindow(glutGetWindow())

    if (key == KEY_W):
        TRANSLATION['z'] += -0.5
    elif (key == KEY_S):
        TRANSLATION['z'] += 0.5

    if (key == KEY_A):
        TRANSLATION['x'] += 0.5
    elif (key == KEY_D):
        TRANSLATION['x'] += -0.5

    if (key == KEY_Q):
        ROTATION['angle'] += 10
        ROTATION['x'] = 0
        ROTATION['y'] = 1
        ROTATION['z'] = 0

    if (key == KEY_E):
        ROTATION['angle'] -= 10
        ROTATION['x'] = 0
        ROTATION['y'] = 1
        ROTATION['z'] = 0


def mouse(button, state, x, y):
    if (button == GLUT_RIGHT_BUTTON):
        ROTATION['angle'] += 5
        ROTATION['x'] = 1
        ROTATION['y'] = 0
        ROTATION['z'] = 0
    if (button == GLUT_LEFT_BUTTON):
        ROTATION['angle'] -= 5
        ROTATION['x'] = 1
        ROTATION['y'] = 0
        ROTATION['z'] = 0

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -5)

    glShadeModel(GL_SMOOTH)

    glPushMatrix()

    # glTranslatef(TRANSLATION['x'], TRANSLATION['y'], TRANSLATION['z'])
    translate(TRANSLATION['x'], TRANSLATION['y'], TRANSLATION['z'])
    # glRotatef(ROTATION['angle'], 0, 1, 0)
    rotate(ROTATION['angle'], ROTATION['x'], ROTATION['y'], ROTATION['z'])
    # glScalef(1, 4, 1)
    # scale(1, 4, 1)

    #for cont in range(8):
    #    for x in range(4):
    #        for z in range (2):
    #            Chair(x*10,0,z*10)
    #mesa_foot(0,0,0)
    altura = 5
    comprimento = 10
    largura = 20

    Chair(0,2.6-altura,-comprimento)
    Chair(5,2.6-altura,-comprimento)
    Chair(-5,2.6-altura,-comprimento)
    glPushMatrix();
    glRotatef(180, 0, 1, 0);
    Chair(0,2.6-altura,-comprimento)
    Chair(5,2.6-altura,-comprimento)
    Chair(-5,2.6-altura,-comprimento)
    glPopMatrix();
    Mesa(0, 0, 0, largura, comprimento, altura)
    #CubeGlut()
    #Cube(1, 0, 0)
    #Cube(-4, 0, 0)
    #Triangle()    

    glPopMatrix()

    glFlush()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # glOrtho(-1, 1, -1, 1, 1.0, 50)
    # ortho(-1, 1, -1, 1, 1.0, 50)

    # glFrustum(-1, 1, -1, 1, 1.0, 50)
    frustum(-1, 1, -1, 1, 1.0, 500)

    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()

    glutInitDisplayMode(GLUT_DEPTH | GLUT_RGBA)
    glutInitWindowPosition(200, 200)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    WINDOW = glutCreateWindow("RU ON OPENGL")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)

    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)

    glutMainLoop()

main()
