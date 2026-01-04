import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def translate_point(p, tx, ty):
    # Homogeneous Matrix for Translation
    matrix = [[1, 0, tx],
              [0, 1, ty],
              [0, 0, 1]]
    x, y = p
    # Matrix Multiplication: [1 0 tx][x], [0 1 ty][y], [0 0 1][1]
    new_x = matrix[0][0]*x + matrix[0][1]*y + matrix[0][2]*1
    new_y = matrix[1][0]*x + matrix[1][1]*y + matrix[1][2]*1
    return (new_x, new_y)

def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    gluOrtho2D(-10, 10, -10, 10)
    
    rect = [(0,0), (4,0), (4,2), (0,2)]
    transformed = [translate_point(p, 3, 2) for p in rect]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
        glClear(GL_COLOR_BUFFER_BIT)
        # Original (White)
        glColor3f(1, 1, 1)
        glBegin(GL_LINE_LOOP); [glVertex2f(p[0], p[1]) for p in rect]; glEnd()
        # Transformed (Red)
        glColor3f(1, 0, 0)
        glBegin(GL_POLYGON); [glVertex2f(p[0], p[1]) for p in transformed]; glEnd()
        pygame.display.flip()

if __name__ == "__main__": main()