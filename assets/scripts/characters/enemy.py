import pygame
import math
from assets.scripts.characters.spaceship import spaceship
from assets.scripts.assets.bullet import bullet

class enemy(spaceship):
	def __init__(self, image : pygame.Surface, x : int, y : int, width : int, height : int, screenWidth : int, screenHeight : int) -> None:
		"""
		Set variables
		"""
		
		# Set enemy details
		self.image = pygame.transform.scale(image, (width, height))
		self.rect = image.get_rect()

		# Set position of enemy
		self.x = x
		self.y = y
		self.angle = 0

		# Get details of pygame main board
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

	def moveToPlayer(self, surface: pygame.Surface, player : spaceship, speed : int = 20):
		diffX = player.x - self.x
		diffY = player.y - self.y
		self.x += diffX/speed
		self.y += diffY/speed
		self.angle = (180 if player.y >= self.y else 0)+math.degrees(math.atan(diffX / diffY))
		self.rect = pygame.transform.rotate(self.image, self.angle).get_rect()
		self.draw(surface)