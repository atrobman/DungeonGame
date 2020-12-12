import OpenGL.GL as gl
from .globals import * #pylint: disable=unused-wildcard-import

class Player:

	def __init__(self, x, y):

		self.loc = (0, 0)

	def draw(self):

		gl.glColor3d(1, 1, 1)
		gl.glRectd(
			self.loc[0] * Globals.TILE_SIZE + Globals.TILE_SIZE/8, 
			self.loc[1] * Globals.TILE_SIZE + Globals.TILE_SIZE/8, 
			self.loc[0] * Globals.TILE_SIZE + 7*Globals.TILE_SIZE/8, 
			self.loc[1] * Globals.TILE_SIZE + 7*Globals.TILE_SIZE/8
			)