from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image
import numpy


def run_scene():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow("Minimal sphere OpenGL")
    lightning()
    glutDisplayFunc(draw_sphere)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40, 1, 1, 40)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 0, 10,
              0, 0, 0,
              0, 1, 0)
    glPushMatrix()
    glutMainLoop()
    return


def lightning():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glLightfv(GL_LIGHT0, GL_POSITION, [10, 4, 10, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 1, 0.8, 1])
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    return

def draw_sphere():
    x=0
    y=0
    z=0
    scale = 1
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    texture_id = read_texture('Imgs/janela.png')
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glBegin(GL_QUADS)
    vertices = [
            ((x+1.5) * scale, (y+1.25) * scale, (z) * scale),
            ((x-1.5) * scale, (y+1.25) * scale, (z) * scale),
            ((x-1.5) * scale, (y-1.25) * scale, (z) * scale),
            ((x+1.5) * scale, (y-1.25) * scale, (z) * scale)
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
    #glutSolidSphere(1, 50, 50)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glutSwapBuffers()
    return


def read_texture(filename):

    img = Image.open(filename)
    img = img.convert("RGB")
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id) # This is what's missing
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    format = GL_RGB if img.mode == "RGB" else GL_RGBA
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0,
             format, GL_UNSIGNED_BYTE, img_data)
    return texture_id


    glBegin(GL_QUAD_STRIP)
    vertices = [
            ((x+1.5) * scale, (y+1.25) * scale, (z) * scale),
            ((x-1.5) * scale, (y+1.25) * scale, (z) * scale),
            ((x-1.5) * scale, (y-1.25) * scale, (z) * scale),
            ((x+1.5) * scale, (y-1.25) * scale, (z) * scale)
        ]
    edges = (
        (0, 1),
        (1, 2),
        (1, 3),
        (3, 0),
    )

    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

if __name__ == '__main__':
    run_scene()