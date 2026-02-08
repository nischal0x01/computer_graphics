from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

sx = sy = sz = 1

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0, 0, -8)
    glScalef(sx, sy, sz)

    glColor3f(0.9, 0.3, 0.3)
    glutSolidSphere(1.5, 40, 40)

    glutSwapBuffers()

def keyboard(key, x, y):
    global sx, sy, sz
    key = key.decode()

    if key == '+':
        sx += 0.1; sy += 0.1; sz += 0.1
    if key == '-':
        sx -= 0.1; sy -= 0.1; sz -= 0.1

    glutPostRedisplay()

def reshape(w, h):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w/h, 1, 100)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(700, 600)
glutCreateWindow(b"3D Scaling")
glEnable(GL_DEPTH_TEST)

glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutReshapeFunc(reshape)
glutMainLoop()
