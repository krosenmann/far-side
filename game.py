#!/usr/bin/env python
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(640, 480) #изменить на данные, прочтенные из сетап-файла
glutInitWindowPosition(50, 50)# analog
glutInit(sys.argv)
glutCreateWindow(b"Far Prototype") #too, but i'm not entierly sure
glutMainLoop() #ofcourse
