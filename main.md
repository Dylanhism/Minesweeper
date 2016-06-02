import pygame
import sys
import time

pygame.init()
size = (750, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper *testing*")
global x 
global y 
done = False

#Colours here#
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (000, 000, 000)
BLUE = (000, 102, 204)
RED = (204, 000, 000)                          
#Fills screen white#
screen.fill(RED)
pygame.display.update()
fontTitle = pygame.font.SysFont("Arial", 30)

def menu():
    borderX = 10
    borderY = 75
    screen.fill(RED)
    pygame.display.update()
    menuText = fontTitle.render("Play", True, BLACK)
    #Code For Putting Images On Screen#
    test = pygame.image.load("EasyBomb.png")
    x = 0 + borderX
    y = 0 + borderY
    while y < 793 - borderY:
        while x < 730 + borderX:        
            screen.blit(test,(x,y))                
            pygame.display.update() 
            x = x + 91
        y = y + 91
        x = borderX
#hardDifNumY = 12
#hardDifNumX = 12
#while t < hardDifNumY:
#    while r < hardDifNumX:
#        array.append(pepe(r))       
#    hardDifNumX = hardDifNumX + 12    
#    t = t + 1
menu()
