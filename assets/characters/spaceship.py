import pygame

class spaceship:
	def __init__(self, surface : pygame.Surface, color : tuple[int], screenWidth, screenHeight) -> None:
		# self.image = image
		self.surface = surface
		self.color = color
		self.x = (screenWidth/2)-30
		self.y = (screenHeight/2)-30

	def draw(self) -> None:
		pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x,self.y,30,30))

	def moveForwards(self) -> None:
		self.y -= 5 if self.y > 5 else 0
		