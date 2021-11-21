from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import ROTATE_180, ROTATE_270, ROTATE_90
from texture import *
import numpy
from breseham import *


janela = read_texture('Imgs/janela.png')


def Sala(x=0, y=0, z=0, scale=1):
    vertices = (
        ((x+2.0)*scale, (y-1.25)*scale, (z-1)*scale),
        ((x+2.0)*scale, (y+1.25)*scale, (z-1)*scale),
        ((x-2.0)*scale, (y+1.25)*scale, (z-1)*scale),
        ((x-2.0)*scale, (y-1.25)*scale, (z-1)*scale),
        ((x+2.0)*scale, (y-1.25)*scale, (z+1)*scale),
        ((x+2.0)*scale, (y+1.25)*scale, (z+1)*scale),
        ((x-2.0)*scale, (y-1.25)*scale, (z+1)*scale),
        ((x-2.0)*scale, (y+1.25)*scale, (z+1)*scale),
    )

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7),
    )
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()   



    #paredes
    paredes =[
        [[(x+2.0), (y-1.85), (z+1)],
        [(x+2.0), (y+0.65), (z+1)],
        [(x-2.0), (y+0.65), (z+1)],
        [(x-2.0), (y-1.85), (z+1)]],

        [[(x+2.0), (y+0.65), (z-1)],
        [(x+2.0), (y+0.65), (z+1)],
        [(x+2.0), (y+0.18), (z+1)],
        [(x+2.0), (y+0.18), (z-1)]],

        [[(x+2.0), (y-1.85), (z-1)],
        [(x+2.0), (y-1.85), (z+1)],
        [(x+2.0), (y-1.075), (z+1)],
        [(x+2.0), (y-1.075), (z-1)]],

        [[(x+2.0), (y+0.18), (z-1)],
        [(x+2.0), (y+0.180), (z-0.75)],
        [(x+2.0), (y-1.075), (z-0.75)],
        [(x+2.0), (y-1.075), (z-1)]],

        [[(x+2.0), (y+0.18), (z+1)],
        [(x+2.0), (y+0.18), (z+0.75)],
        [(x+2.0), (y-1.075), (z+0.75)],
        [(x+2.0), (y-1.075), (z+1)]],

        [[(x-2.0), (y+0.65), (z-1)],
        [(x-2.0), (y+0.65), (z+1)],
        [(x-2.0), (y-0.1), (z+1)],
        [(x-2.0), (y-0.1), (z-1)]],

        [[(x-2.0), (y-1.05), (z-1)],
        [(x-2.0), (y-1.05), (z+0.175)],
        [(x-2.0), (y-1.85), (z+0.175)],
        [(x-2.0), (y-1.85), (z-1)]],

        [[(x-2.0), (y+0.65), (z+1)],
        [(x-2.0), (y+0.65), (z+0.875)],
        [(x-2.0), (y-1.85), (z+0.875)],
        [(x-2.0), (y-1.85), (z+1)]],
    ]

    teto =[
        [(x+2), (y+0.65), (z-1)],
        [(x-2), (y+0.65), (z-1)],
        [(x-2), (y+0.65), (z+1)],
        [(x+2), (y+0.65), (z+1)]
    ]
    glBegin(GL_QUADS)
    for vertex in teto:
        glVertex3f((x+vertex[0])*scale, (y+vertex[1])*scale, (z+vertex[2])*scale)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.961, 0.961, 0.863)
    for parede in paredes:
        for vertex in parede:
            glVertex3f((x+vertex[0])*scale, (y+vertex[1])*scale, (z+vertex[2])*scale)
    

    glEnd()

    #chão 32x20x16 8x5x2 
    for i in range(-3,5, 2):
        for j in range(-7, 9, 2):
            piso(x+j, y-3.25, z+i)

def piso(x=0, y=0, z=0, scale=1):
    borda =[
        [(x+2.0), (y), (z+2)],
        [(x-2.0), (y), (z+2)],

        [(x-2.0), (y), (z-2)],
        [(x+2.0), (y), (z-2)],

        [(x-2.0), (y), (z+2)],
        [(x-2.0), (y), (z-2)],

        [(x+2.0), (y), (z+2)],
        [(x+2.0), (y), (z-2)],
    ]

    glLineWidth(3)
    glColor3f(1,1,1)    
    glBegin(GL_LINES)
    for vertex in borda:
        glVertex3d((x+vertex[0])*scale, (y+vertex[1])*scale, (z+vertex[2])*scale)               
    glEnd()

    azulejo =[
        [(x+1.95), (y), (z+1.95)],
        [(x-1.95), (y), (z+1.95)],
        [(x-1.95), (y), (z-1.95)],
        [(x+1.95), (y), (z-1.95)]
    ]

    glColor3f(0.753, 0.753, 0.753)   
    glBegin(GL_QUADS)
    for vertex in azulejo:
        glVertex3f((x+vertex[0])*scale, (y+vertex[1])*scale, (z+vertex[2])*scale)
    glEnd()
    return

def Janela(x=0, y=0, z=0, scale =1):
    #glEnable(GL_TEXTURE_2D)
    #glBindTexture(GL_TEXTURE_2D, janela)
    #glEnable(GL_TEXTURE_GEN_S)
    #glEnable(GL_TEXTURE_GEN_T)
    #glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_NORMAL_MAP)
    #glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_NORMAL_MAP)
    #glDisable(GL_TEXTURE_2D)
    #glutSwapBuffers()

    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(0.871, 0.722, 0.529)    
    
    #borders
    glVertex3d((x-1.5)*scale, (y-1.25)*scale, z*scale)
    glVertex3d((x+1.5)*scale, (y-1.25)*scale, z*scale)
    
    glVertex3d((x+1.5)*scale, (y+1.25)*scale, z*scale)
    glVertex3d((x-1.5)*scale, (y+1.25)*scale, z*scale) 
    
    glVertex3d((x+1.5)*scale, (y+1.25)*scale, z*scale)
    glVertex3d((x+1.5)*scale, (y-1.25)*scale, z*scale)

    glVertex3d((x-1.5)*scale, (y+1.25)*scale, z*scale)
    glVertex3d((x-1.5)*scale, (y-1.25)*scale, z*scale)  

    #verticalstrip
    glVertex3d((x)*scale, (y+1.25)*scale, z*scale)
    glVertex3d((x)*scale, (y-1.25)*scale, z*scale)   
    #horizontalstrip    
    glVertex3d((x-1.5)*scale, (y)*scale, z*scale)
    glVertex3d((x+1.5)*scale, (y)*scale, z*scale)              
    glEnd()

    #não sobrepor divisões b
    b = 0.025
    vidros =[
        [[0+b, 0+b, 0],
        [1.5-b, 0+b, 0],
        [1.5-b, 1.25-b, 0],
        [0+b, 1.25-b, 0]],

        [[0+b, -1.25+b, 0],
        [1.5-b, -1.25+b, 0],
        [1.5-b, 0-b, 0],
        [0+b, 0-b, 0]],

        [[0-b, -1.25+b, 0],
        [-1.5+b, -1.25+b, 0],
        [-1.5+b, 0-b, 0],
        [0-b, 0-b, 0]],

        [[0-b, +1.25-b, 0],
        [-1.5+b, +1.25-b, 0],
        [-1.5+b, 0+b, 0],
        [0-b, 0+b, 0]]
    ]

    #vidros
    glBegin(GL_QUADS)
    glColor3f(0.690, 0.878, 0.902)
    for vidro in vidros:
        for vertex in vidro:
            glVertex3f((x+vertex[0])*scale, (y+vertex[1])*scale, (z+vertex[2])*scale)
    glEnd()

    return

def Porta(x=0, y=0, z=0, scale =1):
    glBegin(GL_QUADS)
    #porta
    glColor3f(0.467, 0.533, 0.600)

    #front
    vertices = [
        ((x+0.4) * scale, (y+0.975) * scale, (z) * scale),
        ((x-0.4) * scale, (y+0.975) * scale, (z) * scale),
        ((x-0.4) * scale, (y-1.00) * scale, (z) * scale),
        ((x+0.4) * scale, (y-1.00) * scale, (z) * scale)
    ]

    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
    )

    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

    raio = 0.1
    pi = 3.142
    glColor3f(0.412, 0.412, 0.412)
    glBegin(GL_POLYGON)    
    for vertex in range(0, 32):
        angle  = float(vertex) * 2.0 * numpy.pi / 32
        glVertex3f((+0.25+x+numpy.cos(angle)*raio)*scale, (y+numpy.sin(angle)*raio)*scale, z*scale)
    glEnd()
    return
    
    #back
    #glVertex3f(x+0.4, y+1.05, z-0.05)
    #glVertex3f(x-0.4, y+1.05, z-0.05)
    #glVertex3f(x-0.4, y-1.05, z-0.05)
    #glVertex3f(x+0.4, y-1.05, z-0.05)
    #glEnd()
    #maçaneta
    #glColor3f(0.412, 0.412, 0.412)
    #Cube(-5.0, 1.05, 0.05, 0.05)

    
def Quadro(x=0, y=0, z=0, scale = 1):
    z+=0.05
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    #inside
    glVertex3f((x-1.5)*scale, (y-1.0)*scale, z*scale)
    glVertex3f((x+1.5)*scale, (y-1.0)*scale, z*scale)
    glVertex3f((x+1.5)*scale, (y+1.0)*scale, z*scale)
    glVertex3f((x-1.5)*scale, (y+1.0)*scale, z*scale) 
    glEnd()

    #border
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(0.871, 0.722, 0.529)
    glVertex3d((x-1.5)*scale, (y-1.0)*scale, z*scale)
    glVertex3d((x+1.5)*scale, (y-1.0)*scale, z*scale)
    
    glVertex3d((x+1.5)*scale, (y+1.0)*scale, z*scale)
    glVertex3d((x-1.5)*scale, (y+1.0)*scale, z*scale) 
    
    glVertex3d((x+1.5)*scale, (y+1.0)*scale, z*scale)
    glVertex3d((x+1.5)*scale, (y-1.0)*scale, z*scale)

    glVertex3d((x-1.5)*scale, (y+1.0)*scale, z*scale)
    glVertex3d((x-1.5)*scale, (y-1.0)*scale, z*scale)                  
    glEnd()


    texto = 'Sala de Estudos - Biblioteca'
    glColor(1,1,1)
    glRasterPos2f((x-2.5)*scale,y+5*scale)
    for i in texto:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))  


    pos=[0,-8, 10]
    devs = ['Davi Sena - 118314', 'Nicolas Bortoluzzi - 126659', 'Vinícius Oliveira - 129921']
    glColor(0, 0, 0)

    for j in devs:
        glRasterPos3f(pos[0], pos[1], pos[2])
        for i in j:
                glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_10, ord(i))
        pos[1]-=2
        
    glBegin(GL_POINTS)
    glColor(0,0,0)
    #C
    breseham(x-5, y+3, x-5, y+8, (z+0.05)*scale)
    breseham(x-5, y+8, x-2, y+8, (z+0.05)*scale)
    breseham(x-5, y+3, x-2, y+3, (z+0.05)*scale)

    #3
    breseham(x+5, y+3, x+5, y+8, (z+0.05)*scale)
    breseham(x+2, y+8, x+5, y+8, (z+0.05)*scale)
    breseham(x+2, y+3, x+5, y+3, (z+0.05)*scale)
    breseham(x+2, y+5.5, x+5, y+5.5, (z+0.05)*scale)

    glEnd()
    return

def mesa_foot(x, y, z, H):

    #back face
    glVertex3f(x+0.05, y, z)
    glVertex3f(x+0.05, y-H, z)
    glVertex3f(x-0.05, y-H, z)
    glVertex3f(x-0.05, y, z)

    #front face
    glVertex3f(x+0.05, y, z+0.1)
    glVertex3f(x+0.05, y-H, z+0.1)
    glVertex3f(x-0.05, y-H, z+0.1)
    glVertex3f(x-0.05, y, z+0.1)

    #right face
    glVertex3f(x+0.05, y, z+0.1)
    glVertex3f(x+0.05, y-H, z+0.1)
    glVertex3f(x+0.05, y-H, z)
    glVertex3f(x+0.05, y, z)

    #left face
    glVertex3f(x-0.05, y, z+0.1)
    glVertex3f(x-0.05, y-H, z+0.1)
    glVertex3f(x-0.05, y-H, z)
    glVertex3f(x-0.05, y, z)

    #base foot
    glVertex3f(x+0.05, y-H, z+0.1)
    glVertex3f(x+0.05, y-H, z)
    glVertex3f(x-0.05, y-H, z)
    glVertex3f(x-0.05, y-H, z+0.1)

def Mesa(x, y, z, Largura, Comprimento, Altura):
    glBegin(GL_QUADS)
    glColor3f(0.52, 0.37, 0.26)
    #top table
    glVertex3f(x+Largura, y+0.6, z-Comprimento)
    glVertex3f(x+Largura, y+0.6, z+Comprimento)
    glVertex3f(x-Largura, y+0.6, z+Comprimento)
    glVertex3f(x-Largura, y+0.6, z-Comprimento)

    #down table
    glVertex3f(x+Largura, y+0.3, z-Comprimento)
    glVertex3f(x+Largura, y+0.3, z+Comprimento)
    glVertex3f(x-Largura, y+0.3, z+Comprimento)
    glVertex3f(x-Largura, y+0.3, z-Comprimento)


    #side table front
    glVertex3f(x+Largura, y+0.3, z+Comprimento)
    glVertex3f(x+Largura, y+0.6, z+Comprimento)
    glVertex3f(x-Largura, y+0.6, z+Comprimento)
    glVertex3f(x-Largura, y+0.3, z+Comprimento)

    #side table back
    glVertex3f(x+Largura, y+0.3, z-Comprimento)
    glVertex3f(x+Largura, y+0.6, z-Comprimento)
    glVertex3f(x-Largura, y+0.6, z-Comprimento)
    glVertex3f(x-Largura, y+0.3, z-Comprimento)
    
    #side table left
    glVertex3f(x-Largura, y+0.3, z+Comprimento)
    glVertex3f(x-Largura, y+0.3, z-Comprimento)
    glVertex3f(x-Largura, y+0.6, z-Comprimento)
    glVertex3f(x-Largura, y+0.6, z+Comprimento)


    #side table right
    glVertex3f(x+Largura, y+0.3, z+Comprimento)
    glVertex3f(x+Largura, y+0.3, z-Comprimento)
    glVertex3f(x+Largura, y+0.6, z-Comprimento)
    glVertex3f(x+Largura, y+0.6, z+Comprimento)

    #desenhar os pes
    mesa_foot(x+Largura-0.05,y+0.3,z+Comprimento-0.1, Altura)
    mesa_foot(x+Largura-0.05,y+0.3,z-Comprimento, Altura)
    mesa_foot(x-Largura+0.05,y+0.3,z+Comprimento-0.1, Altura)
    mesa_foot(x-Largura+0.05,y+0.3,z-Comprimento, Altura)
    glEnd()
    return


def Chair(x, y, z):
    glBegin(GL_QUADS)

    glColor3f(0.91, 0.76, 0.65)
    
    #glNormal3f(x+0.0, y+0.0, z+1.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    
    #Right
    #glNormal3f(x+1.0, y+0.0, z+0.0)
    glVertex3f(x+2.0, y+-0.2, z+-2.0)
    glVertex3f(x+2.0, y+0.2, z+-2.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+2.0, y+-0.2, z+2.0)
    
    #Back
    #glNormal3f(x+0.0, y+0.0, z+-1.0)
    glVertex3f(x-2.0, y+-0.2, z+-2.0)
    glVertex3f(x+-2.0, y+0.2, z+-2.0)
    glVertex3f(x+2.0, y+0.2, z+-2.0)
    glVertex3f(x+2.0, y+-0.2, z+-2.0)
    
    #Left
    #glNormal3f(x+-1.0, y+0.0, z+0.0)
    glVertex3f(x+-2.0, y+-0.2, z+-2.0)
    glVertex3f(x+-2.0, y+-0.2, z+2.0)
    glVertex3f(x+-2.0, y+0.2, z+2.0)
    glVertex3f(x+-2.0, y+0.2, z+-2.0)
    
    #top
    #glNormal3f(x+0.0,y+1.0,z+0.0)
    glColor3f(0.545, 0.271, 0.075)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+-2.0, y+0.2, z+2.0)
    glVertex3f(x+-2.0, y+0.2, z+-2.0)
    glVertex3f(x+2.0, y+0.2, z+-2.0)
    
    #bottom
    #glNormal3f(x+0.0,y+-1.0,z+0.0)
    
    glVertex3f(x+2.0, y+-0.2, z+2.0)
    glVertex3f(x+-2.0, y+-0.2, z+2.0)
    glVertex3f(x+-2.0, y+-0.2, z+-2.0)
    glVertex3f(x+2.0, y+-0.2, z+-2.0)
    
    #table front leg
    #front
    #glNormal3f(x+0.0, y+0.0, z+1.0)
    
    glVertex3f(x+1.8,y+-0.2,z+1.6)
    glVertex3f(x+1.4, y+-0.2, z+1.6)
    glVertex3f(x+1.4, y+-3.0, z+1.6)
    glVertex3f(x+1.8, y+-3.0, z+1.6)
    
    #back
    #glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+1.8,y+-0.2,z+1.2)
    glVertex3f(x+1.4, y+-0.2, z+1.2)
    glVertex3f(x+1.4, y+-3.0, z+1.2)
    glVertex3f(x+1.8, y+-3.0, z+1.2)
    
    #right
    #glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+1.8,y+-0.2,z+1.6)
    glVertex3f(x+1.8, y+-0.2, z+1.2)
    glVertex3f(x+1.8, y+-3.0, z+1.2)
    glVertex3f(x+1.8, y+-3.0, z+1.6)
    
    #left
    #glNormal3f(x+-1.0, y+0.0, z+0.0)
    
    glVertex3f(x+1.4,y+-0.2,z+1.6)
    glVertex3f(x+1.4, y+-0.2, z+1.2)
    glVertex3f(x+1.4, y+-3.0, z+1.2)
    glVertex3f(x+1.4, y+-3.0, z+1.6)
    
    #back leg back
    #front
    #glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+1.8,y+-0.2,z+-1.2)
    glVertex3f(x+1.4, y+-0.2, z+-1.2)
    glVertex3f(x+1.4, y+-3.0, z+-1.2)
    glVertex3f(x+1.8, y+-3.0, z+-1.2)
    
    #back
    #glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+1.8,y+-0.2,z+-1.6)
    glVertex3f(x+1.4, y+-0.2, z+-1.6)
    glVertex3f(x+1.4, y+-3.0, z+-1.6)
    glVertex3f(x+1.8, y+-3.0, z+-1.6)
    
    #right
    #glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+1.8,y+-0.2,z+-1.6)
    glVertex3f(x+1.8, y+-0.2, z+-1.2)
    glVertex3f(x+1.8, y+-3.0, z+-1.2)
    glVertex3f(x+1.8, y+-3.0, z+-1.6)
    
    #left
    #glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+1.4,y+-0.2,z+-1.6)
    glVertex3f(x+1.4, y+-0.2, z+-1.2)
    glVertex3f(x+1.4, y+-3.0, z+-1.2)
    glVertex3f(x+1.4, y+-3.0, z+-1.6)
    
    #leg left front
    #glNormal3f(x+0.0, y+0.0, z+1.0)
    
    glVertex3f(x+-1.8,y+-0.2, z+1.6)
    glVertex3f(x+-1.4, y+-0.2, z+1.6)
    glVertex3f(x+-1.4, y+-3.0, z+1.6)
    glVertex3f(x+-1.8, y+-3.0, z+1.6)
    
    #back
    #glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+1.2)
    glVertex3f(x+-1.4, y+-0.2, z+1.2)
    glVertex3f(x+-1.4, y+-3.0, z+1.2)
    glVertex3f(x+-1.8, y+-3.0, z+1.2)
    
    #right
    #glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+1.6)
    glVertex3f(x+-1.8, y+-0.2, z+1.2)
    glVertex3f(x+-1.8, y+-3.0, z+1.2)
    glVertex3f(x+-1.8, y+-3.0, z+1.6)
    
    #left
    #glNormal3f(x+-1.0, y+0.0, z+0.0)
    
    glVertex3f(x+-1.4,y+-0.2,z+1.6)
    glVertex3f(x+-1.4, y+-0.2, z+1.2)
    glVertex3f(x+-1.4, y+-3.0, z+1.2)
    glVertex3f(x+-1.4, y+-3.0, z+1.6)
    
    #left leg back front
    
    #front
    #glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+-1.2)
    glVertex3f(x+-1.4, y+-0.2, z+-1.2)
    glVertex3f(x+-1.4, y+-3.0, z+-1.2)
    glVertex3f(x+-1.8, y+-3.0, z+-1.2)
    
    #back
    #glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+-1.6)
    glVertex3f(x+-1.4, y+-0.2, z+-1.6)
    glVertex3f(x+-1.4, y+-3.0, z+-1.6)
    glVertex3f(x+-1.8, y+-3.0, z+-1.6)
    
    #right
    #glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+-1.6)
    glVertex3f(x+-1.8, y+-0.2, z+-1.2)
    glVertex3f(x+-1.8, y+-3.0, z+-1.2)
    glVertex3f(x+-1.8, y+-3.0, z+-1.6)
    
    #left
    #glNormal3f(x+-1.0, y+0.0, z+0.0)
    
    glVertex3f(x+-1.4,y+-0.2,z+-1.6)
    glVertex3f(x+-1.4, y+-0.2, z+-1.2)
    glVertex3f(x+-1.4, y+-3.0, z+-1.2)
    glVertex3f(x+-1.4, y+-3.0, z+-1.6)
    
    #chair back
    #front
    glColor3f(0.502, 0.000, 0.000)
    #glColor3f(1,0,0)
    #glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(x+-1.8, y+0.2, z+-1.8)
    glVertex3f(x+1.8, y+0.2, z+-1.8)
    glVertex3f(x+1.8, y+3.5, z+-1.8)
    glVertex3f(x+-1.8, y+3.5, z+-1.8)
    
    #back
    #glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(x+-1.8, y+0.2, z+-2.0)
    glVertex3f(x+1.8, y+0.2, z+-2.0)
    glVertex3f(x+1.8, y+3.5, z+-2.0)
    glVertex3f(x+-1.8, y+3.5, z+-2.0)
    
    #glNormal3f(-1.0, 0.0, 0.0)
    glVertex3f(x+-1.8, y+0.2, z+-2.0)
    glVertex3f(x+-1.8, y+3.5, z+-2.0)
    glVertex3f(x+-1.8, y+3.5, z+-1.8)
    glVertex3f(x+-1.8, y+0.2, z+-1.8)
    
    
    glVertex3f(x+1.8, y+0.2, z+-2.0)
    glVertex3f(x+1.8, y+3.5, z+-2.0)
    glVertex3f(x+1.8, y+3.5, z+-1.8)
    glVertex3f(x+1.8, y+0.2, z+-1.8)
    
    glVertex3f(x+-1.8, y+3.5, z+-2.0)
    glVertex3f(x+-1.8, y+3.5, z+-1.8)
    glVertex3f(x+1.8, y+3.5, z+-1.8)
    glVertex3f(x+1.8, y+3.5, z+-2.0)
    glEnd()
    return
def CubeGlut():
    glColor3f(1, 1, 0)
    glPushMatrix()
    glTranslatef(1, 1, 1)
    glutWireCube(1)
    glPopMatrix()
    return

def Cube(x=0, y=0, z=0, scale = 1):
    vertices = (
        ((x+1)*scale, (y-1)*scale, (z-1)*scale),
        ((x+1)*scale, (y+1)*scale, (z-1)*scale),
        ((x-1)*scale, (y+1)*scale, (z-1)*scale),
        ((x-1)*scale, (y-1)*scale, (z-1)*scale),
        ((x+1)*scale, (y-1)*scale, (z+1)*scale),
        ((x+1)*scale, (y+1)*scale, (z+1)*scale),
        ((x-1)*scale, (y-1)*scale, (z+1)*scale),
        ((x-1)*scale, (y+1)*scale, (z+1)*scale),
    )

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7),
    )

    glColor3f(0, 1, 1)
    glBegin(GL_LINES)
    
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()
    return

def Triangle():
    glBegin(GL_TRIANGLES)

    glColor3f(255, 0, 0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0, 255, 0)
    glVertex2f(0.5, 0.0)
    glColor3f(0, 0, 255)
    glVertex2f(0.5, 5.0)

    glEnd()

    glColor3f(1, 1, 1)
    return
