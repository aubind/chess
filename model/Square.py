#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from Color import *

### Class Square ###

class Square(Color):
	"""docstring for Square"""

	def __init__(self, color):
		Color.__init__(self, color)
		self.__empty = True
		self.__pawn = None

	def __repr__(self):
		return "Square("+ self.getColor() +")"

	def getPawn(self):
		return self.__pawn

	def free(self):
		return self.__empty

# s = Square("b")
# print "s:", s
