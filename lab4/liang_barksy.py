from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

X_MIN, Y_MIN = -0.5, -0.5
X_MAX, Y_MAX = 0.5, 0.5


def liang_barsky(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - X_MIN, X_MAX - x1, y1 - Y_MIN, Y_MAX - y1]

    u1, u2 = 0.0, 1.0

    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                return None
        else:
            t = qi / pi
            if pi < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)

    if u1 > u2:
        return None

    return (
        x1 + u1 * dx,
        y1 + u1 * dy,
        x1 + u2 * dx,
        y1 + u2 * dy
    )


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

    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(-0.8, 0.6)
    glVertex2f(0.9, -0.4)
    glEnd()

    clipped = liang_barsky(-0.8, 0.6, 0.9, -0.4)
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
    glutCreateWindow(b"Liang-Barsky Line Clipping")
    gluOrtho2D(-1, 1, -1, 1)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()

