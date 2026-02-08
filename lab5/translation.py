from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Constants
CUBE_VERTS = [(-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1), (-1,-1,1), (1,-1,1), (1,1,1), (-1,1,1)]
CUBE_EDGES = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
TRANSLATION = (2.5, 1.5, 0)

def draw_wire_cube(vertices):
    glBegin(GL_LINES)
    for edge in CUBE_EDGES:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_axes():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(1, 0, 0); glVertex3f(-5,0,0); glVertex3f(5,0,0) # X - Red
    glColor3f(0, 1, 0); glVertex3f(0,-5,0); glVertex3f(0,5,0) # Y - Green
    glColor3f(0, 0, 1); glVertex3f(0,0,-5); glVertex3f(0,0,5) # Z - Blue
    glEnd()
    glLineWidth(1.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -10)

    draw_axes()

    # Original Cube - Cyan
    glColor3f(0.2, 0.7, 1.0)
    draw_wire_cube(CUBE_VERTS)

    # Translated Cube - Orange
    translated_verts = [(v[0]+TRANSLATION[0], v[1]+TRANSLATION[1], v[2]+TRANSLATION[2]) for v in CUBE_VERTS]
    glColor3f(1.0, 0.6, 0.0)
    draw_wire_cube(translated_verts)

    glutSwapBuffers()

def init():
    glClearColor(0.05, 0.05, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 50)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"3D Translation")
init()
glutDisplayFunc(display)
glutMainLoop()