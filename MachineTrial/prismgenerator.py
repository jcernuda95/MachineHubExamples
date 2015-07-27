#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)

from FreeCAD import Base
import Part

def machinebuilder(x, y, z, file_path):
    '''
[doc]
-title-
prism
-description-
Create a parametric cube
-images_url-
http://images.freeimages.com/images/previews/92c/toy-1419795.jpg
http://images.freeimages.com/images/previews/ea8/wooden-cubes-1189233.jpg
http://images.freeimages.com/images/previews/b9c/cubes-1-1178873.jpg
[inputs]
int(x=10,(0:1:100))
int(y=10,(0:1:100))
int(z=10,(0:1:100))'''

    p1 = Base.Vector(x, 0, 0)
    p2 = Base.Vector(-x, 0, 0)
    p3 = Base.Vector(-x, y, 0)
    p4 = Base.Vector(x, y, 0)

    l1 = Part.Line(p1, p2)
    l2 = Part.Line(p2, p3)
    l3 = Part.Line(p3, p4)
    l4 = Part.Line(p4, p1)

    shape = Part.Shape([l1, l2, l3, l4])

    wire = Part.Wire(shape.Edges)

    face = Part.Face(wire)

    prism = face.extrude(Base.Vector(0,0,z))

    prism.exportStl(file_path)

