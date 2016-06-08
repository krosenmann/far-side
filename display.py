
import pygame
#from pygame.locals import *
#from OpenGL.GL import *
#from OpenGL.GLU import *
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
try:
    parser.read('gameconfig.cfg')
    resolution = parser.get('display','resolution')
except:
    print TypeError
    resolution = (640, 480)
#import surface

class Display:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Far Prototype")
        self.set_display(resolution)
