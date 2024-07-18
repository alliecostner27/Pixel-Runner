import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = test_font.render(f'{current_time}', False, (64,64,64))
    score_rec = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface,score_rec)
    

pygame.init() ## starts Pygame 
screen = pygame.display.set_mode((800, 400)) ## creates our display screen | 800 width, 400 height
pygame.display.set_caption('Runner Platformer') #title 
clock = pygame.time.Clock()
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('./graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('./graphics/ground.png').convert_alpha()
#text_surface = test_font.render('Score', False, (64, 64, 64))
#text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,300))


player_surface = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300)) #draws a rectangle around the player_surface

player_gravity = 0

while True:
    for event in pygame.event.get(): # gets every single event and loops through 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect >= 300: 
                    player_gravity = -20

            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active=True
                snail_rect.left = 800
                start_time = pygame.time.get_ticks()
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        #pygame.draw.rect(screen, '#8cbed6', text_rect)
        #pygame.draw.rect(screen, '#8cbed6', text_rect,20)
        #screen.blit(text_surface,text_rect)
        display_score()

        #Snail
        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else: 
        screen.fill('Yellow')

    pygame.display.update() # updates our display screen
    clock.tick(60) # while true, the game should not run faster than 60 times per second. 
