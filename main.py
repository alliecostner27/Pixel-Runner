import pygame
from sys import exit

pygame.init() ## starts Pygame 
screen = pygame.display.set_mode((800, 400)) ## creates our display screen | 800 width, 400 height
pygame.display.set_caption('Runner Platformer') #title 
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('dimgray')

while True:
    for event in pygame.event.get(): # gets every single event and loops through 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (400,100))

    pygame.display.update() # updates our display screen
    clock.tick(60) # while true, the game should not run faster than 60 times per second. 
