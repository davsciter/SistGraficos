from OpenGL.GL import *
from OpenGL.GLUT import *
from PIL.Image import ROTATE_180, ROTATE_90
from numpy import matrix
from tkinter import messagebox

from perspectives import *
from transformations import *
from forms import *
from lighting import *
from breseham import *

WINDOW_HEIGHT = Constant('WINDOW_HEIGHT', 600)
WINDOW_WIDTH = Constant('WINDOW_WIDTH', 800)


KEY_W = 115
KEY_A = 97
KEY_S = 119
KEY_D = 100
KEY_Q = 101
KEY_E = 113
WHEEL_UP = 3
WHEEL_DOWN = 4
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
        TRANSLATION['z'] -= -0.5
    elif (key == KEY_S):
        TRANSLATION['z'] -= 0.5

    if (key == KEY_A):
        TRANSLATION['x'] -= 0.5
    elif (key == KEY_D):
        TRANSLATION['x'] -= -0.5

    if (key == KEY_Q):
        ROTATION['angle'] += 5
        ROTATION['x'] = 0
        ROTATION['y'] = 1
        ROTATION['z'] = 0

    if (key == KEY_E):
        ROTATION['angle'] -= 5
        ROTATION['x'] = 0
        ROTATION['y'] = 1
        ROTATION['z'] = 0


def SpecialKeys(key, x, y):
    if (key == GLUT_KEY_UP):
        TRANSLATION['z'] -= 0.5
    elif (key == GLUT_KEY_DOWN):
        TRANSLATION['z'] += 0.5

    if (key == GLUT_KEY_RIGHT):
        TRANSLATION['x'] -= 0.5
    elif (key == GLUT_KEY_LEFT):
        TRANSLATION['x'] += 0.5

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

    if (button == WHEEL_UP):
        ROTATION['angle'] += 5
        ROTATION['x'] = 0
        ROTATION['y'] = 1
        ROTATION['z'] = 0


    if (button == WHEEL_DOWN):
        ROTATION['angle'] -= 5
        ROTATION['x'] = 0
        ROTATION['y'] = 1
        ROTATION['z'] = 0

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(5, -10, -30)
    rotate(165, 0, 1, 0)

    glShadeModel(GL_SMOOTH)

    glPushMatrix()

    # glTranslatef(TRANSLATION['x'], TRANSLATION['y'], TRANSLATION['z'])
    translate(TRANSLATION['x'], TRANSLATION['y'], TRANSLATION['z'])
    # glRotatef(ROTATION['angle'], 0, 1, 0)
    rotate(ROTATION['angle'], ROTATION['x'], ROTATION['y'], ROTATION['z'])

    altura = 5
    comprimento = 4
    largura = 10
    glPushMatrix()
    renderLight() 
    Point()
    glPopMatrix()

    Sala(0, 0.6, 0, 8)
    Chair(0,2.6-altura,-comprimento)
    Chair(5,2.6-altura,-comprimento)
    Chair(-5,2.6-altura,-comprimento)
    
    rotate(180, 0, 1, 0)
    Chair(0,1.6-altura,-comprimento)
    Chair(5,1.6-altura,-comprimento)
    Chair(-5,1.6-altura,-comprimento)
    Mesa(0, -1.6, 0, largura, comprimento, altura)
    Quadro(0, 1.85, -2, 4)
    #CubeGlut()
    #Cube(1, 0, 0)
    #Cube(-4, 0, 0)
    #Triangle()   
    rotate(90, 0, 1, 0)
    Janela(0, 1, 4, 4)
    Janela(1.1, 1, -5.3, 3)
    Porta(-0.60, 0, -2.285, 7)
 

    
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
    messagebox.showinfo(title='Controles', message='WASD / Setas (Cima, Baixo, Esquerda, Direita) para movimentar a perspectiva\n\nQ|E ou Scroll Up/Down Mouse para girar no eixo Y\n\nBotão Direito/Esquerdo Mouse para girar no eixo X')    

    glutInit()

    glutInitDisplayMode(GLUT_DEPTH | GLUT_RGBA)
    glutInitWindowPosition(200, 200)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    WINDOW = glutCreateWindow("SALA DE ESTUDOS ON OPENGL")

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutSpecialFunc(SpecialKeys)
    glutMainLoop()

main()