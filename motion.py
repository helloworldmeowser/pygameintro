import pygame
from sys import exit
#this line above is connect to line 18 exit() to make while True stop causing program error

pygame.init() #After the import pygame, must type pygame.init() to initiate or start pygame (it help run image and sound)

#screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((800,400)) #This line create a display surface (the window player is going to see)
pygame.display.set_caption('Race') #This give game title
clock = pygame.time.Clock() # help control the framework time

test_surface = pygame.Surface((100,200)) # inside tuple ((width, height))
test_surface.fill('Red') # add surface color

#Figure out a way to keep code running forever (keep display surface open), so use while loop
while True:
    for event in pygame.event.get(): # this line for player input all event
        if event.type == pygame.QUIT: #this line allow player ability to close the game
            pygame.quit()
            exit()
    screen.blit(test_surface, (0,0)) #blit stand for block imagine transfer


    pygame.display.update() #this line update the py.game.display.set_mode((800,400))
    clock.tick(60) #this while true should not run faster than 60 times per sec
