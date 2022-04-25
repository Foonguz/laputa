import pygame
import time
import random

from MovementOfThings import Movement
from SpritesOfThings import Sprites
from AttackPatterns import BulletMove
screen = pygame.display.set_mode((800, 600))

test = True 

class Bullet:
    bulletStorage = []
    indieBullets = [random.randrange(200, 570), random.randrange(250, 530)]

class Time: 
    newTime = time.time()
    oldTime = time.time()
    
class AttackMode: 
    attacking = True 

class Player:
    X = [False, False, 400]
    Y = [False, False, 300]
    

class GetOut:
    outOfPlayMode = False

def LoadSprites(RpgPlayer, main, enemy, enemyBullet, attackButton, OX, OY, bulletStorage, attacking):
    screen.fill((0,0,0))
    
    if(attacking == False):
        screen.blit(RpgPlayer, (OX[2], OY[2]))  
    else:
        screen.blit(attackButton, (368, 450))  
        
    screen.blit(enemyBullet, (bulletStorage[0][0], bulletStorage[0][1])) 
    screen.blit(main, (200, 120)) 
    screen.blit(enemy, (568, 158))
    
    
    pygame.display.update()
    

clock = pygame.time.Clock()

def inMenu():
     for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_e):
                AttackMode.attacking = False

def InFight():
    
    clock.tick(60)
    
    for x in range(10):
        Bullet.bulletStorage.append(Bullet.indieBullets)
        
    while(GetOut.outOfPlayMode == False):
        
        if(AttackMode.attacking == False):
            Time.newTime = time.time()
            if(Time.newTime > Time.oldTime + 10):
                AttackMode.attacking = True
                Time.oldTime = time.time()
                
                Player.X[0] = False
                Player.X[1] = False
                Player.Y[0] = False
                Player.Y[1] = False
                
                Player.X[2] = 400
                Player.Y[2] = 300
                
                Bullet.bulletStorage[0][0] = random.randrange(200, 570)
                Bullet.bulletStorage[0][1] = random.randrange(250, 530)
    
        if(AttackMode.attacking):
            inMenu()
        else:
            Movement(Player.X, Player.Y, True)
            BulletMove(Player.X, Player.Y, Bullet.bulletStorage)
            
            
        LoadSprites(Sprites.RpgPlayer, Sprites.main, Sprites.enemy, Sprites.enemyBullet, Sprites.attackButton, Player.X, Player.Y, Bullet.bulletStorage, AttackMode.attacking)
