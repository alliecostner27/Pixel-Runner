import pygame

pygame.init() ## starts Pygame 
screen = pygame.display.set_mode((800, 400)) ## creates our display screen | 800 width, 400 height

while True:
    for event in pygame.event.get(): # gets every single event and loops through 
        if event.type == pygame.QUIT:
            pygame.quit()
    # draw all our elements
    # update everything
    pygame.display.update() # updates our display screen
