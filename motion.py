#background and ground current progress
import pygame
from sys import exit
#this line above is connect to line 18 exit() to make while True stop causing program error

pygame.init() #After the import pygame, must type pygame.init() to initiate or start pygame (it help run image and sound)

#screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((800,400)) #This line create a display surface (the window player is going to see)
pygame.display.set_caption('Race') #This give game title
clock = pygame.time.Clock() # help control the framework time

test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # (font type, font size)

#test_surface = pygame.Surface((100,200)) # inside tuple ((width, height))
# test_surface.fill('Red') # add surface color

# import image and specify a path to graphics folder
sky_surface = pygame.image.load('graphics/Sky.png')

# import ground image
ground_surface = pygame.image.load('graphics/ground.png')

text_surface = test_font.render('My game', False, 'Black') # (text, AA, color) has to be False because it is pixel art else it be True

#Figure out a way to keep code running forever (keep display surface open), so use while loop
while True:
    for event in pygame.event.get(): # this line for player input all event
        if event.type == pygame.QUIT: #this line allow player ability to close the game
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0,0)) #blit stand for block imagine transfer, this is sky coordination

    screen.blit(ground_surface, (0,300)) # ground coordination

    screen.blit(text_surface, (300,50))

    pygame.display.update() #this line update the py.game.display.set_mode((800,400))
    clock.tick(60) #this while true should not run faster than 60 times per sec
