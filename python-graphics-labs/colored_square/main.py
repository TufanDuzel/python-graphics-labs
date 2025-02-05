import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def draw_square():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)

    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, -1.0, 0.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_square()
        pygame.display.flip()
        pygame.time.wait(10)

main()