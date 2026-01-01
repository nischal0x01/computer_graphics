from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def midpoint_circle(xc, yc, r):
    x, y = 0, r
    p = 1 - r
    glBegin(GL_POINTS)
    while x <= y:
        # 8-way symmetry
        for dx, dy in [(x,y), (y,x), (y,-x), (x,-y), (-x,-y), (-y,-x), (-y,x), (-x,y)]:
            glVertex2i(xc + dx, yc + dy)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 1.0) # Cyan Circle
    midpoint_circle(250, 250, 150)
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Midpoint Circle Drawing")
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(display)
glutMainLoop()