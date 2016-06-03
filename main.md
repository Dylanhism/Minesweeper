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
    r = 0
    t = 0
    screen.fill(RED)
    pygame.display.update()
    menuText = fontTitle.render("Play", True, BLACK)
    #Code For Putting Images On Screen#
    test = pygame.image.load("EasyBomb.png")
    x = 0 + borderX
    y = 0 + borderY
    
def easy():
    bombCount = 16
    easyDifNumY = 8
    easyDifNumX = 8
    while t < easyDifNumY:
        while r < easyDifNumX:
            screen.blit(test,(x,y))                
            pygame.display.update()
            r = r + 1
            x = x + 91
        easyDifNumX = easyDifNumX + 8    
        t = t + 1
        y = y + 91
def meduim():
    bombCount = 25
    medDifNumY = 10
    easyDifNumX = 10
    while t < medDifNumY:
        while r < medDifNumX:
            array.append(pepe(r)) 
            r = r + 1
        medDifNumX = medDifNumX + 10    
        t = t + 1
        medDifNumY = 10
def hard():
    bombCount = 36
    hardDifNumX = 10
    while t < hardDifNumY:
        while r < hardDifNumX:
            array.append(pepe(r))
            r = r + 1
        hardDifNumX = hardDifNumX + 10    
        t = t + 1
menu()
