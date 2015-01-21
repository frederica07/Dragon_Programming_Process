#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from jp.ac.kyoto_su.aokilab.dragon.mvc.model import OpenGLModel
from jp.ac.kyoto_su.aokilab.dragon.mvc.view import OpenGLView
from jp.ac.kyoto_su.aokilab.dragon.mvc.controller import OpenGLController
from jp.ac.kyoto_su.aokilab.dragon.opengl.triangle import OpenGLTriangle

class UnitTest(object):
	"""
	単体テストのためのクラスです。
	"""

	def __init__(self):

		# 単体テスト(各レシーバに対してunit_test()というメッセージを送っている)
		OpenGLModel.unit_test()
		OpenGLView.unit_test()
		OpenGLController.unit_test()
		OpenGLTriangle.unit_test()

		return

# end of file