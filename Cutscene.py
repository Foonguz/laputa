import pygame
from SpritesOfThings import Sprites 

pygame.font.init() 

screen = pygame.display.set_mode((800, 600))

readLine = open('Cutscene.txt', 'r')
my_font = pygame.font.SysFont('Comic Sans MS', 30)

#these are related to rendering text
class Reading: 
    value = readLine.readlines()
    text = my_font.render('Some Text', False, (0, 0, 0))
    SceneIsPlayingOut = True
    lineOn = 1
    enoughEnd = 0

#these are the positions of the charaters in cutscenes
class Chara: 
    lyeX = 300
    lyeY = 300
    
    ferinX = 600
    ferinY = 300

    


def loadSprites(whichScene):
    screen.fill((0,0,0))
    #this renders the charaters differently if it's on cutscene 0, 1 or 2
    if(whichScene == 0 or whichScene == 1):
        screen.blit(Sprites.main, (Chara.lyeX, Chara.lyeY))
        
        if(Reading.lineOn == 3):
            screen.blit(Sprites.moth, (Chara.ferinX - 10, Chara.ferinY))
        else:
            screen.blit(Sprites.cutsceneFerin, (Chara.ferinX, Chara.ferinY))
    
    if(whichScene == 2):
        screen.blit(Sprites.main, (Chara.lyeX, Chara.lyeY))
        
        if(Reading.lineOn == 18):
            screen.blit(Sprites.evilFerinDestoryed, (Chara.ferinX, Chara.ferinY))
        else: 
            screen.blit(Sprites.ferinDown, (Chara.ferinX, Chara.ferinY))
            screen.blit(Sprites.brokenMask, (500, 400))
         
    #this checks if the cutscene is over, if it is it ends it
    if(Reading.value[Reading.lineOn].strip('\n') != 'end'):
        if(Reading.value[Reading.lineOn].isdigit() == False):
            Reading.text = my_font.render(Reading.value[Reading.lineOn].strip('\n'), False, (255, 255, 255))
        else:
            #this adds 1 to the line if the cutscene hasn't ended
            print(Reading.lineOn, Reading.value[Reading.lineOn])
            Reading.lineOn += 1
    else:
        Reading.SceneIsPlayingOut = False
        
    screen.blit(Reading.text, (130,400))
        

    
def Scene(whichScene):         
    for x in range(len(Reading.value)):
            
        #this checks which cutscene the game is on
        if(Reading.enoughEnd == whichScene):
            Reading.lineOn = x
            Reading.enoughEnd = 50
        if(Reading.value[x].strip('\n') == 'end'):
            Reading.enoughEnd += 1
                
    #this loads the sprites
    while(Reading.SceneIsPlayingOut):
        loadSprites(whichScene)        
        pygame.display.update()
        
        
        #this adds 1 whenever e is pressed
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_e):
                    Reading.lineOn += 1
                    
    print(Reading.lineOn, Reading.value[Reading.lineOn])
    #this resets everything for next time
    Reading.SceneIsPlayingOut = True
    Reading.enoughEnd = 0
        