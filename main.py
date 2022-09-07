import pygame
import time
import random
from assets.scripts.characters.spaceship import spaceship
from assets.scripts.characters.enemy import enemy, trackingEnemy
from assets.scripts.assets.planet import planet

# Init
pygame.init()
pygame.font.init()

# Set screen
surface = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))

# Get screen sizing
SCREENWIDTH, SCREENHEIGHT = pygame.display.get_surface().get_size()

if SCREENHEIGHT > 700:
	surface = pygame.display.set_mode((pygame.display.Info().current_w, 700))
	SCREENHEIGHT = 700

# Set title of window
pygame.display.set_caption('Spaceship Odyssey')

# Create new characters
player = spaceship(pygame.image.load(r'./assets/images/characters/player.png'), 50, 50, SCREENWIDTH, SCREENHEIGHT)
enemies = [] 
trackingEnemies = []

# Set player health stats
health = 100
dmgTaken = 3

# Set level variables
level = 1
levelNotificationY = 0

# Set wait time for enemy spawn
waitTime = .5

# Planet variables
redPlanet = planet(pygame.image.load(r'./assets/images/items/planet.png'), 250, 250, SCREENWIDTH, SCREENHEIGHT)
planetPause = True

# Set enemies to no longer pause
pauseEnemies = False

# Set running variable for game loop
running = True

# Set font variables
font = pygame.font.Font(r'./assets/fonts/FONT.ttf', 30)

# Set background variables
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

def showLevelText(surface : pygame.Surface, level : int, speed : int = 5) -> bool:
	# To display the level text

	font = pygame.font.Font(r'./assets/fonts/FONT.ttf', 50)

	global levelNotificationY

	text = font.render(f'Level {level+1}', True, (255,255,255))
	surface.blit(text, text.get_rect(center=(SCREENWIDTH/2, levelNotificationY)))

	if levelNotificationY < SCREENHEIGHT:
		levelNotificationY += speed
	else:
		levelNotificationY = 0
		return True

	return False

# Set speeds of how things will run
FPS = 30
ACCELERATION = 12
ROTATION = 10
TIMERINIT = 10
timerSpeed = 20

# Set color variables
WHITE = (255,255,255)
BLACK = (0,0,0)

# Set clock
clock = pygame.time.Clock()

# All movestates
moveState = {
	'left' : False,
	'right' : False,
	'up' : False,
	'shoot' : False
}

# Timer
timer = time.time()
enemyTimer = time.time()

# Starting page
startingPageShow = True

# Create values for starting page
titleFont = pygame.font.Font(r'./assets/fonts/FONT.ttf', 50)

# Starting page loop
while startingPageShow:
	# Add starting page background to screen
	setBackground(SCREENWIDTH, SCREENHEIGHT, surface)

	# Add title
	title = titleFont.render("Spaceship Odyssey", False, WHITE)
	surface.blit(title, title.get_rect(center=(SCREENWIDTH/2, 50)))

	# Add start instructions
	startInstructions = font.render("[Click anywhere to start]", False, WHITE)
	surface.blit(startInstructions, startInstructions.get_rect(center=(SCREENWIDTH/2, SCREENHEIGHT-50)))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			startingPageShow = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			startingPageShow = False

	# Update frames
	pygame.display.flip()
	clock.tick(FPS)

# Game loop
while running:
	# Updating frames
	setBackground(SCREENWIDTH, SCREENHEIGHT, surface)

	# Shooting
	if player.shootState == True:
		player.shoot(surface)

	# Draw player
	player.draw(surface)

	# Update and draw enemies
	removedEnemies = []
	for i in enemies:
		i.moveToPlayer(surface)
		i.shoot(surface, True)
		player.checkHit(i)
		if i.checkHit(player):
			health -= dmgTaken
		if player.checkHit(i):
			removedEnemies.append(i)
	enemies = [i for i in enemies if i not in removedEnemies]

	removedEnemies = []
	for i in trackingEnemies:
		i.moveToPlayer(surface, player)
		i.shoot(surface, True)
		if i.checkHit(player):
			health -= dmgTaken
		if player.checkHit(i):
			removedEnemies.append(i)
	trackingEnemies = [i for i in trackingEnemies if i not in removedEnemies]

	# Movements
	if moveState['left'] == True:
		player.rotate(ROTATION)
	if moveState['right'] == True:
		player.rotate(-1*ROTATION)
	if moveState['up'] == True:
		player.move(ACCELERATION)
	if moveState['shoot'] == True:
		player.shoot(surface, True)

	# Deal with timer
	current_time = time.time()
	time_past = timer - current_time
	amtMove = time_past*timerSpeed
	enemyTimePast = current_time - enemyTimer

	# Spawn enemies based on time
	if enemyTimePast >= waitTime and not pauseEnemies:
		# Spawn normal enemies
		amtEnemies = random.randint(1,3)
		for i in range(amtEnemies):
			enemies.append(enemy(pygame.image.load(r'./assets/images/characters/enemy.png'),20,random.randint(-92,SCREENWIDTH),0,70,92,SCREENWIDTH,SCREENHEIGHT,player))
		
		# Spawn tracking enemies
		amtEnemies = random.randint(0,2)
		for i in range(amtEnemies):
			trackingEnemies.append(trackingEnemy(pygame.image.load(r'./assets/images/characters/enemyTracker.png'),20,random.randint(-92,SCREENWIDTH),0,70,92,SCREENWIDTH,SCREENHEIGHT,player))
		
		# Update timers
		waitTime = random.uniform(.5,2)
		enemyTimer = time.time()
	
	# Prevent enemies from spawning when paused
	elif pauseEnemies:
		waitTime = random.uniform(1,2.5)
		enemyTimer = time.time()

	# Rectangle side timer
	pygame.draw.rect(surface, (0, 100, 0), pygame.Rect((45, 190), (50, 290)))
	if abs(TIMERINIT-amtMove) <= 280:
		# Draw timers
		pygame.draw.rect(surface, (0, 255, 0), pygame.Rect((50, (475-TIMERINIT)+amtMove), (40, TIMERINIT-amtMove)))
	else:
		pygame.draw.rect(surface, (0, 255, 0), pygame.Rect((50, 195), (40, 280)))

		# Pause enemies
		pauseEnemies = True

		# Animate planet
		if redPlanet.animationStat['down'] == False:
			redPlanet.animateDown(surface)
		else:
			planetPause = showLevelText(surface, level)
			redPlanet.animateThrough(surface)
			if redPlanet.animationStat['through'] == True and planetPause == True:
				# Reset timers
				timer = time.time()
				redPlanet.reset()

				# Unpause enemies
				pauseEnemies = False

				# Update level
				level += 1

	# Draw side text
	healthText = font.render("HEALTH: " + str(health), False, WHITE)
	surface.blit(healthText, (20, SCREENHEIGHT-40))

	levelText = font.render("LEVEL: " + str(level), False, WHITE)
	surface.blit(levelText, (20, SCREENHEIGHT-20))

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

	# Check player health
	print(health)
	if health <= 0:
		pass

	# Updates
	pygame.display.flip()
	clock.tick(FPS)