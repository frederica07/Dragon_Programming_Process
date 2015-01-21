#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import urllib

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from jp.ac.kyoto_su.aokilab.dragon.mvc.model import OpenGLModel
from jp.ac.kyoto_su.aokilab.dragon.mvc.view import *
from jp.ac.kyoto_su.aokilab.dragon.opengl.triangle import OpenGLTriangle
from jp.ac.kyoto_su.aokilab.dragon.opengl.polygon import OpenGLPolygon

TRACE = True
DEBUG = False

class DragonModel(OpenGLModel):
	"""ドラゴンのモデル。"""

	def __init__(self):
		"""ドラゴンのモデルのコンストラクタ。"""
		if TRACE: print(__name__), self.__init__.__doc__

		super(DragonModel, self).__init__()
		self._eye_point = [-5.5852450791872 , 3.07847342734 , 15.794105252496]
		self._sight_point = [0.27455347776413 , 0.20096999406815 , -0.11261999607086]
		self._up_vector = [0.1018574904194 , 0.98480906061847 , -0.14062775604137]
		self._fovy = self._default_fovy = 12.642721790235

		filename = os.path.join(os.getcwd(), 'dragon.txt')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Dragon/dragon.txt'
			urllib.urlretrieve(url, filename)

		with open(filename, "rU") as a_file:
			while True:
				a_string = a_file.readline()
				if len(a_string) == 0: break
				a_list = a_string.split()
				if len(a_list) == 0: continue
				first_string = a_list[0]
				if first_string == "number_of_vertexes":
					number_of_vertexes = int(a_list[1])
				if first_string == "number_of_triangles":
					number_of_triangles = int(a_list[1])
				if first_string == "end_header":
					get_tokens = (lambda file: file.readline().split())
					collection_of_vertexes = []
					for n_th in range(number_of_vertexes):
						a_list = get_tokens(a_file)
						a_vertex = map(float, a_list[0:3])
						collection_of_vertexes.append(a_vertex)
					index_to_vertex = (lambda index: collection_of_vertexes[index-1])
					for n_th in range(number_of_triangles):
						a_list = get_tokens(a_file)
						indexes = map(int, a_list[0:3])
						vertexes = map(index_to_vertex, indexes)
						a_tringle = OpenGLTriangle(*vertexes)
						self._display_object.append(a_tringle)

		return

	def default_window_title(self):
		"""ドラゴンのウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print(__name__), self.default_window_title.__doc__

		return "Dragon"


class WaspModel(OpenGLModel):
	"""スズメバチのモデル。"""

	def __init__(self):
		"""スズメバチのモデルのコンストラクタ。"""
		if TRACE: print(__name__), self.__init__.__doc__

		super(WaspModel, self).__init__()
		self._eye_point = [-5.5852450791872 , 3.07847342734 , 15.794105252496]
		self._sight_point = [0.19825005531311 , 1.8530999422073 , -0.63795006275177]
		self._up_vector = [0.070077999093727 , 0.99630606032682 , -0.049631725731267]
		self._fovy = self._default_fovy = 41.480099231656

		filename = os.path.join(os.getcwd(), 'wasp.txt')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Wasp/wasp.txt'
			urllib.urlretrieve(url, filename)

		with open(filename, "rU") as a_file:
			while True:
				a_string = a_file.readline()
				if len(a_string) == 0: break
				a_list = a_string.split()
				if len(a_list) == 0: continue
				first_string = a_list[0]
				if first_string == "number_of_vertexes":
					number_of_vertexes = int(a_list[1])
				if first_string == "number_of_polygons":
					number_of_polygons = int(a_list[1])
				if first_string == "end_header":
					get_tokens = (lambda file: file.readline().split())
					collection_of_vertexes = []
					for n_th in range(number_of_vertexes):
						a_list = get_tokens(a_file)
						a_vertex = map(float, a_list[0:3])
						collection_of_vertexes.append(a_vertex)
					index_to_vertex = (lambda index: collection_of_vertexes[index-1])
					for n_th in range(number_of_polygons):
						a_list = get_tokens(a_file)
						number_of_indexes = int(a_list[0])
						index = number_of_indexes + 1
						indexes = map(int, a_list[1:index])
						vertexes = map(index_to_vertex, indexes)
						rgb_color = map(float, a_list[index:index+3])
						a_polygon = OpenGLPolygon(vertexes, rgb_color)
						self._display_object.append(a_polygon)

		return

	def default_view_class(self):
		"""スズメバチのモデルを表示するデフォルトのビューのクラスを応答する。"""
		if TRACE: print(__name__), self.default_view_class.__doc__

		return WaspView

	def default_window_title(self):
		"""スズメバチのウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print(__name__), self.default_window_title.__doc__

		return "Wasp"


class BunnyModel(OpenGLModel):
	"""うさぎのモデル。"""

	def __init__(self):
		"""うさぎのモデルのコンストラクタ。"""
		if TRACE: print(__name__), self.__init__.__doc__

		super(BunnyModel, self).__init__()

		filename = os.path.join(os.getcwd(), 'bunny.ply')
		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			url = 'http://www.cc.kyoto-su.ac.jp/~atsushi/Programs/Bunny/bunny.ply'
			urllib.urlretrieve(url, filename)

		with open(filename, "rU") as a_file:
			while True:
				a_string = a_file.readline()
				if len(a_string) == 0: break
				a_list = a_string.split()
				if len(a_list) == 0: continue
				first_string = a_list[0]
				if first_string == "element":
					second_string = a_list[1]
					if second_string == "vertex":
						number_of_vertexes = int(a_list[2])
					if second_string == "face":
						number_of_faces = int(a_list[2])
				if first_string == "end_header":
					get_tokens = (lambda file: file.readline().split())
					collection_of_vertexes = []
					for n_th in range(number_of_vertexes):
						a_list = get_tokens(a_file)
						a_vertex = map(float, a_list[0:3])
						collection_of_vertexes.append(a_vertex)
					index_to_vertex = (lambda index: collection_of_vertexes[index])
					for n_th in range(number_of_faces):
						a_list = get_tokens(a_file)
						indexes = map(int, a_list[1:4])
						vertexes = map(index_to_vertex, indexes)
						a_tringle = OpenGLTriangle(*vertexes)
						self._display_object.append(a_tringle)
				if first_string == "comment":
					second_string = a_list[1]
					if second_string == "eye_point_xyz":
						self._eye_point = map(float, a_list[2:5])
					if second_string == "sight_point_xyz":
						self._sight_point = map(float, a_list[2:5])
					if second_string == "up_vector_xyz":
						self._up_vector = map(float, a_list[2:5])
					if second_string == "zoom_height" and a_list[3] == "fovy":
						self._fovy = self._default_fovy = float(a_list[4])

		return

	def default_view_class(self):
		"""うさぎのモデルを表示するデフォルトのビューのクラスを応答する。"""
		if TRACE: print(__name__), self.default_view_class.__doc__

		return BunnyView

	def default_window_title(self):
		"""うさぎのウィンドウのタイトル(ラベル)を応答する。"""
		if TRACE: print(__name__), self.default_window_title.__doc__

		return "Stanford Bunny"

# end of file