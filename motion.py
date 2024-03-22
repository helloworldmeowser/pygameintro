import pygame
from sys import exit # Connect to  exit() to while True stop causing program error

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)

pygame.init() #After the import pygame, must type pygame.init() to initiate or start pygame (it help run image and sound)

#screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((800,400)) #This line create a display surface (the window player is going to see)
pygame.display.set_caption('Jump Game Basic') #This give game title
clock = pygame.time.Clock() # help control the framework time
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # (font type, font size)
game_active = False
start_time = 0


#test_surface = pygame.Surface((100,200)) # inside tuple ((width, height))
# test_surface.fill('Red') # add surface color

#convert help pygame to convert image for pygame to work with easily and convert_alpha is to get rid of black and white line

# import image and specify a path to graphics folder
sky_surface = pygame.image.load('graphics/Sky.png').convert()
# import ground image
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surf = test_font.render('My game', False, (64,64,64)) # (text, AA, color) has to be False because it is pixel art else it be True
#score_rect = score_surf.get_rect(center = (400,50)) #center the text

#import snail image
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

#import plyaer image
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) #help snail pass through main character
player_gravity = 0
# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Jump', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400,300))

#Figure out a way to keep code running forever (keep display surface open), so use while loop
while True:
    for event in pygame.event.get(): # this line for player input all event
        if event.type == pygame.QUIT: #this line allow player ability to close the game
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEMOTION:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20 
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
    if game_active:
        screen.blit(sky_surface, (0,0)) #blit stand for block imagine transfer, this is sky coordination
        screen.blit(ground_surface, (0,300)) # ground coordination
        #pygame.draw.rect(screen,'#c0e8ec',score_rect)
        #pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        #pygame.draw.line(screen,'Brown',pygame.Rect,(50,200,100,100)) #(left,top,width,height))
        #screen.blit(score_surf,score_rect) # text size
        display_score( )


        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        
        screen.blit(snail_surf,snail_rect) # snail position and it is static
        
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # Function that end the game when player touch the snail - collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(game_name,game_name_rect)
        screen.blit(game_message,game_message_rect)


    pygame.display.update() #this line update the py.game.display.set_mode((800,400))
    clock.tick(60) #this while true should not run faster than 60 times per sec
