from OpenGL.GL import *
from OpenGL.GLUT import glutWireCube

# vertices = (
#     (1,  -1, -1),
#     (1,   1, -1),
#     (-1,  1, -1),
#     (-1, -1, -1),
#     (1,  -1,  1),
#     (1,   1,  1),
#     (-1, -1,  1),
#     (-1,  1,  1),
# )

# edges = (
#     (0, 1),
#     (0, 3),
#     (0, 4),
#     (2, 1),
#     (2, 3),
#     (2, 7),
#     (6, 3),
#     (6, 4),
#     (6, 7),
#     (5, 1),
#     (5, 4),
#     (5, 7),
# )
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



def Chair(x, y, z):
    glBegin(GL_QUADS)
    glColor3f(0.91, 0.76, 0.65)
    glNormal3f(x+0.0, y+0.0, z+1.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    
    #Right
    glNormal3f(x+1.0, y+0.0, z+0.0)
    glVertex3f(x+2.0, y+-0.2, z+-2.0)
    glVertex3f(x+2.0, y+0.2, z+-2.0)
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+2.0, y+-0.2, z+2.0)
    
    #Back
    glNormal3f(x+0.0, y+0.0, z+-1.0)
    glVertex3f(x-2.0, y+-0.2, z+-2.0)
    glVertex3f(x+-2.0, y+0.2, z+-2.0)
    glVertex3f(x+2.0, y+0.2, z+-2.0)
    glVertex3f(x+2.0, y+-0.2, z+-2.0)
    
    #Left
    glNormal3f(x+-1.0, y+0.0, z+0.0)
    glVertex3f(x+-2.0, y+-0.2, z+-2.0)
    glVertex3f(x+-2.0, y+-0.2, z+2.0)
    glVertex3f(x+-2.0, y+0.2, z+2.0)
    glVertex3f(x+-2.0, y+0.2, z+-2.0)
    
    #top
    glNormal3f(x+0.0,y+1.0,z+0.0)
    
    glVertex3f(x+2.0, y+0.2, z+2.0)
    glVertex3f(x+-2.0, y+0.2, z+2.0)
    glVertex3f(x+-2.0, y+0.2, z+-2.0)
    glVertex3f(x+2.0, y+0.2, z+-2.0)
    
    #bottom
    glNormal3f(x+0.0,y+-1.0,z+0.0)
    
    glVertex3f(x+2.0, y+-0.2, z+2.0)
    glVertex3f(x+-2.0, y+-0.2, z+2.0)
    glVertex3f(x+-2.0, y+-0.2, z+-2.0)
    glVertex3f(x+2.0, y+-0.2, z+-2.0)
    
    #table front leg
    #front
    glNormal3f(x+0.0, y+0.0, z+1.0)
    
    glVertex3f(x+1.8,y+-0.2,z+1.6)
    glVertex3f(x+1.4, y+-0.2, z+1.6)
    glVertex3f(x+1.4, y+-3.0, z+1.6)
    glVertex3f(x+1.8, y+-3.0, z+1.6)
    
    #back
    glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+1.8,y+-0.2,z+1.2)
    glVertex3f(x+1.4, y+-0.2, z+1.2)
    glVertex3f(x+1.4, y+-3.0, z+1.2)
    glVertex3f(x+1.8, y+-3.0, z+1.2)
    
    #right
    glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+1.8,y+-0.2,z+1.6)
    glVertex3f(x+1.8, y+-0.2, z+1.2)
    glVertex3f(x+1.8, y+-3.0, z+1.2)
    glVertex3f(x+1.8, y+-3.0, z+1.6)
    
    #left
    glNormal3f(x+-1.0, y+0.0, z+0.0)
    
    glVertex3f(x+1.4,y+-0.2,z+1.6)
    glVertex3f(x+1.4, y+-0.2, z+1.2)
    glVertex3f(x+1.4, y+-3.0, z+1.2)
    glVertex3f(x+1.4, y+-3.0, z+1.6)
    
    #back leg back
    #front
    glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+1.8,y+-0.2,z+-1.2)
    glVertex3f(x+1.4, y+-0.2, z+-1.2)
    glVertex3f(x+1.4, y+-3.0, z+-1.2)
    glVertex3f(x+1.8, y+-3.0, z+-1.2)
    
    #back
    glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+1.8,y+-0.2,z+-1.6)
    glVertex3f(x+1.4, y+-0.2, z+-1.6)
    glVertex3f(x+1.4, y+-3.0, z+-1.6)
    glVertex3f(x+1.8, y+-3.0, z+-1.6)
    
    #right
    glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+1.8,y+-0.2,z+-1.6)
    glVertex3f(x+1.8, y+-0.2, z+-1.2)
    glVertex3f(x+1.8, y+-3.0, z+-1.2)
    glVertex3f(x+1.8, y+-3.0, z+-1.6)
    
    #left
    glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+1.4,y+-0.2,z+-1.6)
    glVertex3f(x+1.4, y+-0.2, z+-1.2)
    glVertex3f(x+1.4, y+-3.0, z+-1.2)
    glVertex3f(x+1.4, y+-3.0, z+-1.6)
    
    #leg left front
    glNormal3f(x+0.0, y+0.0, z+1.0)
    
    glVertex3f(x+-1.8,y+-0.2, z+1.6)
    glVertex3f(x+-1.4, y+-0.2, z+1.6)
    glVertex3f(x+-1.4, y+-3.0, z+1.6)
    glVertex3f(x+-1.8, y+-3.0, z+1.6)
    
    #back
    glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+1.2)
    glVertex3f(x+-1.4, y+-0.2, z+1.2)
    glVertex3f(x+-1.4, y+-3.0, z+1.2)
    glVertex3f(x+-1.8, y+-3.0, z+1.2)
    
    #right
    glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+1.6)
    glVertex3f(x+-1.8, y+-0.2, z+1.2)
    glVertex3f(x+-1.8, y+-3.0, z+1.2)
    glVertex3f(x+-1.8, y+-3.0, z+1.6)
    
    #left
    glNormal3f(x+-1.0, y+0.0, z+0.0)
    
    glVertex3f(x+-1.4,y+-0.2,z+1.6)
    glVertex3f(x+-1.4, y+-0.2, z+1.2)
    glVertex3f(x+-1.4, y+-3.0, z+1.2)
    glVertex3f(x+-1.4, y+-3.0, z+1.6)
    
    #left leg back front
    
    #front
    glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+-1.2)
    glVertex3f(x+-1.4, y+-0.2, z+-1.2)
    glVertex3f(x+-1.4, y+-3.0, z+-1.2)
    glVertex3f(x+-1.8, y+-3.0, z+-1.2)
    
    #back
    glNormal3f(x+0.0, y+0.0, z+-1.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+-1.6)
    glVertex3f(x+-1.4, y+-0.2, z+-1.6)
    glVertex3f(x+-1.4, y+-3.0, z+-1.6)
    glVertex3f(x+-1.8, y+-3.0, z+-1.6)
    
    #right
    glNormal3f(x+1.0, y+0.0, z+0.0)
    
    glVertex3f(x+-1.8,y+-0.2,z+-1.6)
    glVertex3f(x+-1.8, y+-0.2, z+-1.2)
    glVertex3f(x+-1.8, y+-3.0, z+-1.2)
    glVertex3f(x+-1.8, y+-3.0, z+-1.6)
    
    #left
    glNormal3f(x+-1.0, y+0.0, z+0.0)
    
    glVertex3f(x+-1.4,y+-0.2,z+-1.6)
    glVertex3f(x+-1.4, y+-0.2, z+-1.2)
    glVertex3f(x+-1.4, y+-3.0, z+-1.2)
    glVertex3f(x+-1.4, y+-3.0, z+-1.6)
    
    #chair back
    #front
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

def CubeGlut():
    glColor3f(1, 1, 0)
    glPushMatrix()
    glTranslatef(1, 1, 1)
    glutWireCube(1)
    glPopMatrix()

def Cube(x, y, z):
    vertices = (
        (x+1, y-1, z-1),
        (x+1, y+1, z-1),
        (x-1, y+1, z-1),
        (x-1, y-1, z-1),
        (x+1, y-1, z+1),
        (x+1, y+1, z+1),
        (x-1, y-1, z+1),
        (x-1, y+1, z+1),
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


def Point():
    glPointSize(10)

    glBegin(GL_POINTS)

    glVertex2f(5, 5)
    glVertex2f(-5, -5)

    glEnd()
