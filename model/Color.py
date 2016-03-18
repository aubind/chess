#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

### Class Color ###

class Color(object):
	"""docstring for Color"""

	def __init__(self, arg):
		if "w" in arg or "W" in arg:
			self.__white = True
			self.__black = False
			self.__color = "White"
		else:
			self.__white = False
			self.__black = True
			self.__color = "Black"

	def __repr__(self):
		return "Color(" + self.__color + ")"

	def switchColor(self):
		if self.__black == True:
			self.__white = True
			self.__black = False
			self.__color = "White"
		else:
			self.__white = False
			self.__black = True
			self.__color = "Black"

	def getColor(self):
		return self.__color

	def isBlack(self):
		return self.__black

	def isWhite(self):
		return self.__white

c = Color("w")
# print "white:", c
c.switchColor()
# print "black:", c
