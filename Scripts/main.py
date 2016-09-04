from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def draw():
    return 0

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(800, 600)

glutInitWindowPosition(150, 150)

glutInit(sys.argv)

glutCreateWindow(b"FAR SIDE")

glutDisplayFunc(draw)

glutMainLoop()
