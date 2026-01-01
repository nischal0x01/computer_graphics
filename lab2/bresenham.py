from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def bresenham_line(x1, y1, x2, y2):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    glBegin(GL_POINTS)
    while True:
        glVertex2i(x1, y1)
        if x1 == x2 and y1 == y2: break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.5, 0.0) # Orange Line
    bresenham_line(100, 400, 400, 100) # Negative slope
    bresenham_line(50, 50, 450, 300)   # Positive slope
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Bresenham Line Drawing")
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(display)
glutMainLoop()