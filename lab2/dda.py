from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def dda_line(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    
    x, y = x1, y1
    glBegin(GL_POINTS)
    for _ in range(steps + 1):
        glVertex2i(round(x), round(y))
        x += x_inc
        y += y_inc
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0) # Green Line
    dda_line(50, 50, 450, 400)
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"DDA Line Drawing")
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(display)
glutMainLoop()