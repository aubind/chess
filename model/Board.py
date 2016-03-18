#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from Square import *

### Class Board ###
class Board(object):
	"""docstring for Board"""

	def __init__(self):

		super(Board, self).__init__()

		self.__tab = [] # List containing the squares of the board
		color = "black" # first color for A1

		# Computation of the color for each square of the board
		for i in range(8):
			if "white" in color:
				color = "black"
			else:
				color = "white"
			for j in range(8):
				if "white" in color:
					color = "black"
				else:
					color = "white"
				self.__tab.append(Square(color))

	def __repr__(self):
		i = 0
		var = ""
		for square in self.__tab:
			if i==0 or ((i)%8)==0:
				if i == 0:
					var += "  +---+---+---+---+---+---+---+---+\n8"
				else:
					var += " |\n  +---+---+---+---+---+---+---+---+\n" + str(8-(i/8))
			if square.free():
				key = " "
			var += " | " + key
			i += 1
		var += " |\n  +---+---+---+---+---+---+---+---+\n"
		var += "    A   B   C   D   E   F   G   H "
		return var


b = Board()
print(b)
