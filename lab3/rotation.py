import pygame, math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def rotate_point(p, angle):
    rad = math.radians(angle)
    c, s = math.cos(rad), math.sin(rad)
    # Homogeneous Rotation Matrix
    matrix = [[c, -s, 0], [s, c, 0], [0, 0, 1]]
    x, y = p
    new_x = matrix[0][0]*x + matrix[0][1]*y + matrix[0][2]*1
    new_y = matrix[1][0]*x + matrix[1][1]*y + matrix[1][2]*1
    return (new_x, new_y)

def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    gluOrtho2D(-10, 10, -10, 10)
    tri = [(1,1), (4,1), (2.5,4)]
    transformed = [rotate_point(p, 45) for p in tri]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1); glBegin(GL_LINE_LOOP); [glVertex2f(p[0], p[1]) for p in tri]; glEnd()
        glColor3f(0, 1, 0); glBegin(GL_POLYGON); [glVertex2f(p[0], p[1]) for p in transformed]; glEnd()
        pygame.display.flip()

if __name__ == "__main__": main()