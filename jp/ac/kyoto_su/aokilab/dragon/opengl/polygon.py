#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

DEBUG = False

class OpenGLPolygon(object):
	"""OpenGL多角形。"""

	def __init__(self, vertexes, rgb):
		"""OpenGL多角形のコンストラクタ。"""
		if DEBUG: print(__name__), self.__init__.__doc__

		self._vertexes = vertexes
		self._rgb = rgb

		x = 0.0
		y = 0.0
		z = 0.0
		length = len(vertexes)
		for i in range(0, length):
			j = (i + 1) % length
			k = (i + 2) % length
			ux, uy, uz = map((lambda each1, each2: each1 - each2), vertexes[j], vertexes[i])
			vx, vy, vz = map((lambda each1, each2: each1 - each2), vertexes[k], vertexes[j])
			x = x + (uy * vz - uz * vy)
			y = y + (uz * vx - ux * vz)
			z = z + (ux * vy - uy * vx)
		normal_vector = [x, y, z]
		distance = sum(map((lambda each: each * each), normal_vector)) ** 0.5
		self._normal_unit_vector = map((lambda vector: vector / distance), normal_vector)

		return

	def rendering(self):
		"""OpenGL多角形をレンダリングする。"""
		if DEBUG: print(__name__), self.rendering.__doc__

		glColor4d(self._rgb[0], self._rgb[1], self._rgb[2], 1.0)
		glBegin(GL_POLYGON)
		glNormal3fv(self._normal_unit_vector)
		for vertex in self._vertexes:
			glVertex3fv(vertex)
		glEnd()

		return

	@classmethod
	def unit_test(a_class):
		"""
		このクラスおよびサブクラスの単体テストのためのプログラムです。
		"""
		# print(__file__)
		a_name = a_class.__name__

		# print('\n*** Unit Test：{0} ***'.format(a_name))

		return

# end of file