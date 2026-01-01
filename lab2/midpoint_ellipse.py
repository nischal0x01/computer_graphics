from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def midpoint_ellipse(xc, yc, rx, ry):
    x, y = 0, ry
    # Region 1
    p1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
    glBegin(GL_POINTS)
    while (2 * ry**2 * x) <= (2 * rx**2 * y):
        for dx, dy in [(x,y), (-x,y), (x,-y), (-x,-y)]:
            glVertex2i(xc + dx, yc + dy)
        x += 1
        if p1 < 0:
            p1 += 2 * ry**2 * x + ry**2
        else:
            y -= 1
            p1 += 2 * ry**2 * x - 2 * rx**2 * y + ry**2
    # Region 2
    p2 = (ry**2 * (x + 0.5)**2) + (rx**2 * (y - 1)**2) - (rx**2 * ry**2)
    while y >= 0:
        for dx, dy in [(x,y), (-x,y), (x,-y), (-x,-y)]:
            glVertex2i(xc + dx, yc + dy)
        y -= 1
        if p2 > 0:
            p2 += rx**2 - 2 * rx**2 * y
        else:
            x += 1
            p2 += 2 * ry**2 * x - 2 * rx**2 * y + rx**2
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0) # Magenta Ellipse
    midpoint_ellipse(250, 250, 200, 100)
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Midpoint Ellipse Drawing")
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(display)
glutMainLoop()