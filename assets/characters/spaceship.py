import pygame

class spaceship(pygame.Surface):
	def __init__(self, surface : pygame.Surface, color : tuple[int], screenWidth, screenHeight) -> None:
		# self.image = image
		self.surface = surface
		self.color = color
		self.x = (screenWidth/2)-30
		self.y = (screenHeight-50)-30
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

	def draw(self) -> None:
		rect = pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x,self.y,30,30))

	def moveY(self, yAmt) -> None:
		self.y += yAmt
		if self.y > self.screenHeight-30:
			self.y = self.screenHeight-30
		elif self.y < self.screenHeight-150:
			self.y = self.screenHeight-150
	def moveX(self, xAmt) -> None:
		self.x += xAmt
		if self.x > self.screenWidth-30:
			self.x = self.screenWidth-30
		elif self.x < 0:
			self.x = 0