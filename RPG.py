import pygame
import time
import random
from pygame import mixer
from Cutscene import Scene 


from MovementOfThings import Movement
from SpritesOfThings import Sprites
from AttackPatterns import BulletMove
screen = pygame.display.set_mode((800, 600))

test = True 

#bullet is what the enemy uses to attack the player
class Bullet:
    bulletStorage = []
    indieBullets = [random.randrange(200, 570), random.randrange(250, 530)]
    damage = 0
    
#time counting
class Time: 
    newTime = time.time()
    oldTime = time.time()
    
#sees when attack and defense mode should activate, also sees when the battle should end
class AttackMode: 
    attacking = True 
    endAttack = 3

#the player posistion 
class Player:
    X = [False, False, 400]
    Y = [False, False, 300]
    

#checks if the player should return to normal mode
class GetOut:
    outOfPlayMode = False

#loads sprites according to their posistion
def LoadSprites(RpgPlayer, main, ferin, evilFerin, enemy, enemyBullet, attackButton, OX, OY, bulletStorage, attacking, bossBattle):
    screen.fill((0,0,0))
    
    if(attacking == False):
        screen.blit(RpgPlayer, (OX[2], OY[2]))  
    else:
        screen.blit(attackButton, (368, 450))  
        
    screen.blit(enemyBullet, (bulletStorage[0][0], bulletStorage[0][1])) 

    #this renders differently depending on if its the boss or not
    if(bossBattle == False):
        screen.blit(enemy, (568, 158))
        screen.blit(main, (200, 160))  
        screen.blit(ferin, (200, 60)) 
    else: 
        screen.blit(evilFerin, (568, 100))
        screen.blit(main, (200, 100)) 
    
    
    pygame.display.update()
    

clock = pygame.time.Clock()

def inMenu(bossBattle):
    #resets everything needed to reset to go from attack mode to defense mode
     for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_e):
                AttackMode.attacking = False
                AttackMode.endAttack -= 1
                AttackMode.musicPlayed = False
            
            #ends rpg mode if player has hit the enemy enough
            if(bossBattle == False):
                if(AttackMode.endAttack <= 0):
                    AttackMode.attacking = True
                    GetOut.outOfPlayMode = True
                    AttackMode.endAttack = 3
            elif(AttackMode.endAttack <= 0): 
                Scene(2)
                AttackMode.attacking = True
                GetOut.outOfPlayMode = True
                AttackMode.endAttack = 3
                

def InFight(bossBattle):
    print('yo')
    clock.tick(60)
    
    #this checks if its a normal enemy or the boss
    if(bossBattle == False):
        mixer.music.load("FightSong.mp3")
        mixer.music.play(-1)
    else:
        mixer.music.load('WhatsHisNameTheme.wav')
        mixer.music.play(-1)
    
    for x in range(10):
        #stores bullets in bulletstorage
        Bullet.bulletStorage.append(Bullet.indieBullets)
        
    #checks if rpg mode should be on
    while(GetOut.outOfPlayMode == False):
        
        #if the player is in defense mode this is true
        if(AttackMode.attacking == False):
            
            #returns player to attack mode if a certain amount of time has passed
            Time.newTime = time.time()
            if(Time.newTime > Time.oldTime + 7):
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
        
        #goes to menu if in attack mode
        if(AttackMode.attacking):
            
            inMenu(bossBattle)
            Time.oldTime = time.time()
        
        #moves player and bullet if in defense mode
        else:
            Movement(Player.X, Player.Y, True, Bullet.damage, Bullet.bulletStorage)
            BulletMove(Player.X, Player.Y, Bullet.bulletStorage, bossBattle)
            
        #loads all sprites
        LoadSprites(Sprites.RpgPlayer, Sprites.main, Sprites.ferin, Sprites.evilFerin, Sprites.enemy, Sprites.enemyBullet, Sprites.attackButton, Player.X, Player.Y, Bullet.bulletStorage, AttackMode.attacking, bossBattle)
    
    GetOut.outOfPlayMode = False
