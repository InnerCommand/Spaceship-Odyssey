import pygame
import math
from assets.scripts.assets.bullet import *

class spaceship:
	def __init__(self, image : pygame.Surface, width : int, height : int, screenWidth : int, screenHeight : int) -> None:
		"""
		The player
		"""

		# Update and set images
		image = pygame.transform.scale(image, (width, height))
		self.image = image
		self.rect = image.get_rect()

		# Set all positioning variables
		self.angle = 0
		self.x = (screenWidth/2)-(self.rect.width/2)
		self.y = (screenHeight-50)-(self.rect.height/2)

		# Set ship sizing
		self.width = width
		self.height = height

		# Add total screen sizes for future reference
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

		# Shooting variables
		self.shootState = False
		self.shooter = []

	def draw(self, surface : pygame.Surface) -> None:
		"""
		This is to draw the player onto the screen
		"""
		surface.blit(pygame.transform.rotate(self.image, self.angle), (self.x-(self.rect.width/2), self.y-(self.rect.height/2)))

	def move(self, amt : int) -> None:
		"""
		To move the player
		"""

		# Update x and y based on movement
		self.y += math.cos(math.radians(self.angle)) * (-1*amt)
		self.x += math.sin(math.radians(self.angle)) * (-1*amt)

		# Check to make sure user is not hitting edges
		if self.y > self.screenHeight-(self.height/2):
			self.y = self.screenHeight-(self.height/2)
		elif self.y < 0+(self.height/2):
			self.y = 0+(self.height/2)

		if self.x > self.screenWidth-(self.width/2):
			self.x = self.screenWidth-(self.width/2)
		elif self.x < 0+(self.width/2):
			self.x = 0+(self.width/2)

	def rotate(self, angle : int) -> None:
		"""
		Updating the rotation the player is facing
		"""

		self.angle += angle
		self.rect = pygame.transform.rotate(self.image, self.angle).get_rect()

	def shoot(self, surface : pygame.Surface, initial = False) -> None:
		"""
		Shooting bullets with bullet class
		"""
		if initial: self.shooter.append(bullet(surface, 5, 5, self.x, self.y, self.screenWidth, self.screenHeight, angle=self.angle))

		for i in self.shooter:
			self.shootState = i.shoot(25)

			if self.shootState == False:
				del i

	def resize(self, screenWidth : int, screenHeight : int) -> None:
		"""
		Deal with resize of screen
		"""

		# Update screen width and height values
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

		# Check if user is off edges, if so, relocate user
		if self.y > self.screenHeight-(self.height/2):
			self.y = self.screenHeight-(self.height/2)
		elif self.y < 0+(self.height/2):
			self.y = 0+(self.height/2)

		if self.x > self.screenWidth-(self.width/2):
			self.x = self.screenWidth-(self.width/2)
		elif self.x < 0+(self.width/2):
			self.x = 0+(self.width/2)

	def checkHit(self, enemy) -> bool:
		"""
		Check if bullets have hit enemy
		"""
		returnVal = False

		# Check if all bullets are touching enemy
		for i in self.shooter:
			if (enemy.x-enemy.width <= i.x <= enemy.x+enemy.width) and (enemy.y-enemy.height <= i.y <= enemy.y+enemy.height):
				returnVal = True
		
		return returnVal