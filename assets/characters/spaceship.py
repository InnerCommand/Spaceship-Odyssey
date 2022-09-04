import pygame

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
		# self.rect = pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x,self.y,30,30))
		surface.blit(pygame.transform.rotate(self.image, self.angle), (self.x-(self.rect.width/2), self.y-(self.rect.height/2)))

	def move(self, yAmt : int) -> None:
		self.y += yAmt
		if self.y > self.screenHeight-self.height:
			self.y = self.screenHeight-self.height
		elif self.y < 150:
			self.y = 150

	def rotate(self, angle : int) -> None:
		# self.x += xAmt
		# if self.x > self.screenWidth-self.width:
		# 	self.x = self.screenWidth-self.width
		# elif self.x < 0:
		# 	self.x = 0
		self.angle += angle
		self.rect = pygame.transform.rotate(self.image, self.angle).get_rect()