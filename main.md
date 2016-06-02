#import pygame
import sys
import time

pygame.init()
size = (1024, 768)
screen = pygame.displat.set_mode(size)
pygame.display.set_caption("Minesweeper *testing*")

done = False

#Colours here#
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (000, 000, 000)
BLUE = (000, 102, 204)
RED = (204, 000, 000)

#Fills screen white#
screen.fill(WHITE)
pygame.display.update()
fontTitle = pygame.font.SysFont("Arial", 30)

def menu():
  screen.fill(WHITE)
  pygame.display.update()
  menuText = fontTitle.render("Play" True, BLACK)
  
