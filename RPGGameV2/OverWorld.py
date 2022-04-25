from RPG import InFight
import random
import pygame 
from SpritesOfThings import Sprites
from RandomGen import RandomGeneration
class Player: 
    #[True, True, 0] stands for ['Going up', 'Going down' and 'posistion']
    X = [True, True, 0]
    Y = [True, True, 0]
    
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        

#two different player classes
playerOver = Player([False, False, 362], [False, False, 268])
    
class Enemy:
    X = 0
    Y = 0
    isMade = False
    
    def __init__(self, X, Y, isMade):
        self.X = X
        self.Y = Y
        self.isMade = isMade

class Lay(): 
    layout = ['']

RandomGeneration(Lay.layout)

testEnemy = Enemy(random.randrange(20), random.randrange(20), False)
while(testEnemy.isMade == False):
    if(testEnemy.X*20 + testEnemy.Y <= 400):
        if(Lay.layout[0][testEnemy.X*20 + testEnemy.Y] == 'true'):
            testEnemy.isMade = True
            print(testEnemy.X, testEnemy.Y)
        else:
            testEnemy.X = random.randrange(20)
            testEnemy.Y = random.randrange(20)
    else:
        testEnemy.X = random.randrange(20)
        testEnemy.Y = random.randrange(20)
    

class PlayMode:
    inPlayMode = False
    groundIs = [0, 0]

#defs are here
def LoadSprites(main, enemy, ground, OX, OY, EX, EY, layout, groundIs):
    
    for x in range(20):
        for y in range(20):
            if(layout[0][y*20+x] == 'true'):
                            screen.blit(ground, (x * 80 - groundIs[0] * 80 + 40, y * 60 - groundIs[1] * 60 + 30))
            if(x == EX):
                if(y == EY):
                    if(True):
                        screen.blit(enemy, (testEnemy.X * 80 - groundIs[0] * 80, testEnemy.Y * 60 - groundIs[1] * 60))
                 
    screen.blit(main, (OX[2], OY[2]))
    
            
        
screen = pygame.display.set_mode((800, 600))

running = True

#what happens when the game is actually running is here

clock = pygame.time.Clock()
while(running):
 
    clock.tick(60)

    screen.fill((0,0,0))
    LoadSprites(Sprites.main, Sprites.enemy, Sprites.ground, playerOver.X, playerOver.Y, testEnemy.X, testEnemy.Y, Lay.layout, PlayMode.groundIs)
    pygame.display.update()
    
    if(PlayMode.inPlayMode == False):  
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(PlayMode.groundIs[1] > -6):
                    if(event.key == pygame.K_w):
                            PlayMode.groundIs[1] -= 1
                if(PlayMode.groundIs[1] < 16):
                    if(event.key == pygame.K_s):
                            PlayMode.groundIs[1] += 1
                if(PlayMode.groundIs[0] > -6):
                    if(event.key == pygame.K_a):
                            PlayMode.groundIs[0] -= 1
                if(PlayMode.groundIs[0] < 16):
                    if(event.key == pygame.K_d):
                            PlayMode.groundIs[0] += 1
                print(PlayMode.groundIs[0], PlayMode.groundIs[1], testEnemy.X, testEnemy.Y)
    if(PlayMode.groundIs[0] == testEnemy.X - 5 and PlayMode.groundIs[1] == testEnemy.Y - 5):
        print('why')
        PlayMode.inPlayMode = True
        
    if(PlayMode.inPlayMode):
        InFight()
        
    