from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

X_MIN, Y_MIN = -0.5, -0.5
X_MAX, Y_MAX = 0.5, 0.5


def inside(p, edge):
    x, y = p
    if edge == "LEFT":
        return x >= X_MIN
    if edge == "RIGHT":
        return x <= X_MAX
    if edge == "BOTTOM":
        return y >= Y_MIN
    if edge == "TOP":
        return y <= Y_MAX


def intersect(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2

    if edge == "LEFT":
        x = X_MIN
        y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1)
    elif edge == "RIGHT":
        x = X_MAX
        y = y1 + (y2 - y1) * (X_MAX - x1) / (x2 - x1)
    elif edge == "BOTTOM":
        y = Y_MIN
        x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1)
    elif edge == "TOP":
        y = Y_MAX
        x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1)

    return (x, y)


def sutherland_hodgman(polygon):
    edges = ["LEFT", "RIGHT", "BOTTOM", "TOP"]

    for edge in edges:
        new_poly = []
        for i in range(len(polygon)):
            curr = polygon[i]
            prev = polygon[i - 1]

            if inside(curr, edge):
                if not inside(prev, edge):
                    new_poly.append(intersect(prev, curr, edge))
                new_poly.append(curr)
            elif inside(prev, edge):
                new_poly.append(intersect(prev, curr, edge))
        polygon = new_poly

    return polygon


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

    polygon = [(-0.7, -0.3), (-0.2, 0.8), (0.7, 0.4), (0.4, -0.7)]
    clipped = sutherland_hodgman(polygon)

    glColor3f(0, 1, 0)
    glBegin(GL_LINE_LOOP)
    for x, y in clipped:
        glVertex2f(x, y)
    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Sutherland-Hodgman Polygon Clipping")
    gluOrtho2D(-1, 1, -1, 1)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
