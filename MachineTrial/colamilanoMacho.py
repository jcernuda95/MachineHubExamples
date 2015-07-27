#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
FREECADPATH = '/usr/lib/freecad/lib/'
sys.path.append(FREECADPATH)

from FreeCAD import Base  #importing freecad base and part require for every 3d model creation
import Part
from math import tan, pi  #importing the math library available by default.

def machinebuilder(x, y, z,smallSide, angle, depth, file_path):
    '''
[doc]
-title-
male dovetail
-description-
Creation of a parametric male dovetail
-images_url-
http://www.dovetailshutters.com/images/the_difference_dovetail_joint.gif
http://chestofbooks.com/home-improvement/woodworking/Course-Boys/images/No-13-Dovetail-Joint-20.jpg
[inputs]
int(x=10,(0:1:100))
int(y=10,(0:1:100))
int(z=10,(0:1:100))
int(smallSide=4,(0:1:100))
int(angle=45,(0:1:100))
int(depth=5,(0:1:100)) 
    '''
    #TODO: redefine the parameterlimits
    
    angle = angle * pi / 180 #the angle is introduce in grades, the math library require it in radians
    
    #Definition of the 4 points that define the initial sketch
    p1 = Base.Vector(x + smallSide/2, 0, 0)
    p2 = Base.Vector(x - smallSide/2, 0, 0)
    p3 = Base.Vector((x + smallSide) + depth / tan(angle), depth, 0)
    p4 = Base.Vector((x - smallSide) - depth / tan(angle), depth, 0)

    #DEfinition of the segments that join the points, in this case simple lines
    l1 = Part.Line(p1, p2)
    l2 = Part.Line(p1, p3)
    l3 = Part.Line(p2, p4)
    l4 = Part.Line(p3, p4)

    #we tell freecad all this lines form a groups
    shape = Part.Shape([l1, l2, l3, l4])

    #we generate the wire that join them
    wire = Part.Wire(shape.Edges)

    #we generate a face around the wire
    face = Part.Face(wire)

    #we extrude that face in the z axis
    c = face.extrude(Base.Vector(0,0,2))

    #-- Export the file
    c.exportStl(file_path)
