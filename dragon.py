#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import os

from jp.ac.kyoto_su.aokilab.dragon.test.unit_test import UnitTest
from jp.ac.kyoto_su.aokilab.dragon.example_model.example import *

TRACE = True

# print(__file__)
a_directory = os.path.dirname(__file__)  # このスクリプトが存在するディレクトリ
a_directory = os.path.abspath(a_directory)  # そのディレクトリを絶対パスにする
# print('***', a_directory, sep=' ')
if not(a_directory in sys.path):  # 当該のディレクトリがサーチパスに含まれていないとき
	sys.path.append(a_directory)  # 当該のディレクトリをサーチパスに加える
	print(sys.path)

def main():
	"""OpenGL立体データを読み込んで描画する。"""
	if TRACE: print(__name__), main.__doc__

	a_model = DragonModel()
	a_model.open()

	a_model = WaspModel()
	a_model.open()
	
	a_model = BunnyModel()
	a_model.open()

	glutMainLoop()

	return 0

if __name__ == '__main__':
	"""
	テストプログラムを実行します。
	"""

	UnitTest()

	sys.exit(main())
	

# end of file