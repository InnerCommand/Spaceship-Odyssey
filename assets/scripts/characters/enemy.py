import pygame
from assets.scripts.characters.spaceship import spaceship
from assets.scripts.assets.bullet import bullet

class enemy(spaceship):
	def __init__(self, surface : pygame.Surface, image : pygame.Surface, x : int, y : int, width : int, height : int, screenWidth : int, screenHeight : int) -> None:
		"""
		Set variables
		"""
		
		# Set enemy details
		self.image = pygame.transform.scale(image, (width, height))

		# Set position of enemy
		self.x = x
		self.y = y

		# Get details of pygame main board
		self.surface = surface
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

	def moveToPlayer(self, player : spaceship):
		pass