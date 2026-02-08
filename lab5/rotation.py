from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

ROT_ANGLE = 45.0
ROT_AXIS = (0, 1, 0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -7)

    # Original - Darker Blue
    glColor3f(0.2, 0.5, 0.8)
    glutWireCube(2)

    # Rotated - Bright Orange
    glPushMatrix()
    glRotatef(ROT_ANGLE, *ROT_AXIS)
    glColor3f(1.0, 0.5, 0.0)
    glutWireCube(2)
    glPopMatrix()

    glutSwapBuffers()

def init():
    glClearColor(0.1, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 1, 50)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitWindowSize(800, 600)
glutCreateWindow(b"3D Rotation")
init()
glutDisplayFunc(display)
glutMainLoop()