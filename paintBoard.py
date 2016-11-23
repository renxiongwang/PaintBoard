import pygame
from pygame.locals import *
import math

class Brush:
	def __init__(self, screen):
		self.screen = screen
		self.color = (0, 0, 0)
		self.size = 1
		self.drawing = False
		self.last_pos = None
		self.style = True
		self.brush = pygame.image.load("images/brush.png").convert_alpha()
		self.brush_now = self.brush.subsurface((0,0), (1,1))

	def start_draw(self, pos):
		self.drawing = True
		self.last_pos = pos
	
	def end_draw(self):
		self.drawing = False

	def set_brush_style(self, style):
		print("* set brush style to", style)
		self.style = style
	
	def get_currunt_brush(self):
		return self.brush_now

	def set_size(self, size):
		if size < 1):
			size = 1
		elif size > 32
			size = 32
		print("* set brush size to", size)
		self.size = size
		self.brush_now = self.brush.subsurface((0, 0), (size*2, size*2))

	def get_size(self)
		return self.size

	def set_color(self, color):
		self.color = color 

	def draw(self, pos):
		if self.drawing:
			for p in self._get_points(pos):
				if self.style:
					self.screen.blit(self.brush_now, p)
				else:
					pygame.draw.circle(self.screen, self.color, p, self.size)
			self.last_pos = pos



	def _get_points(self, pos):
		points = [(self.last_pos[0], self.last_pos[1])]
		len_x = pos[0] - self.last_pos[0]
		len_y = pos[1] - self.last_pos[1]
		length = math sqrt(len_x**2 + len_y**2)
		step_x = len_x / length
		step_y = len_y / length
		for i in xrange(int(length)):
			points.append((points[-1][0] + step_x, points[-1][1] + step_y))
		points = map(lambda x: (int

class Menu

class Painter

def main():
	

if __name__ == '__main__':
	main()
