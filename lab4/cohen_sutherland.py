from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Clipping window
X_MIN, Y_MIN = -0.5, -0.5
X_MAX, Y_MAX = 0.5, 0.5

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


def compute_code(x, y):
    code = INSIDE
    if x < X_MIN:
        code |= LEFT
    elif x > X_MAX:
        code |= RIGHT
    if y < Y_MIN:
        code |= BOTTOM
    elif y > Y_MAX:
        code |= TOP
    return code


def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    while True:
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2
        if code1 & code2 != 0:
            return None

        code_out = code1 if code1 else code2

        if code_out & TOP:
            x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1)
            y = Y_MAX
        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1)
            y = Y_MIN
        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (X_MAX - x1) / (x2 - x1)
            x = X_MAX
        elif code_out & LEFT:
            y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1)
            x = X_MIN

        if code_out == code1:
            x1, y1 = x, y
            code1 = compute_code(x1, y1)
        else:
            x2, y2 = x, y
            code2 = compute_code(x2, y2)


def draw_window():
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(X_MIN, Y_MIN)
    glVertex2f(X_MAX, Y_MIN)
    glVertex2f(X_MAX, Y_MAX)
    glVertex2f(X_MIN, Y_MAX)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_window()

    # Original line
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-0.8, -0.2)
    glVertex2f(0.8, 0.7)
    glEnd()

    clipped = cohen_sutherland(-0.8, -0.2, 0.8, 0.7)
    if clipped:
        glColor3f(0, 1, 0)
        glBegin(GL_LINES)
        glVertex2f(clipped[0], clipped[1])
        glVertex2f(clipped[2], clipped[3])
        glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Cohen-Sutherland Line Clipping")
    gluOrtho2D(-1, 1, -1, 1)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
