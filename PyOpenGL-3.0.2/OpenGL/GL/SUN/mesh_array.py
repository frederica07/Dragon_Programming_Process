'''OpenGL extension SUN.mesh_array

This module customises the behaviour of the 
OpenGL.raw.GL.SUN.mesh_array to provide a more 
Python-friendly API

Overview (from the spec)
	
	
	This extension defines a new mesh primitive.
	The primitive can only be used with vertex arrays and cannot be used in
	immediate mode. The application must arrange the vertices in row major format.
	For example if a quad mesh is 4 vertices wide the, vertices in the first
	row are the first 4 vertices and vertices in the second row are vertices 5
	through 8. 

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SUN/mesh_array.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SUN.mesh_array import *
### END AUTOGENERATED SECTION