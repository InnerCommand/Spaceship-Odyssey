import pygame
import time
from assets.scripts.characters.spaceship import spaceship
from assets.scripts.characters.enemy import enemy, trackingEnemy
from assets.scripts.assets.planet import planet

# Init
pygame.init()

surface = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))

SCREENWIDTH, SCREENHEIGHT = pygame.display.get_surface().get_size()

if SCREENHEIGHT > 700:
	surface = pygame.display.set_mode((pygame.display.Info().current_w, 700))
	SCREENHEIGHT = 700

pygame.display.set_caption('Spaceship Odyssey')

# Create new characters
player = spaceship(pygame.image.load(r'./assets/images/characters/player.png'), 50, 50, SCREENWIDTH, SCREENHEIGHT)
enemies = [enemy(pygame.image.load(r'./assets/images/characters/enemy.png'), 30, SCREENWIDTH/2+180, 60, 70, 92, SCREENWIDTH, SCREENHEIGHT, player)] 
trackingEnemies = [trackingEnemy(pygame.image.load(r'./assets/images/characters/enemyTracker.png'),10, SCREENWIDTH/2, 60, 70, 92, SCREENWIDTH, SCREENHEIGHT, player)]

running = True

y1s1 = 0
y2s1 = -1*SCREENHEIGHT
y1s2 = 0
y2s2 = -1*SCREENHEIGHT

def setBackground(width : int, height : int, screen : pygame.Surface) -> None:
	# To set the background to a 'tiled' version of the background, also to make it move

	screen.fill((10,10,10))

	global y1s1
	global y2s1
	global y1s2
	global y2s2

	y1s1 += 5
	y2s1 += 5
	y1s2 += 3
	y2s2 += 3

	for x in range(0,width,500):
		surface.blit(pygame.image.load(r'./assets/images/background/stars1.png'), (x,y2s1))
		surface.blit(pygame.image.load(r'./assets/images/background/stars1.png'), (x,y1s1))
		surface.blit(pygame.image.load(r'./assets/images/background/stars2.png'), (x,y1s2))
		surface.blit(pygame.image.load(r'./assets/images/background/stars2.png'), (x,y2s2))

	if y1s1 > height:
		y1s1 = -1*height
	if y2s1 > height:
		y2s1 = -1*height
	if y1s2 > height:
		y1s2 = -1*height
	if y2s2 > height:
		y2s2 = -1*height

# Init Variables
BLACK = (0, 0, 0)
FPS = 30
ACCELERATION = 12
ROTATION = 10
TIMERINIT = 10
timerSpeed = 30
clock = pygame.time.Clock()

# All movestates
moveState = {
	'left' : False,
	'right' : False,
	'up' : False,
	'shoot' : False
}
#timer
timer = time.time()

# Game loop
while running:
	# Updating frames
	setBackground(SCREENWIDTH, SCREENHEIGHT, surface)

	# Shooting
	if player.shootState == True:
		player.shoot(surface)

	# Draw player
	player.draw(surface)

	removedEnemies = []
	for i in enemies:
		i.moveToPlayer(surface)
		player.checkHit(i)
		if player.checkHit(i):
			removedEnemies.append(i)
	enemies = [i for i in enemies if i not in removedEnemies]

	removedEnemies = []
	for i in trackingEnemies:
		i.moveToPlayer(surface, player)
		if player.checkHit(i):
			removedEnemies.append(i)
	trackingEnemies = [i for i in trackingEnemies if i not in removedEnemies]

	# Rectangle side timer
	current_time = time.time()
	time_past = timer - current_time
	amtMove = time_past*timerSpeed

	pygame.draw.rect(surface, (0, 100, 0), pygame.Rect((45, 190), (50, 290)))
	print(TIMERINIT-amtMove)
	if abs(TIMERINIT-amtMove) <= 280:
		pygame.draw.rect(surface, (0, 255, 0), pygame.Rect((50, (475-TIMERINIT)+amtMove), (40, TIMERINIT-amtMove)))
	else:
		pygame.draw.rect(surface, (0, 255, 0), pygame.Rect((50, 195), (40, 280)))

	# Movements
	if moveState['left'] == True:
		player.rotate(ROTATION)
	if moveState['right'] == True:
		player.rotate(-1*ROTATION)
	if moveState['up'] == True:
		player.move(ACCELERATION)
	if moveState['shoot'] == True:
		player.shoot(surface, True)

	# Check for keypress
	for event in pygame.event.get():
		# Check if user quit
		if event.type == pygame.QUIT:
			running = False

		# Check for user keypresses
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				moveState['up'] = True
			if event.key == pygame.K_RIGHT:
				moveState['right'] = True
			if event.key == pygame.K_LEFT:
				moveState['left'] = True

			if event.key == pygame.K_SPACE:
				moveState['shoot'] = True

		# Remove movements when key no longer pressed
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				moveState['up'] = False
			if event.key == pygame.K_LEFT:
				moveState['left'] = False
			if event.key == pygame.K_RIGHT:
				moveState['right'] = False

			if event.key == pygame.K_SPACE:
				moveState['shoot'] = False

		# Check if game has resized
		if event.type == pygame.VIDEORESIZE:
			SCREENWIDTH, SCREENHEIGHT = pygame.display.get_surface().get_size()
			player.resize(SCREENWIDTH, SCREENHEIGHT)

	# Updates
	pygame.display.flip()
	clock.tick(FPS)