import pygame
from SpritesOfThings import Sprites 

pygame.font.init() 

screen = pygame.display.set_mode((800, 600))

readLine = open('Cutscene.txt', 'r')
my_font = pygame.font.SysFont('Comic Sans MS', 30)

class Reading: 
    value = readLine.readlines()
    text = my_font.render('Some Text', False, (0, 0, 0))
    SceneIsPlayingOut = True
    lineOn = 1
    enoughEnd = 0

class Chara: 
    lyeX = 400
    lyeY = 300
    
    ferinX = 200
    ferinY = 300

    


def loadSprites(whichScene):
    screen.fill((0,0,0))
    if(whichScene == 0 or whichScene == 1):
        screen.blit(Sprites.main, (Chara.lyeX, Chara.lyeY))
        screen.blit(Sprites.ferin, (Chara.ferinX, Chara.ferinY))
        
    if(Reading.value[Reading.lineOn].strip('\n') != 'end'):
        if(Reading.value[Reading.lineOn].isdigit() == False):
            Reading.text = my_font.render(Reading.value[Reading.lineOn].strip('\n'), False, (255, 255, 255))
        else:
            print(Reading.lineOn, Reading.value[Reading.lineOn])
            Reading.lineOn += 1
    else:
        Reading.SceneIsPlayingOut = False
        
    screen.blit(Reading.text, (130,400))
        

        
def Scene(whichScene):         
    for x in range(len(Reading.value)):
            
        if(Reading.enoughEnd == whichScene):
            Reading.lineOn = x
            Reading.enoughEnd = 50
        if(Reading.value[x].strip('\n') == 'end'):
            Reading.enoughEnd += 1
                
    while(Reading.SceneIsPlayingOut):
        loadSprites(whichScene)        
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_e):
                    Reading.lineOn += 1
                    
    print(Reading.lineOn, Reading.value[Reading.lineOn])
    Reading.SceneIsPlayingOut = True
    Reading.enoughEnd = 0
        