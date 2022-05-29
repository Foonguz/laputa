import pygame
from SpritesOfThings import Sprites
from pygame import mixer
screen = pygame.display.set_mode((800, 600))

def Ended():
    
    mixer.music.load("End.mp3")
    mixer.music.play(-1)
    running = True
    
    while(running):
        screen.fill((0,0,0))
        screen.blit(Sprites.TBC, (50, 500))
        pygame.display.update()
        
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    running = False
                    pygame.display.quit()
                    pygame.quit()