import pygame

pygame.init()

window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))

    pygame.draw.rect(window, (0, 0, 255), (20, 20, 160, 160))
        [(100, 20), (100 + 0.8660 * 80, 140), (100 - 0.8660 * 80, 140)])

    pygame.display.flip()

pygame.quit()
exit()