from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def loadOBJ(filename):
    numVerts = 0  
    verts = []  
    norms = []  
    vertsOut = []  
    normsOut = []  
    for line in open("C:\\Users\й\Desktop\Prjct\far-side\res\models\cube.obj", "r"):
        vals = line.split()  
        if vals[0] == "v":  
            v = map(float, vals[1:4])  
            verts.append(v)  
        if vals[0] == "vn":  
            n = map(float, vals[1:4])  
            norms.append(n)  
        if vals[0] == "f":  
            for f in vals[1:]:  
                w = f.split("/")  
                # OBJ Files are 1-indexed so we must subtract 1 below  
                vertsOut.append(list(verts[int(w[0])-1]))  
                normsOut.append(list(norms[int(w[2])-1]))  
                numVerts += 1  
    return vertsOut, normsOut


glutInit("")
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutInitWindowPosition(50, 50)
glutCreateWindow(b"FAR SIDE")
glutDisplayFunc(loadOBJ)
# if bool(config.get("VIDEO", "WindowedMode")):
#    glutFullScreen()
# else:
#    print("WindowedMode")
glutIdleFunc(loadOBJ)
glutMainLoop()
