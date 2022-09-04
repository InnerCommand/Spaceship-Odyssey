import pygame

class spaceship:
	def __init__(self, image : pygame.Surface, width : int, height : int, screenWidth : int, screenHeight : int) -> None:
		image = pygame.transform.scale(image, (width, height))
		self.image = image
		self.x = (screenWidth/2)-(width/2)
		self.y = (screenHeight-50)-(height/2)
		self.width = width
		self.height = height
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

	def draw(self, surface : pygame.Surface) -> None:
		# self.rect = pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x,self.y,30,30))
		surface.blit(self.image, (self.x, self.y))

	def moveY(self, yAmt : int) -> None:
		self.y += yAmt
		if self.y > self.screenHeight-self.height:
			self.y = self.screenHeight-self.height
		elif self.y < 150:
			self.y = 150
	def moveX(self, xAmt : int) -> None:
		self.x += xAmt
		if self.x > self.screenWidth-self.width:
			self.x = self.screenWidth-self.width
		elif self.x < 0:
			self.x = 0