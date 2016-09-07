from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import configparser
from pyglet.gl import *

config = configparser.RawConfigParser()
config.read("game.cfg")
window = int(config.get("VIDEO", "Window"))


def init():
    glClearColor(0.0, 0.0, 0.0, 0.5)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(config.get("VIDEO", "Width")) / float(config.get("VIDEO", "Height")), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def resize_window(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(config.get("VIDEO", "Width")) / float(config.get("VIDEO", "Height")), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    '''Раскомментить для проверки что хоть что-то рисуется
    glBegin(GL_POLYGON)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()
    '''

    glutSwapBuffers()
    glutPostRedisplay()


def exit_game(key):
    if key == GLUT_KEY_UP:  # - завершение с ошибкой, что не есть правильно.
        glutDestroyWindow(window)
        sys.exit()


def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(int(config.get("VIDEO", "Width")), int(config.get("VIDEO", "Height")))
    glutInitWindowPosition(int(config.get("VIDEO", "WindowPositionX")), int(config.get("VIDEO", "WindowPositionY")))
    window = glutCreateWindow(b"FAR SIDE")
    glutDisplayFunc(draw_scene)
    # if bool(config.get("VIDEO", "WindowedMode")): - пока не сделал парсинг значения из конфига - фуллскрин или нет.
    #    glutFullScreen()
    # else:
    #    print("WindowedMode")
    glutIdleFunc(draw_scene)
    # glutReshapeFunc(resize_window) - не работает правильно.
    glutKeyboardFunc(exit_game)
    glutMainLoop()


main()
