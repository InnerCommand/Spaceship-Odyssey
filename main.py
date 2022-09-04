import pygame
from assets.characters.spaceship import spaceship

# Init
pygame.init()

SCREENWIDTH = 1000
SCREENHEIGHT = 700

surface = pygame.display.set_mode(((SCREENWIDTH, SCREENHEIGHT)))

pygame.display.set_caption('Red Planet')
player = spaceship(surface, (255,0,0), SCREENWIDTH, SCREENHEIGHT)

running = True

# Init Colors
BLACK = (0, 0, 0)

# Game loop
while running:
	surface.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player.moveForwards()
				print('move')

	player.draw()