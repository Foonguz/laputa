from RPG import InFight
from MovementOfThings import Movement
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
playerOver = Player([False, False, 0], [False, False, 0])

class Enemy:
    X = 0
    Y = 0
    
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        
testEnemy = Enemy(400, 400)

class Lay(): 
    layout = []

class PlayMode:
    inPlayMode = False
    

#defs are here
def LoadSprites(main, enemy, OX, OY, EX, EY):
    screen.blit(enemy, (EX, EY))
    screen.blit(main, (OX[2], OY[2]))
    
    RandomGeneration(Lay.layout)
    print(Lay.layout)
        
screen = pygame.display.set_mode((800, 600))

running = True

#what happens when the game is actually running is here

clock = pygame.time.Clock()
while(running):
 
    clock.tick(60)

    screen.fill((0,0,0))
    LoadSprites(Sprites.main, Sprites.enemy, playerOver.X, playerOver.Y, testEnemy.X, testEnemy.Y)
    pygame.display.update()
    
    if(PlayMode.inPlayMode == False):
        Movement(playerOver.X, playerOver.Y, False)
    
    if(playerOver.X[2] <= testEnemy.X + 30 and playerOver.Y[2] <= testEnemy.Y + 50 and playerOver.X[2] >= testEnemy.X - 30 and playerOver.Y[2] >= testEnemy.Y - 50):
        print('why')
        PlayMode.inPlayMode = True
        
    if(PlayMode.inPlayMode):
        InFight()
        
    print(f'{playerOver.X[2]} {playerOver.Y[2]}')
    print(f'{testEnemy.X} {testEnemy.Y}')
    