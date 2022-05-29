import pygame
import random
clock = pygame.time.Clock()

#here is where bullet attack patterns are stored

def BulletMove(PlayerX, PlayerY, bulletStorage, bossBattle):      
    clock.tick(60)    
    
    #this specific pattern makes the bullet hone in on the player
    
    bossAttack = 1
    
    if(bossBattle):
        bossAttack = 3
        
        if(random.randrange(4) == 1):
                bulletStorage[0][0] += 5
        if(random.randrange(4) == 2):
               bulletStorage[0][0] -= 5
        if(random.randrange(4) == 3):
               bulletStorage[0][1] += 5
        if(random.randrange(4) == 4):
               bulletStorage[0][1] -= 5
    
    if(bulletStorage[0][0] < PlayerX[2]):
        bulletStorage[0][0] += bossAttack
    else:
        bulletStorage[0][0] -= bossAttack
    if(bulletStorage[0][1] < PlayerY[2]):
        bulletStorage[0][1] += bossAttack
    else:
        bulletStorage[0][1] -= bossAttack

       