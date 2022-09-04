import pygame
from assets.characters.spaceship import spaceship

# Init
pygame.init()

SCREENWIDTH = 1000
SCREENHEIGHT = 700

surface = pygame.display.set_mode(((SCREENWIDTH, SCREENHEIGHT)))

pygame.display.set_caption('Red Planet')
player = spaceship(pygame.image.load(r'./assets/images/characters/player.png'), 50, 50, SCREENWIDTH, SCREENHEIGHT)

running = True

def setBackground(width, height):
	for y in range(0, height, 500):
		for x in range(0, width, 500):
			surface.blit(pygame.image.load(r'./assets/images/background/background.png'), (x,y))

# Init Variables
BLACK = (0, 0, 0)
FPS = 30
clock = pygame.time.Clock()

moveState = {
	'left' : False,
	'right' : False,
	'up' : False,
	'down' : False
}

# Game loop
while running:
	# Updating frames
	setBackground(SCREENWIDTH, SCREENHEIGHT)
	player.draw(surface)

	# Movements
	if moveState['left'] == True:
		player.moveX(-5)
	if moveState['right'] == True:
		player.moveX(5)
	if moveState['up'] == True:
		player.moveY(-5)
	if moveState['down'] == True:
		player.moveY(5)

	# Check for keypress
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				moveState['up'] = True
			if event.key == pygame.K_RIGHT:
				moveState['right'] = True
			if event.key == pygame.K_LEFT:
				moveState['left'] = True
			if event.key == pygame.K_DOWN:
				moveState['down'] = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				moveState['up'] = False
			if event.key == pygame.K_DOWN:
				moveState['down'] = False
			if event.key == pygame.K_LEFT:
				moveState['left'] = False
			if event.key == pygame.K_RIGHT:
				moveState['right'] = False

	# Updates
	pygame.display.flip()
	clock.tick(FPS)