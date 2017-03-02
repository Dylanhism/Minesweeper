import pygame
import sys
import time #Imports needed for code
import os
import random

pygame.init()
size = (750, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper *testing*")

done = False

#Colours here#
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
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

clock = pygame.time.Clock()

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
        mousePos = pygame.mouse.get_pos()  #Position for the mouse
        if easyPosition.collidepoint(mousePos):
          easyMode()
        elif mediumPosition.collidepoint(mousePos): #Collide with each text selection and then load the function
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
    borderX = 11
    borderY = 64 #These boarders are for adding space for reset button(pepe in this case)
    #Code For Putting Images On Screen#
    path = os.path.join("Images\\EasySize", "easyUnknown.png")
    backPath = os.path.join("Images", "backGround.png")
    happy = os.path.join("Images", "happy.png")
    angry = os.path.join("Images", "angry.png")
    image = pygame.image.load(path)
    happyImage = pygame.image.load(happy)
    angryImage = pygame.image.load(angry)
    backGroundImage = pygame.image.load(backPath)
    screen.blit(backGroundImage, (0,0))
    screen.blit(happyImage, (354, 15))
    x = 0 + borderX
    y = 0 + borderY
    imageX = 0 + borderX
    imageY = 0 + borderY
    
    unknownPos = image.get_rect()
    
    b = "B"
    BombArray = []
    for i in range(1,65): #Location for the bombs become generated into an array.
      BombArray.append(i) #Since 64 tiles, loop 64 times and add those numbers to the array.
      #print BombArray[i]
      i = i + 1
    bombs = 17 #Num. of bombs in array to be created. Can be increased.
    for j in range(0, bombs):
      bombPlacement = random.randint(1,64) #Makes random position for bombs
      meme = (BombArray[bombPlacement]) 
      if isinstance ((meme), str): #If there is a bomb there(because it becomes a string) then add 1 to the loop count.
        bombs = bombs + 1
      if isinstance ((meme), int): # else, add "B" representing a bomb followed by a num(it's position)
        meme = str(BombArray[bombPlacement])
        meme = (meme + "B")
        BombArray[bombPlacement] = meme
    #print BombArray

    grid = []
    for row in range(8):
      grid.append([])
      for column in range(8): #loops through to create a grid
        grid[row].append(0)
    grid[1][1] = 0
    for bombLetter in BombArray:
      if isinstance ((bombLetter), str):
        bombIndex = BombArray.index(bombLetter)
        if bombIndex >= 0 and <= 8:
          grid[0][bombLetter]
    print grid#PRINTS EACH BLOCK OF ROWS AND COLUMNS
    go = True
    while go:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          go = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          column = mousePos[0] // (91) + 1#Round to the nearest tile
          row = mousePos[1] // (91)#91 being the size of each tile
          #grid[row][column] = 1
          print("Click ", mousePos, "Grid coordinates: ", row, column)
          print grid

      while y < 793 - borderY:
        while x < 720 + borderX:
          screen.blit(image,(x,y))
          pygame.display.update()
          x = x + 91
        y = y + 91
        x = borderX
        
    pygame.quit()
    
def medMode():
    borderX = 11
    borderY = 64 #These boarders are for adding space for reset button(pepe in this case)
    #Code For Putting Images On Screen#
    path = os.path.join("Images\\MediumSize", "mediumUnknown.png")
    backPath = os.path.join("Images", "backGround.png")
    happy = os.path.join("Images", "happy.png")
    angry = os.path.join("Images", "angry.png")#load all the images
    image = pygame.image.load(path)
    backGroundImage = pygame.image.load(backPath)
    happyImage = pygame.image.load(happy) #Load all the images
    angryImage = pygame.image.load(angry)
    screen.blit(backGroundImage, (0,0))
    screen.blit(happyImage, (354, 15))
    x = 0 + borderX
    y = 0 + borderY
    pygame.display.update()

    grid = []
    for row in range(9):
      grid.append([])
      for column in range(9): #loops through to create a grid
        grid[row].append(0)
    grid[1][1] = 1

    go = True
    while go:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          go = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          column = mousePos[0] // (73) #Round to the nearest tile
          row = mousePos[1] // (73)
          grid[row][column] = 1
          print("Click ", mousePos, "Grid coordinates: ", row, column)
          
      while y < 810 - borderY:
        while x < 720 + borderX:        
          screen.blit(image,(x,y))                
          pygame.display.update() 
          x = x + 73
        y = y + 73
        x = borderX
    pygame.quit()

def hardMode():
    borderX = 15
    borderY = 67 #These boarders are for adding space for reset button(pepe in this case)
    #Code For Putting Images On Screen#
    path = os.path.join("Images\\HardSize", "hardUnknown.png")
    backPath = os.path.join("Images", "backGround.png")
    happy = os.path.join("Images", "happy.png")
    angry = os.path.join("Images", "angry.png")
    image = pygame.image.load(path)
    happyImage = pygame.image.load(happy) #Load all the images
    angryImage = pygame.image.load(angry)
    backGroundImage = pygame.image.load(backPath)
    screen.blit(backGroundImage, (0,0))
    screen.blit(happyImage, (354, 15))
    x = 0 + borderX
    y = 0 + borderY

    grid = []
    for row in range(13):
      grid.append([])
      for column in range(13): #loops through to create a grid
        grid[row].append(0)
    grid[1][1] = 1

    go = True
    while go:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          go = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          mousePos = pygame.mouse.get_pos()
          column = mousePos[0] // (60) #Round to the nearest tile
          row = mousePos[1] // (60)
          grid[row][column] = 1
          print("Click ", mousePos, "Grid coordinates: ", row, column)# Print mouse position for testing grid
          
      while y < 820 - borderY:
        while x < 720 + borderX:        
            screen.blit(image,(x,y))                
            pygame.display.update() 
            x = x + 60
        y = y + 60
        x = borderX
    pygame.quit()

def instructions():
    screen.fill(WHITE)
    pygame.display.update()
    newFile = open('howToPlay.txt', 'r') #opens txt file with instructions
    go = True
    x = 50
    y = 150 #Start position for the lines that are printed
    backText = fontTitle.render("Back to Menu", True, BLACK) #Return button for the menu
    titlePosition = backText.get_rect() #Position for text to be centered
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
          if titlePosition.collidepoint(mousePos): #Return to the menu if clicked on.
            menu()
      for line in newFile:
        lineText = fontTiny.render(line, True, BLACK)
        screen.blit(lineText, (x, y)) #loops and move position for each line
        y += 50
        pygame.display.update()
    
    pygame.quit() 

menu()
