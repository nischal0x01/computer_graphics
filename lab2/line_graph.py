from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Sample Data: (x, y)
dataset = [(50, 50), (100, 200), (200, 150), (300, 400), (450, 300)]

def bresenham_line(x1, y1, x2, y2):
    dx, dy = abs(x2-x1), abs(y2-y1)
    sx, sy = (1 if x1<x2 else -1), (1 if y1<y2 else -1)
    err = dx - dy
    glBegin(GL_POINTS)
    while True:
        glVertex2i(x1, y1)
        if x1 == x2 and y1 == y2: break
        e2 = 2 * err
        if e2 > -dy: err -= dy; x1 += sx
        if e2 < dx: err += dx; y1 += sy
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0) # White lines
    for i in range(len(dataset) - 1):
        p1, p2 = dataset[i], dataset[i+1]
        bresenham_line(p1[0], p1[1], p2[0], p2[1])
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Line Graph Implementation")
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(display)
glutMainLoop()