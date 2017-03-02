import random
b = "B"
BombArray = []
for i in range(0,64):
    BombArray.append(i)
    i = i + 1
bombs = 17
for j in range(0, bombs):
    bombPlacement = random.randint(0,63)
    meme = (BombArray[bombPlacement])
    if isinstance ((meme), str):
        bombs = bombs + 1
        
    if isinstance ((meme), int):
        meme = str(BombArray[bombPlacement])
        meme = (meme + "B")
        BombArray[bombPlacement] = meme
print BombArray
