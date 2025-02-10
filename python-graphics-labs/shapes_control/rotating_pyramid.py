import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Vertices and edges of the pyramid
vertices = [
    (0, 1, 0),  # Apex (tepe noktası)
    (-1, -1, -1),  # Base corner 1
    (1, -1, -1),  # Base corner 2
    (1, -1, 1),  # Base corner 3
    (-1, -1, 1)  # Base corner 4
]

edges = [
    (0, 1), (0, 2), (0, 3), (0, 4),  # Tepe noktası tabana bağlanıyor
    (1, 2), (2, 3), (3, 4), (4, 1)  # Taban kenarları
]

def Pyramid():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Pyramid()
        pygame.display.flip()
        pygame.time.wait(10)

main()
