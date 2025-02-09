import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def init_scene():
    glClearColor(0.53, 0.81, 0.92, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)

def draw_sun():
    glColor3f(1, 1, 0)
    glBegin(GL_POLYGON)
    for angle in range(0, 360, 10):
        theta = angle * math.pi / 180
        glVertex2f(7 + 2 * math.cos(theta), 7 + 2 * math.sin(theta))
    glEnd()

def draw_cloud(x, y):
    glColor3f(1, 1, 1)
    for dx, dy, sx, sy in [(0, 1, 1.5, 1), (-1, 0, 2, 1.5), (1, 0, 2, 1.5)]:
        glBegin(GL_POLYGON)
        for angle in range(0, 360, 10):
            theta = angle * math.pi / 180
            glVertex2f(x + dx + sx * math.cos(theta), y + dy + sy * math.sin(theta))
        glEnd()

def draw_house():
    glColor3f(0.8, 0.52, 0.25)
    glBegin(GL_QUADS)
    glVertex2f(-4, -4)
    glVertex2f(-1, -4)
    glVertex2f(-1, -1)
    glVertex2f(-4, -1)
    glEnd()
    glColor3f(0.6, 0.1, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(-4, -1)
    glVertex2f(-1, -1)
    glVertex2f(-2.5, 1)
    glEnd()

def draw_car():
    glColor3f(0.1, 0.6, 0.8)
    glBegin(GL_QUADS)
    glVertex2f(0, -6)
    glVertex2f(5, -6)
    glVertex2f(5, -4)
    glVertex2f(0, -4)
    glEnd()
    for cx in [1, 4]:
        glColor3f(0, 0, 0)
        glBegin(GL_POLYGON)
        for angle in range(0, 360, 10):
            theta = angle * math.pi / 180
            glVertex2f(cx + 0.5 * math.cos(theta), -6.5 + 0.5 * math.sin(theta))
        glEnd()

def draw_tree():
    glColor3f(0.55, 0.27, 0.07)
    glBegin(GL_QUADS)
    glVertex2f(-7, -5)
    glVertex2f(-6, -5)
    glVertex2f(-6, -2)
    glVertex2f(-7, -2)
    glEnd()
    glColor3f(0, 0.8, 0)
    for dx, dy in [(0, 0), (-0.5, 1), (0.5, 1)]:
        glBegin(GL_POLYGON)
        for angle in range(0, 360, 10):
            theta = angle * math.pi / 180
            glVertex2f(-6.5 + dx + math.cos(theta), -2 + dy + math.sin(theta))
        glEnd()

def draw_grass():
    glColor3f(0, 1, 0)
    for i in range(-10, 11, 1):
        glBegin(GL_QUADS)
        glVertex2f(i, -10)
        glVertex2f(i + 0.5, -10)
        glVertex2f(i + 0.5, -9.5)
        glVertex2f(i, -9.5)
        glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init_scene()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_sun()
        draw_cloud(-4, 6)
        draw_cloud(4, 7)
        draw_house()
        draw_car()
        draw_tree()
        draw_grass()
        pygame.display.flip()
        pygame.time.wait(10)
    pygame.quit()

if __name__ == "__main__":
    main()
