import pygame
import math
from assets.scripts.characters.spaceship import spaceship
from assets.scripts.assets.bullet import bullet

class enemy(spaceship):
	def __init__(self, image : pygame.Surface, speed : int, x : int, y : int, width : int, height : int, screenWidth : int, screenHeight : int, player : spaceship) -> None:
		"""
		Enemy ship
		"""
		
		# Set enemy details
		self.image = pygame.transform.scale(image, (width, height))
		self.rect = image.get_rect()
		self.speed = speed
		self.width = width
		self.height = height

		# Set position of enemy
		self.x = x
		self.y = y

		# Set stats of player's current position
		self.playerX = player.x
		self.playerY = player.y
		self.playerAngle = player.angle

		# Calculate the distance difference between the player and the enemy
		self.diffX = (self.playerX - self.x)/speed
		self.diffY = (self.playerY - self.y)/speed

		# Make enemy face player
		self.angle = (180 if self.playerY >= self.y else 0)+math.degrees(math.atan(self.diffX / self.diffY))

		# Get details of pygame main board
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

		# Shooting variables
		self.shootState = False
		self.shooter = []

	def moveToPlayer(self, surface: pygame.Surface) -> None:
		"""
		Follow the player's direction on spawn
		"""

		# Make the enemy move towards the player with the set speed
		self.x += self.diffX
		self.y += self.diffY
		self.rect = pygame.transform.rotate(self.image, self.angle).get_rect()

		# Draw the enemy
		self.draw(surface)

class trackingEnemy(enemy):
	def moveToPlayer(self, surface: pygame.Surface, player : spaceship) -> None:
		"""
		Follow player (direction and location) until death
		"""

		# Calculate the distance difference between the player and the enemy
		diffX = player.x - self.x
		diffY = player.y - self.y

		# Make the enemy move towards the player with the set speed
		self.x += diffX/self.speed
		self.y += diffY/self.speed

		# Make the enemy face the player
		self.angle = (180 if player.y >= self.y else 0)+math.degrees(math.atan(diffX / diffY))
		self.rect = pygame.transform.rotate(self.image, self.angle).get_rect()

		# Draw the enemy
		self.draw(surface)