import random
import copy
def RandomGeneration(layout):
    class Gen:
        level = []
        levelOld = []
        
        startPoint = 0
        startPointXY = [0, 0]
        amountOfRooms = 0
        
        bigRooms = 10
        corridor = [0, 0]
        madeCorridors = False
        whatRoomIsFirst = random.randrange(4)
    
    
    Gen.amountOfRooms = random.randrange(10)
    
    Gen.startPointXY[0] = random.randrange(20)
    Gen.startPointXY[1] = random.randrange(20)
    
    Gen.startPoint = int((float(Gen.startPointXY[0]) * 20 - 20) + float(Gen.startPointXY[1]))
    Gen.corridor = [copy.deepcopy(Gen.startPointXY[0]), copy.deepcopy(Gen.startPointXY[1])]
    
    for x in range(400):
       Gen.level.append('')
       if(x == Gen.startPoint):
           Gen.level[x] = 'true'
    
    for x in range(5):   
        while(Gen.bigRooms > 0):
            
            Gen.levelOld = copy.deepcopy(Gen.level)
            for x in range(400):
                    if(x < 380):
                        if(Gen.levelOld[x + 20] == 'true'):
                            Gen.level[x] = 'true'
                            Gen.bigRooms -= 1
                            
                    if(x > 19):
                        if(Gen.levelOld[x - 20] == 'true' and random.randrange(10) < 7):
                            Gen.level[x] = 'true'
                            Gen.bigRooms -= 1
                            
                    if(((x+1)/10).is_integer() == False):
                        if(Gen.levelOld[x + 1] == 'true' and random.randrange(10) < 7):
                            Gen.level[x] = 'true'
                            Gen.bigRooms -= 1
                            
                    if((x/10).is_integer() == False):
                        if(Gen.levelOld[x - 1] == 'true' and random.randrange(11) < 7):
                            Gen.level[x] = 'true'
                            Gen.bigRooms -= 1
                            
        while(Gen.madeCorridors == False):
            
            Gen.level[Gen.corridor[0] * 20 - 20 + Gen.corridor[1]] = 'true'
            
            if(Gen.startPointXY[0] > Gen.corridor[0]):
                Gen.corridor[0] += 1
            if(Gen.startPointXY[0] < Gen.corridor[0]):
                Gen.corridor[0] -= 1
            if(Gen.startPointXY[1] > Gen.corridor[1]):
                Gen.corridor[1] += 1
            if(Gen.startPointXY[1] < Gen.corridor[1]):
                Gen.corridor[1] -= 1
            if(Gen.corridor[0] == Gen.startPointXY[0] and Gen.corridor[1] == Gen.startPointXY[1]):
                Gen.madeCorridors = True
                            
        Gen.bigRooms = 10
        
        while(Gen.level[Gen.startPoint] == 'true'):
            Gen.startPointXY[0] = random.randrange(20)
            Gen.startPointXY[1] = random.randrange(20)
            
            Gen.startPoint = Gen.startPointXY[0] * 20 - 20 + Gen.startPointXY[1]
            
        Gen.level[Gen.startPoint] = 'true'
            
        Gen.madeCorridors = False
        
    Gen.amountOfRooms += -1
    
    for x in range(20):
        for y in range(20): 
            if(Gen.level[x*20+y] == 'true'):
                print('@ ', end='')
            else:
                print('# ', end='')
        print('')
    layout = Gen.level
        