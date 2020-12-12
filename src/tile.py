import OpenGL.GL as gl
import random
from .globals import * #pylint: disable=unused-wildcard-import

class Tile:

	def __init__(self, x, y):

		self.loc = (x, y)
		self.color = (random.random(), random.random(), random.random())

	def draw(self):

		gl.glColor3d(self.color[0], self.color[1], self.color[2])
		gl.glRectd(
			self.loc[0] * Globals.TILE_SIZE, 
			self.loc[1] * Globals.TILE_SIZE, 
			self.loc[0] * Globals.TILE_SIZE + Globals.TILE_SIZE, 
			self.loc[1] * Globals.TILE_SIZE + Globals.TILE_SIZE
			)