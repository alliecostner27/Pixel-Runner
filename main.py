import pygame
from sys import exit

pygame.init() ## starts Pygame 
screen = pygame.display.set_mode((800, 400)) ## creates our display screen | 800 width, 400 height
pygame.display.set_caption('Runner Platformer') #title 
clock = pygame.time.Clock()
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('./graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('./graphics/ground.png').convert_alpha()
text_surface = test_font.render('My Game', False, 'Black')

snail_surface = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

while True:
    for event in pygame.event.get(): # gets every single event and loops through 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface,(300, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 265))

    pygame.display.update() # updates our display screen
    clock.tick(60) # while true, the game should not run faster than 60 times per second. 
