from RPG import InFight
import random
import pygame 
from SpritesOfThings import Sprites
from RandomGen import RandomGeneration
from Cutscene import Scene 
from pygame import mixer
from End import Ended

#this script is the main overworld

mixer.init()
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

class Partner:
    X = 3627
    Y = 208

#two different player classes
playerOver = Player([False, False, 362], [False, False, 268], 0, 0)
    
#Enemy class
class Enemy:
    X = 0
    Y = 0
    isMade = False
    hasFought = False
    
    def __init__(self, X, Y, isMade, hasFought):
        self.X = X
        self.Y = Y
        self.isMade = isMade
        self.hasFought = hasFought

#what actually controls the player
class PlayMode:
    inPlayMode = False
    groundIs = [0, 0]
    everything = True
    goneThrough = -1
    whenBoss = 2

class Music:
    musicPlayed = False

#Layout of the level
class Lay(): 
    layout = [[], []]
    
    #sees when level should reset
    levelAgain = False

class Cut: 
    cutSceneStart = True
    whichScene = 0

#what sends the script to randomGen, makes level what it is
RandomGeneration(Lay.layout)

#makes the test enemy 
testEnemy = Enemy(0, 0, False, False)



#defs are here
#this one loads all sprites
def LoadSprites(main, enemy, ground, stairs, ferin, OX, OY, grounIs, EX, EY, PX, PY, layout, groundIs):
    if(PlayMode.everything):
        for y in range(20):
            for x in range(20):
                
                #sees if a ground tile is true, if it is it makes the ground
                if(layout[0][y*20+x] == 'true'):
                    screen.blit(ground, (x * 80 - groundIs[0] * 80 + 40, y * 60 - groundIs[1] * 60 + 30))
                #does the same but with enemy
                
                if(layout[1][y*20+x] == 'true'):
                    screen.blit(stairs,(x*80 - groundIs[0] * 80 + 40, y*60 - groundIs[1] * 60 + 30))
                    
                screen.blit(enemy, (testEnemy.X * 80 - grounIs[0] * 80, testEnemy.Y * 60 - groundIs[1] * 60))
        #puts the player model in the middle of the screen
        
        screen.blit(ferin, (PX + 20, PY - 35))
        screen.blit(main, (OX[2] + 20, OY[2] - 35))
        if(PY > OY[2]): 
            screen.blit(ferin, (PX + 20, PY - 35))
            
#makes the screen
screen = pygame.display.set_mode((800, 600))

#sees if the game should be able to be played
running = True


#is everything that should run more than once


while(PlayMode.everything):
    #resets everything to what they are originally incase the code needs to reset
    testEnemy.isMade = False
    playerOver.isMade = False
    running = True

    #makes the level again
    if(Lay.levelAgain == True):
        for x in range(400):
            Lay.layout[1] = []
        RandomGeneration(Lay.layout)
    
    #spawns the enemmy at a random ground tile
    while(testEnemy.isMade == False):
        #gives the random number
        Player.randomX = random.randrange(19) 
        Player.randomY = random.randrange(19) 
        #if the random number is true and not under certain number
        if(Player.randomY*20+Player.randomX >= 0 and Player.randomY*20+Player.randomX <= 400):
            if(Lay.layout[0][Player.randomY*20+Player.randomX] == 'true'):
                testEnemy.X = Player.randomX +1
                testEnemy.Y = Player.randomY +1
                testEnemy.isMade = True
            #resets if these conditions aren't met
            else: 
                Player.randomX = random.randrange(19) 
                Player.randomY = random.randrange(19) 
        else: 
            Player.randomX = random.randrange(19) 
            Player.randomY = random.randrange(19) 
            
    #same thing as with the enemy but with the player
    while(playerOver.isMade == False):
        
        Player.randomX = random.randrange(20) - 4
        Player.randomY = random.randrange(20) - 4
        if(Player.randomY*20+Player.randomX -  84 <= 400 ):
            if(Lay.layout[0][Player.randomY * 20 + Player.randomX + 84] == 'true'):
                print('yo')
                PlayMode.groundIs[0] = Player.randomX
                PlayMode.groundIs[1] = Player.randomY
                playerOver.isMade = True
            else: 
                Player.randomX = random.randrange(20) -4
                Player.randomY = random.randrange(20) -4
        else:
            Player.randomX = random.randrange(20) -4
            Player.randomY = random.randrange(20) -4
        
    #what happens when the game is actually running is here
    #clock, used to steady fps
    clock = pygame.time.Clock()
    while(running):
        
        #this is used to play music
        if(Music.musicPlayed == False):
            mixer.music.load("CaveTheme.mp3")
            mixer.music.play(-1)
            Music.musicPlayed = True
            
        #this starts the cutscenes
        if(Cut.cutSceneStart): 
            Scene(Cut.whichScene)
            Cut.whichScene += 1
            Cut.cutSceneStart = False
            
            #this checks if the player should encounter the boss, in which case they go to the boss cutscene, it also ends the game when finished with the boss
            if(PlayMode.goneThrough == PlayMode.whenBoss):
                PlayMode.everything = False
                running = False
                playerOver.isMade = True
                InFight(True)

            
        clock.tick(60)
    
        screen.fill((0,0,0))
        #load sprites
        LoadSprites(Sprites.main, Sprites.enemy, Sprites.ground, Sprites.stairs, Sprites.ferin, playerOver.X, playerOver.Y, PlayMode.groundIs, testEnemy.X, testEnemy.Y, Partner.X, Partner.Y, Lay.layout, PlayMode.groundIs)
        pygame.display.update()
        
        #moves the player one tile if the tile is true
        if(PlayMode.inPlayMode == False):  
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    
                    if(PlayMode.groundIs[1] > -4):
                        if(event.key == pygame.K_w):
                            if(Lay.layout[0][PlayMode.groundIs[1] * 20 + PlayMode.groundIs[0] + 64] == 'true'):
                                Partner.Y = 328
                                Partner.X = 362
                                PlayMode.groundIs[1] -= 1
                    if(PlayMode.groundIs[1] < 15):
                        if(event.key == pygame.K_s):
                            if(Lay.layout[0][PlayMode.groundIs[1] * 20 + PlayMode.groundIs[0] + 104] == 'true'):
                                Partner.Y = 208
                                Partner.X = 362
                                PlayMode.groundIs[1] += 1
                    if(PlayMode.groundIs[0] > -4):
                        if(event.key == pygame.K_a):
                            if(Lay.layout[0][PlayMode.groundIs[1] * 20 + PlayMode.groundIs[0] + 83] == 'true'):
                                Partner.Y = 268
                                Partner.X = 442     
                                PlayMode.groundIs[0] -= 1
                    if(PlayMode.groundIs[0] < 15):
                        if(event.key == pygame.K_d):
                            if(Lay.layout[0][PlayMode.groundIs[1] * 20 + PlayMode.groundIs[0] + 85] == 'true'):
                                Partner.Y = 268
                                Partner.X = 282
                                PlayMode.groundIs[0] += 1
                    if(event.key == pygame.K_t):
                        running = False
                        Lay.levelAgain = True
                    
                    print(PlayMode.groundIs[1], PlayMode.groundIs[0], testEnemy.Y -5, testEnemy.X-5)
                    print(Lay.layout[0][PlayMode.groundIs[1]*20 + PlayMode.groundIs[0] + 84])
       
        
       
        #sees if player and enemy touch
        if(PlayMode.groundIs[0] == testEnemy.X -5 and PlayMode.groundIs[1] == testEnemy.Y-5):
            InFight(False)
            testEnemy.X = 200
            testEnemy.hasFought = True
            Music.musicPlayed = False
        
        if(Lay.layout[1][PlayMode.groundIs[1]*20+PlayMode.groundIs[0] + 84] == 'true' and testEnemy.hasFought == True):
            running = False
            testEnemy.hasFought = False
            Lay.levelAgain = True
            PlayMode.goneThrough += 1
        if(PlayMode.goneThrough == PlayMode.whenBoss):
            Cut.cutSceneStart = True
    
Ended()            

        