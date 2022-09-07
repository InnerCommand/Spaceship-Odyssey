import pygame
import math

class bullet:
	def __init__(self, screen : pygame.Surface, width : int, height : int, x : int, y : int, screenWidth : int, screenHeight : int, angle : int = 0, color : tuple[int] = (255,255,255)) -> None:
		"""
		The bullet to shoot
		"""
		
		# Set sizing variables
		self.width = width
		self.height = height

		# Set positioning variables
		self.x = x
		self.y = y
		self.angle = angle

		# Set decorational variables
		self.color = color

		# Set screen variables
		self.screen = screen
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

		# Set rectangle
		self.rect = pygame.Rect(x, y, width, height)

	def draw(self):
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect(self.screen, self.color, self.rect)

	def shoot(self, speed = 20) -> bool:
		# Update x and y
		self.y += math.cos(math.radians(self.angle)) * (-1*speed)
		self.x += math.sin(math.radians(self.angle)) * (-1*speed)

		self.draw()

		# Check for bullet hitting edge
		if self.y > self.screenHeight:
			return False
		elif self.y < 0-self.height:
			return False

		if self.x > self.screenWidth:
			return False
		elif self.x < 0-self.width:
			return False

		return True