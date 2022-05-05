from RPG import InFight
import random
import pygame 
from SpritesOfThings import Sprites
from RandomGen import RandomGeneration
class Player: 
    #[True, True, 0] stands for ['Going up', 'Going down' and 'posistion']
    X = [True, True, 0]
    Y = [True, True, 0]
    isMade = False
    randomX = 0
    randomY = 0
    
    def __init__(self, X, Y, randomX, randomY):
        self.X = X
        self.Y = Y
        self.randomX = randomX
        self.randomY = randomY

#two different player classes
playerOver = Player([False, False, 362], [False, False, 268], 0, 0)
    
class Enemy:
    X = 0
    Y = 0
    isMade = False
    
    def __init__(self, X, Y, isMade):
        self.X = X
        self.Y = Y
        self.isMade = isMade

class PlayMode:
    inPlayMode = False
    groundIs = [0, 0]
    everything = True

class Lay(): 
    layout = [[], []]
    
    levelAgain = False

RandomGeneration(Lay.layout)


testEnemy = Enemy(0, 0, False)



#defs are here
def LoadSprites(main, enemy, ground, OX, OY, EX, EY, layout, groundIs):
    
    for x in range(20):
        for y in range(20):
            if(layout[0][y*20+x] == 'true'):
                            screen.blit(ground, (x * 80 - groundIs[0] * 80 + 40, y * 60 - groundIs[1] * 60 + 30))
            if(testEnemy.X*20+testEnemy.Y <= 400):
                if(layout[0][testEnemy.X*20+testEnemy.Y] == 'true'):
                        if(True):
                            screen.blit(enemy, (testEnemy.X * 80 - groundIs[0] * 80, testEnemy.Y * 60 - groundIs[1] * 60))
                     
    screen.blit(main, (OX[2], OY[2]))
    
            
        
screen = pygame.display.set_mode((800, 600))

running = True
while(PlayMode.everything):
    testEnemy.isMade = False
    playerOver.isMade = False
    running = True

    if(Lay.levelAgain == True):
        RandomGeneration(Lay.layout)
        
    while(testEnemy.isMade == False):
        Player.randomX = random.randrange(20) -5
        Player.randomY = random.randrange(20) -5
        if(Player.randomY*20+Player.randomX >= 0):
            if(Lay.layout[0][Player.randomY*20+Player.randomX] == 'true'):
                testEnemy.X = Player.randomX + 1
                testEnemy.Y = Player.randomY + 1 
                testEnemy.isMade = True
            else: 
                Player.randomX = random.randrange(20) -5
                Player.randomY = random.randrange(20) -5
        else: 
            Player.randomX = random.randrange(20) -5
            Player.randomY = random.randrange(20) -5
            
    while(playerOver.isMade == False):
        
        Player.randomX = random.randrange(20) -5
        Player.randomY = random.randrange(20) -5
        if(Player.randomY*20+Player.randomX + 84 < 400 ):
            if(Lay.layout[0][Player.randomY * 20 + Player.randomX + 84] == 'true'):
                print('yo')
                PlayMode.groundIs[0] = Player.randomX
                PlayMode.groundIs[1] = Player.randomY
                playerOver.isMade = True
            else: 
                Player.randomX = random.randrange(20) -5 
                Player.randomY = random.randrange(20) -5
        else:
            Player.randomX = random.randrange(20) -5 
            Player.randomY = random.randrange(20) -5
        
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
                    if(PlayMode.groundIs[1] > -5):
                        if(event.key == pygame.K_w):
                            if(Lay.layout[0][PlayMode.groundIs[1] * 20 + PlayMode.groundIs[0] + 64] == 'true'):
                                PlayMode.groundIs[1] -= 1
                    if(PlayMode.groundIs[1] < 15):
                        if(event.key == pygame.K_s):
                            if(Lay.layout[0][PlayMode.groundIs[1] * 20 + PlayMode.groundIs[0] + 104] == 'true'):
                                PlayMode.groundIs[1] += 1
                    if(PlayMode.groundIs[0] > -5):
                        if(event.key == pygame.K_a):
                            if(Lay.layout[0][PlayMode.groundIs[1] * 20 + PlayMode.groundIs[0] + 83] == 'true'):
                                PlayMode.groundIs[0] -= 1
                    if(PlayMode.groundIs[0] < 15):
                        if(event.key == pygame.K_d):
                            if(Lay.layout[0][PlayMode.groundIs[1] * 20 + PlayMode.groundIs[0] + 85] == 'true'):
                                PlayMode.groundIs[0] += 1
                    if(event.key == pygame.K_t):
                        running = False
                        Lay.levelAgain = True
                                
                    print(PlayMode.groundIs[1], PlayMode.groundIs[0], testEnemy.Y, testEnemy.X)
        if(PlayMode.groundIs[0] == testEnemy.X - 5 and PlayMode.groundIs[1] == testEnemy.Y - 5):
            InFight()
            testEnemy.X = 200
    
            
        