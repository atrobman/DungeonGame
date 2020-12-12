import OpenGL.GL as gl
from .tile import Tile
from .player import Player
from .globals import * #pylint: disable=unused-wildcard-import

class Game:

	def __init__(self):
		
		self.state = 0
		self.player = Player(1, 1)
		self.map = []
		self.loc = (0, 0)
		self.enemies = []
		self.items = []
		self.level = 1

		for i in range(10):
			row = []
			for j in range(5):
				row.append( Tile(i, j) )
			self.map.append(row)

	def draw(self):

		gl.glPushMatrix()
		
		gl.glTranslated(
			Globals.WINDOW_WIDTH/2 - Globals.TILE_SIZE / 2 - self.player.loc[0] * Globals.TILE_SIZE,
			Globals.WINDOW_HEIGHT/2 - Globals.TILE_SIZE / 2 - self.player.loc[1] * Globals.TILE_SIZE,
			0
			)

		for row in self.map:
			for tile in row:
				tile.draw()

		self.player.draw()
	
		gl.glPopMatrix()