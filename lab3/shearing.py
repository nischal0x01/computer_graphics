import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def shear_point(p, shx, shy):
    matrix = [[1, shx, 0], [shy, 1, 0], [0, 0, 1]]
    x, y = p
    new_x = x + shx * y
    new_y = shy * x + y
    return (new_x, new_y)

def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    gluOrtho2D(-10, 10, -10, 10)
    square = [(1,1), (3,1), (3,3), (1,3)]
    transformed = [shear_point(p, 1.5, 0) for p in square]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1); glBegin(GL_LINE_LOOP); [glVertex2f(p[0], p[1]) for p in square]; glEnd()
        glColor3f(1, 0, 1); glBegin(GL_POLYGON); [glVertex2f(p[0], p[1]) for p in transformed]; glEnd()
        pygame.display.flip()

if __name__ == "__main__": main()