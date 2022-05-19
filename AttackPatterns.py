import pygame
clock = pygame.time.Clock()

#here is where bullet attack patterns are stored

def BulletMove(PlayerX, PlayerY, bulletStorage):      
    clock.tick(60)    
    
    #this specific pattern makes the bullet hone in on the player
    if(bulletStorage[0][0] < PlayerX[2]):
        bulletStorage[0][0] += 1
    else:
        bulletStorage[0][0] -= 1
    if(bulletStorage[0][1] < PlayerY[2]):
        bulletStorage[0][1] += 1
    else:
        bulletStorage[0][1] -= 1
        