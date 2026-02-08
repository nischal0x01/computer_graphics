from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

NEAR_POS = (0, 0, -4)
FAR_POS = (0, 0, -12)

def draw_grid():
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_LINES)
    for i in range(-10, 11):
        glVertex3f(i, -1, -20); glVertex3f(i, -1, 0)
        glVertex3f(-10, -1, -i-10); glVertex3f(10, -1, -i-10)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 3, 8, 0, 0, -5, 0, 1, 0)

    draw_grid()

    # Near Cube - Blue
    glPushMatrix()
    glTranslatef(*NEAR_POS)
    glColor3f(0.2, 0.6, 1.0)
    glutWireCube(2)
    glPopMatrix()

    # Far Cube - Orange
    glPushMatrix()
    glTranslatef(*FAR_POS)
    glColor3f(1.0, 0.5, 0.0)
    glutWireCube(2)
    glPopMatrix()

    glutSwapBuffers()

def init():
    glClearColor(0.05, 0.05, 0.05, 1)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 1, 100)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Perspective Projection")
init()
glutDisplayFunc(display)
glutMainLoop()