import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    [0, 1, 0],
    [-1, -1, 0],
    [1, -1, 0]
]

def draw_triangle():
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-2, 2, -2, 2)

    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(angle, 0, 0, 1)
        draw_triangle()
        glPopMatrix()

        angle += 1
        pygame.display.flip()
        pygame.time.wait(10)

main()
