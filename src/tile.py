import OpenGL.GL as gl
import random

class Tile:

	def __init__(self, x, y):

		self.loc = (x, y)
		self.color = (random.random(), random.random(), random.random())

	def draw(self):
		gl.glColor3d(self.color[0], self.color[1], self.color[2])
		gl.glRectd(self.loc[0] * 10, self.loc[1] * 10, self.loc[0] * 10 + 10, self.loc[1] * 10 + 10)