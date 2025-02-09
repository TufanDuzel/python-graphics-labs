import pygame
from pygame.locals import *
from OpenGL.GL import *
from math import cos, sin, pi

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glViewport(0, 0, 800, 600)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(-3, 3, -3, 3, -1, 1)
glMatrixMode(GL_MODELVIEW)

def draw_triangle():
    glPushMatrix()
    glTranslatef(-2, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(0, 1)
    glEnd()
    glPopMatrix()

def draw_square():
    glPushMatrix()
    glTranslatef(2, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()
    glPopMatrix()

def draw_rectangle():
    glPushMatrix()
    glTranslatef(-2, -1.5, 0)
    glBegin(GL_QUADS)
    glVertex2f(-1.5, -0.5)
    glVertex2f(1.5, -0.5)
    glVertex2f(1.5, 0.5)
    glVertex2f(-1.5, 0.5)
    glEnd()
    glPopMatrix()

def draw_circle():
    glPushMatrix()
    glTranslatef(2, -1.5, 0)
    sides = 32
    radius = 0.5
    glBegin(GL_TRIANGLE_FAN)
    for i in range(sides + 1):
        angle = 2 * pi * i / sides
        glVertex2f(radius * cos(angle), radius * sin(angle))
    glEnd()
    glPopMatrix()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)
    draw_triangle()
    draw_square()
    draw_rectangle()
    draw_circle()
    pygame.display.flip()

pygame.quit()
