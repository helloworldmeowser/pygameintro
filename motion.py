import pygame
from sym import exit

#After the import pygame, must type pygame.init() to initiate or start pygame (it help run image and sound)
pygame.init()

#This line create a display surface (the window player is going to see)
#screen = pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((800,400))

#Figure out a way to keep code running forever (keep display surface open), so use while loop
while True:
    #draw all the element 
    #update everything
    for event in pygame.event.get(): # this line for player input all event
        if event.type == pygame.QUIT: #this line allow player ability to close the game
            pygame.quit()
    pygame.display.update() #this line update the py.game.display.set_mode((800,400))