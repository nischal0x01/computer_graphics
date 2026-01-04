import pygame, math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def multiply_3x3(A, B):
    C = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k] * B[k][j]
    return C

def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    gluOrtho2D(-10, 10, -10, 10)
    
    # 1. Scaling Matrix
    S = [[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]]
    # 2. Rotation Matrix (30 deg)
    a = math.radians(30); c, s = math.cos(a), math.sin(a)
    R = [[c, -s, 0], [s, c, 0], [0, 0, 1]]
    # 3. Shear Matrix
    Sh = [[1, 0.5, 0], [0, 1, 0], [0, 0, 1]]
    # 4. Translation Matrix
    T = [[1, 0, 2], [0, 1, -3], [0, 0, 1]]

    # Composite = T * Sh * R * S (Applied right to left)
    comp = multiply_3x3(T, multiply_3x3(Sh, multiply_3x3(R, S)))
    
    shape = [(0,0), (2,0), (2,2), (0,2)]
    transformed = []
    for x, y in shape:
        nx = comp[0][0]*x + comp[0][1]*y + comp[0][2]*1
        ny = comp[1][0]*x + comp[1][1]*y + comp[1][2]*1
        transformed.append((nx, ny))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1); glBegin(GL_LINE_LOOP); [glVertex2f(p[0], p[1]) for p in shape]; glEnd()
        glColor3f(0, 1, 1); glBegin(GL_POLYGON); [glVertex2f(p[0], p[1]) for p in transformed]; glEnd()
        pygame.display.flip()

if __name__ == "__main__": main()