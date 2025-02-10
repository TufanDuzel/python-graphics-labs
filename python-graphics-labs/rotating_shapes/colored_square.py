import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    [1, 1, 0],
    [-1, 1, 0],
    [-1, -1, 0],
    [1, -1, 0]
]

colors = [
    [1, 0, 0],  # Kırmızı
    [0, 1, 0],  # Yeşil
    [0, 0, 1],  # Mavi
    [1, 1, 0]   # Sarı
]

def draw_colored_square():
    glBegin(GL_QUADS)
    for i, vertex in enumerate(vertices):
        glColor3fv(colors[i])
        glVertex3fv(vertex)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-2, 2, -2, 2)

    angle = 0
    speed = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            speed += 0.1
        if keys[K_DOWN]:
            speed -= 0.1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(angle, 0, 0, 1)
        draw_colored_square()
        glPopMatrix()

        angle += speed
        pygame.display.flip()
        pygame.time.wait(10)

main()
