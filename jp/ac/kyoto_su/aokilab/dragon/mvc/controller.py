#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

TRACE = True

class OpenGLController(object):
	"""OpenGLコントローラ。"""

	def __init__(self, a_view):
		"""OpenGLコントローラのコンストラクタ。"""
		if TRACE: print(__name__), self.__init__.__doc__

		self._model = a_view._model
		self._view = a_view

		return

	def close(self):
		"""ウィンドウを閉じる際の処理をする。"""
		if TRACE: print(__name__), self.close.__doc__

		sys.exit(0)

		return

	def keyboard(self, key, x, y):
		"""キーボードを処理する。"""
		if TRACE: print(__name__), self.keyboard.__doc__

		if key in "qQ\33":
			sys.exit(0)
		if key == 'r' or key == 'R':
			self._view._angle_x = 0.0
			self._view._angle_y = 0.0
			self._view._angle_z = 0.0
			self._model._fovy = self._model._default_fovy
		if key == 'x':
			self._view._angle_x += 1.0
		if key == 'y':
			self._view._angle_y += 1.0
		if key == 'z':
			self._view._angle_z += 1.0
		if key == 'X':
			self._view._angle_x -= 1.0
		if key == 'Y':
			self._view._angle_y -= 1.0
		if key == 'Z':
			self._view._angle_z -= 1.0
		if key == 's':
			self._model._fovy += 1.0
		if key == 'S':
			self._model._fovy -= 1.0

		glutPostRedisplay()

		return

	def motion(self, x, y):
		"""マウスボタンを押下しながらの移動を処理する。"""
		if TRACE: print(__name__), self.motion.__doc__

		print("motion at (" + str(x) + ", " + str(y) + ")")

		return

	def mouse(self, button, state, x, y):
		"""マウスボタンを処理する。"""
		if TRACE: print(__name__), self.mouse.__doc__

		if button == GLUT_LEFT_BUTTON:
			print("left"),
		elif button == GLUT_MIDDLE_BUTTON:
			print("middle")
		elif button == GLUT_RIGHT_BUTTON:
			print("right"),
		else:
			pass

		print("button is"),

		if state == GLUT_DOWN:
			print("down"),
		elif state == GLUT_UP:
			print("up"),
		else:
			pass

		print("at (" + str(x) + ", " + str(y) + ")")

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