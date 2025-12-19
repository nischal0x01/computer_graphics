from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_rect(x, y, w, h):
    glBegin(GL_POLYGON)
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h)
    glVertex2f(x, y + h)
    glEnd()

# ----- Letter Functions -----
def draw_N(x):
    draw_rect(x, 0.0, 0.05, 0.4)
    draw_rect(x + 0.15, 0.0, 0.05, 0.4)
    draw_rect(x, 0.35, 0.2, 0.05)

def draw_I(x):
    draw_rect(x, 0.0, 0.2, 0.05)
    draw_rect(x + 0.075, 0.0, 0.05, 0.4)
    draw_rect(x, 0.35, 0.2, 0.05)

def draw_S(x):
    draw_rect(x, 0.35, 0.2, 0.05)
    draw_rect(x, 0.2, 0.05, 0.15)
    draw_rect(x, 0.2, 0.2, 0.05)
    draw_rect(x + 0.15, 0.0, 0.05, 0.2)
    draw_rect(x, 0.0, 0.2, 0.05)

def draw_C(x):
    draw_rect(x, 0.35, 0.2, 0.05)
    draw_rect(x, 0.0, 0.2, 0.05)
    draw_rect(x, 0.0, 0.05, 0.4)

def draw_H(x):
    draw_rect(x, 0.0, 0.05, 0.4)
    draw_rect(x + 0.15, 0.0, 0.05, 0.4)
    draw_rect(x, 0.2, 0.2, 0.05)

def draw_A(x):
    draw_rect(x, 0.0, 0.05, 0.4)
    draw_rect(x + 0.15, 0.0, 0.05, 0.4)
    draw_rect(x, 0.35, 0.2, 0.05)
    draw_rect(x, 0.2, 0.2, 0.05)

def draw_L(x):
    draw_rect(x, 0.0, 0.05, 0.4)
    draw_rect(x, 0.0, 0.2, 0.05)

# ----- Display -----
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.1, 0.5, 0.9)  # blue color
    
    draw_N(-0.9)
    draw_I(-0.65)
    draw_S(-0.4)
    draw_C(-0.15)
    draw_H(0.1)
    draw_A(0.35)
    draw_L(0.6)
    
    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # white background
    glMatrixMode(GL_PROJECTION)  # <- ADDED THIS
    glLoadIdentity()              # <- ADDED THIS
    gluOrtho2D(-1, 1, -1, 1)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)  # <- ADDED: positions window on screen
    glutCreateWindow(b"NISCHAL - OpenGL Python")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()