
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import surface

class Display:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Far Prototype")
        self.set_display((640, 480))
