import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def scale_point(p, sx, sy):
    matrix = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
    x, y = p
    return (matrix[0][0]*x, matrix[1][1]*y)

def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    gluOrtho2D(-10, 10, -10, 10)
    square = [(1,1), (3,1), (3,3), (1,3)]
    transformed = [scale_point(p, 2, 0.5) for p in square]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1); glBegin(GL_LINE_LOOP); [glVertex2f(p[0], p[1]) for p in square]; glEnd()
        glColor3f(0, 0, 1); glBegin(GL_POLYGON); [glVertex2f(p[0], p[1]) for p in transformed]; glEnd()
        pygame.display.flip()

if __name__ == "__main__": main()