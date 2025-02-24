import random
import pygame
import time

pygame.init()

root = pygame.display.set_mode((800, 800))

color = 'Red'

running = True

while running:
    time.sleep(0.1)
    timer = random.randint(0, 3)
    if start == True:

        root.fill(color)
    else:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start = True