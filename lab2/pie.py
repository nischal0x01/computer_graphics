from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

data = [30, 20, 15, 35] # Percentages
colors = [(1,0,0), (0,1,0), (0,0,1), (1,1,0)]

def draw_pie(xc, yc, r):
    total = sum(data)
    start_angle = 0
    for i, val in enumerate(data):
        sweep = (val / total) * 2 * math.pi
        glColor3fv(colors[i % len(colors)])
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(xc, yc)
        for j in range(51):
            theta = start_angle + (sweep * j / 50)
            glVertex2f(xc + r * math.cos(theta), yc + r * math.sin(theta))
        glEnd()
        start_angle += sweep

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_pie(250, 250, 180)
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Pie Chart Implementation")
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(display)
glutMainLoop()