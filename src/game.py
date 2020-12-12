import OpenGL.GL as gl
from .tile import Tile

class Game:

	def __init__(self):
		
		self.state = 0
		self.player = None
		self.map = []
		self.pos = (0, 0)
		self.enemies = []
		self.items = []
		self.level = 1

		for i in range(10):
			row = []
			for j in range(5):
				row.append( Tile(i, j) )
			self.map.append(row)

	def draw(self):
		for row in self.map:
			for tile in row:
				tile.draw()