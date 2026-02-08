from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def shear(shx, shy):
    m = [
        1, shy, 0, 0,
        shx, 1, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1
    ]
    glMultMatrixf(m)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0, 0, -8)
    shear(0.5, 0.0)

    glColor3f(0.4, 0.6, 1)
    glutSolidCube(2)

    glutSwapBuffers()

def reshape(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w/h, 1, 100)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(700, 600)
glutCreateWindow(b"3D Shearing")
glEnable(GL_DEPTH_TEST)

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
