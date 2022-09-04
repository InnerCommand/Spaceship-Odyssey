import pygame
import math

class spaceship:
	def __init__(self, image : pygame.Surface, width : int, height : int, screenWidth : int, screenHeight : int) -> None:
		image = pygame.transform.scale(image, (width, height))
		self.image = image
		self.rect = image.get_rect()
		self.angle = 0
		self.x = (screenWidth/2)-(self.rect.width/2)
		self.y = (screenHeight-50)-(self.rect.height/2)
		self.width = width
		self.height = height
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

	def draw(self, surface : pygame.Surface) -> None:
		surface.blit(pygame.transform.rotate(self.image, self.angle), (self.x-(self.rect.width/2), self.y-(self.rect.height/2)))

	def move(self, amt : int) -> None:
		self.y += math.cos(math.radians(self.angle)) * (-1*amt)
		self.x += math.sin(math.radians(self.angle)) * (-1*amt)
		if self.y > self.screenHeight-self.height:
			self.y = self.screenHeight-self.height
		elif self.y < 150:
			self.y = 150
		if self.x > self.screenWidth-self.width:
			self.x = self.screenWidth-self.width
		elif self.x < 0:
			self.x = 0

	def rotate(self, angle : int) -> None:
		self.angle += angle
		self.rect = pygame.transform.rotate(self.image, self.angle).get_rect()