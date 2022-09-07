import pygame

class button:
	def __init__(self, size : tuple[int], coords : tuple[int], content : str, font : pygame.font, surface : pygame.Surface, color : tuple[int] = (255,255,255), image : pygame.Surface = None, fontColor : tuple[int] = (0,0,0)) -> None:
		"""
		Creates a new button for pygame
		"""

		# Set content and font properties
		self.content = content
		self.font = font
		self.fontColor = fontColor

		# Set sizing and positioning variables
		self.width,self.height = size
		self.x,self.y = coords

		# Set image qualities
		self.image = image
		self.color = color
		
		if image == None:
			self.rect = pygame.Rect(coords, size)
		else:
			self.rect = image.get_rect()

		# Set display variables
		self.surface = surface

	def writeContent(self) -> None:
		"""
		Draw/add content onto surface/button
		"""
		self.surface.blit(self.font.render(self.content, False, self.fontColor), (self.x, self.y))

	def draw(self) -> None:
		"""
		Draw button onto surface
		"""
		if self.image != None:
			self.surface.blit(self.image, (self.x, self.y))
		else:
			pygame.draw.rect(self.surface, self.color, self.rect)

		self.writeContent()

	def detectClick(self, point) -> bool:
		"""
		Check if mouse is hovering on button
		"""

		return self.rect.collidepoint(point)