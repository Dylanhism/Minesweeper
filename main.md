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
#Code For Putting Images On Screen#
VARIABLE = pygame.image.load("image.jpg")        #Creates A variable That is The Image Itself
displayScreen.blit(VARIABLE(x,y))                #Places The Image Called "VARIABLE" On The Screen At The X and Y Coordinates
pygame.display.update()                          #updates Screen
#Algorithm Theory#
#borderSize = WhatWeWantItToBeExDee            #The borderSize is the difference in coordinates between The Origin and Where                                                  #the minefield is. example: (20,50), Therefore the border is 20 pixels from the                                                #right side and 50 pixels from the top. The same can be done for the bottom and                                                #the left by simply taking the total resolution and subtracting the border      #if difficulty == HARD:                        #instead. example: screenSize = (800,600) borderSize2 = ScreenSize - (20,50)
#  imageSize = screenSize / 5                  #Essentially if screen size is (1000,1000) than image size will now be(200,200).
#  originalImage = (0,0) + borderSize          #takes the top right corner, ((0,0)) and moves it down and to the right equal to
#if difficulty == MEDIUM:                      #the point at which the actual square begins.
#  imageSize = screenSize / 4                  #Essentially if screen size is (1000,1000) than image size will now be (250,250)
  
#if difficulty == EASY:
#  imageSize = screenSize / 3                  #Essentially if screen size is (1000,1000) than image size will now be (333,333)
  
#Fills screen white#
screen.fill(WHITE)
pygame.display.update()
fontTitle = pygame.font.SysFont("Arial", 30)

def menu():
  screen.fill(WHITE)
  pygame.display.update()
  menuText = fontTitle.render("Play" True, BLACK)
  
