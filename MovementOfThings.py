import pygame
from pygame import *
clock = pygame.time.Clock()

class Rects:
    playerRect = Rect(0, 0, 32, 32)
    box = Rect(0, 0, 250, 200)
    bullet = Rect(0,0,32,32)
    
    
def Movement(X, Y, isFighting):  
    clock.tick(60)
    
    for event in pygame.event.get():
        
        if(event.type == pygame.KEYDOWN):
            
            if(event.key == pygame.K_w):
                Y[1] = True
            if(event.key == pygame.K_s):
                Y[0] = True
            if(event.key == pygame.K_a):
                X[1] = True
            if(event.key == pygame.K_d):
                X[0] += True
                
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_w):
                Y[1] = False
            if(event.key == pygame.K_s):
                Y[0] = False
            if(event.key == pygame.K_a):
                X[1] = False
            if(event.key == pygame.K_d):
                X[0] = False
                
    Rects.playerRect = Rect(X[2], Y[2], 32, 32)
    Rects.box = Rect(370, 280, 200, 250)
    if(isFighting == False): 
        if(Y[1]):
            Y[2] += -5 
        if(Y[0]):
            Y[2] += 5
        if(X[1]):
            X[2] += -5 
        if(X[0]):
            X[2] += 5
    else:
        if(Y[1]):
            Y[2] += -5 
            if(Rects.playerRect.colliderect(Rects.box) == 0 and Y[2] < 240):
                Y[2] += 5
        if(Y[0]):
            Y[2] += 5
            if(Rects.playerRect.colliderect(Rects.box) == 0 and Y[2] > 530):
                Y[2] += -5
        if(X[1]):
            X[2] += -5 
            if(Rects.playerRect.colliderect(Rects.box) == 0 and X[2] < 200):
                X[2] += 5
        if(X[0]):
            X[2] += 5
            if(Rects.playerRect.colliderect(Rects.box) == 0 and X[2] > 570):
                X[2] += -5

        