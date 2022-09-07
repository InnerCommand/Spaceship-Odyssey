import pygame

class planet:
	def __init__(self, image : pygame.Surface, width : int, height : int, screenWidth : int, screenHeight : int) -> None:
		"""
		The end-goal/planet
		"""

		# Set styling variables
		self.image = pygame.transform.scale(image, (width, height))
		self.width = width
		self.height = height
		self.rect = self.image.get_rect()

		# Set positioning variables
		self.x = screenWidth/2
		self.y = (-1*height)/2
		self.angle = 0

		# Set screen status variables
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

		# Set animation variables
		self.animationStat = {
			"down" : False,
			"up" : False
		}

	def draw(self, surface : pygame.Surface) -> None:
		"""
		Draw planet onto screen
		"""
		surface.blit(pygame.transform.rotate(self.image, self.angle), (self.x-(self.rect.width/2), self.y-(self.rect.height/2)))

	def rotate(self, angle : int) -> None:
		"""
		Updating the rotation the player is facing
		"""

		self.angle += angle
		self.rect = pygame.transform.rotate(self.image, self.angle).get_rect()

	def animateDown(self, surface : pygame.Surface, speed : int = 5) -> None:
		"""
		Animate planet from top of screen to middle
		"""
		self.rotate(5)
		if self.y < self.screenHeight/2:
			self.y += speed

			self.animationStat['down'] = False
		else: self.animationStat['down'] = True

		self.draw(surface)

	def animateUp(self, surface : pygame.Surface, speed : int = 5) -> None:
		"""
		Animate planet from middle of screen back to top
		"""
		self.rotate(5)
		if self.y > (-1*self.height)/2:
			self.y -= speed
			
			self.animationStat['up'] = False
		else: self.animationStat['up'] = True

		self.draw(surface)

	def reset(self) -> None:
		"""
		Resets all variables
		"""
		self.y = 0
		self.animationStat = {
			"down" : False,
			"up" : False
		}