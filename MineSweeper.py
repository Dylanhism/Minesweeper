import pygame
import sys
import time
import os
import random
pygame.init()
size = (750, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper *testing*")

done = False

#Colours here#
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (000, 000, 000)
BLUE = (000, 102, 204)
RED = (204, 000, 000)
#Code For Putting Images On Screen#
#VARIABLE = pygame.image.load("image.jpg")        #Creates A variable That is The Image Itself
#displayScreen.blit(VARIABLE(x,y))                #Places The Image Called "VARIABLE" On The Screen At The X and Y Coordinates
#pygame.display.update()                          #updates Screen

#Fills screen white#
screen.fill(WHITE)
pygame.display.update()
fontTitle = pygame.font.SysFont("Arial", 75)
fontSmall = pygame.font.SysFont("Arial", 50)
fontTiny = pygame.font.SysFont("Arial", 20)

def menu():
  screen.fill(WHITE)
  pygame.display.update()
  playText = fontTitle.render("Play", True, BLACK)
  titleText = fontTitle.render("Minesweeper", True, BLACK)
  easyText = fontSmall.render("Easy", True, BLACK)
  mediumText = fontSmall.render("Medium", True, BLACK)
  hardText = fontSmall.render("Hard", True, BLACK)
  instrucText = fontTitle.render("How to play", True, BLACK)
  quitText = fontSmall.render("Quit", True, BLACK)
  
  titlePosition = titleText.get_rect() #Position for "Minesweeper"
  titlePosition.centerx = screen.get_rect().centerx
  titlePosition.centery = screen.get_rect().centery - 300
  
  positionText = playText.get_rect()  #Position for "Play"
  positionText.centerx = screen.get_rect().centerx
  positionText.centery = screen.get_rect().centery - 200

  easyPosition = easyText.get_rect()  #Position for "Easy"
  easyPosition.centerx = screen.get_rect().centerx
  easyPosition.centery = screen.get_rect().centery - 125

  mediumPosition = mediumText.get_rect()  #Position for "Medium"
  mediumPosition.centerx = screen.get_rect().centerx
  mediumPosition.centery = screen.get_rect().centery -75

  hardPosition = hardText.get_rect()  #Position for "Hard"
  hardPosition.centerx = screen.get_rect().centerx
  hardPosition.centery = screen.get_rect().centery - 25

  instrucPos = instrucText.get_rect()  #position for "how to play"
  instrucPos.centerx = screen.get_rect().centerx
  instrucPos.centery = screen.get_rect().centery + 25

  quitPos = quitText.get_rect()  #Position for quit button
  quitPos.centerx = screen.get_rect().centerx - 300
  quitPos.centery = screen.get_rect().centery + 350

  screen.blit(titleText,(titlePosition))  #Puts the loaded images onto the screen with the positions predetermined
  screen.blit(playText,(positionText))  #Play button
  screen.blit(easyText,(easyPosition))  #Easy difficulty
  screen.blit(mediumText,(mediumPosition))  #Medium difficulty
  screen.blit(hardText,(hardPosition))  #Hard difficulty
  screen.blit(instrucText,(instrucPos))  #How to play text
  screen.blit(quitText, (quitPos))  #Quit text
  pygame.display.update()
  
  
  go = True
  while go == True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        go = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()
        if easyPosition.collidepoint(mousePos):
          easyMode()
        elif mediumPosition.collidepoint(mousePos):
          medMode()
        elif hardPosition.collidepoint(mousePos):
          hardMode()
        elif instrucPos.collidepoint(mousePos):
          instructions()
        elif quitPos.collidepoint(mousePos):
          go = False
          
  pygame.quit()
  sys.exit()
  
def easyMode():
    bombPlacement(8, 91, 16)
    borderX = 11
    borderY = 71
    screen.fill(GREY)
    pygame.display.update()
    #Code For Putting Images On Screen#
    path = os.path.join("Images\\EasySize", "easyUnknown.png")
    image = pygame.image.load(path)
    x = 0 + borderX
    y = 0 + borderY
    go = True
    while go:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          go = False
      while y < 793 - borderY:
        while x < 720 + borderX:        
          screen.blit(image,(x,y))                
          pygame.display.update() 
          x = x + spriteSize
        y = y + spriteSize
        x = borderX
    pygame.quit()
    #sys.exit()
    
def medMode():
    bombPlacement(10, 73, 25)
    borderX = 11
    borderY = 71
    screen.fill(GREY)
    pygame.display.update()
    #Code For Putting Images On Screen#
    path = os.path.join("Images\\MediumSize", "mediumUnknown.png")
    image = pygame.image.load(path)
    x = 0 + borderX
    y = 0 + borderY
    go = True
    while go:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          go = False
      while y < 810 - borderY:
        while x < 720 + borderX:        
          screen.blit(image,(x,y))                
          pygame.display.update() 
          x = x + spriteSize
        y = y + spriteSize
        x = borderX
    pygame.quit()
    sys.exit()

def hardMode():
    bombPlacement(12, 60, 48)
    borderX = 15
    borderY = 71
    screen.fill(GREY)
    pygame.display.update()
    #Code For Putting Images On Screen#
    path = os.path.join("Images\\HardSize", "hardUnknown.png")
    image = pygame.image.load(path)
    x = 0 + borderX
    y = 0 + borderY
    go = True
    while go:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          go = False
      while y < 820 - borderY:
        while x < 720 + borderX:        
            screen.blit(image,(x,y))                
            pygame.display.update() 
            x = x + spriteSize
        y = y + spriteSize
        x = borderX
    pygame.quit()
    sys.exit()

def instructions():
    screen.fill(WHITE)
    pygame.display.update()
    newFile = open('howToPlay.txt', 'r')
    go = True
    x = 50
    y = 150
    backText = fontTitle.render("Back to Menu", True, BLACK)
    titlePosition = backText.get_rect() #Position for "Minesweeper"
    titlePosition.centerx = screen.get_rect().centerx
    titlePosition.centery = screen.get_rect().centery + 300
    screen.blit(backText,(titlePosition))
    pygame.display.update()
    while go:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          go = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          if titlePosition.collidepoint(mousePos):
            menu()
      for line in newFile:
        lineText = fontTiny.render(line, True, BLACK)
        screen.blit(lineText, (x, y))
        y += 50
        pygame.display.update()
    
    pygame.quit()
    #sys.exit() 

def bombPlacement(u, spriteSize, bombNum):
    j = 0
   #u = 8
    X = 0
    Y = 0
    #spriteSize = 91
    XArray = []
    YArray = []
    for i in range(0, ((u*u)-1)):
        XArray.append(X)
        YArray.append(Y)
        X = X + spriteSize
        j = j + 1
        #print XArray    #(for the good shit)
        if j == u:
            Y = Y + spriteSize
            X = 0
            j = 0
    i = 0
    lengthXArray = len(XArray) - 1
    lengthYArray = len(YArray) - 1
    for i in range (0, bombNum):
        bombPlacementX = XArray[random.randint(0,((u*u)-1))]
        bombPlacementY = YArray[random.randint(0,((u*u)-1))]
        for p in range(0,  lengthYArray):
            if (bombPlacementY) == YArray[p]:
                for k in range(0, lengthXArray):
                    if (bombPlacementX) == XArray[k] :
                        bombNum += 1

    #lengthX = len(bombPlacementX)
    #lengthY = len(bombPlacementY)

    #for i in range(0, lengthX):
    #    pass

menu()
