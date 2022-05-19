import random
import copy

#this is for generation of the level

def RandomGeneration(layout):
    class Gen:
        #these are used to check the current and past box
        level = []
        levelOld = []
        
        #this is the 'startpoint', the point in which a room starts
        startPoint = 0
        startPointXY = [0, 0]
        
        #this checks the amount of rooms that have been made
        amountOfRooms = 0
        
        #this makes rooms 10 blocks large
        bigRooms = 10
        
        #these values make corridors
        corridor = [0, 0]
        madeCorridors = False
    
    #this makes amount of rooms 1-5
    Gen.amountOfRooms = random.randrange(3) + 3
    
    #makes a random startpoint from 0-19
    Gen.startPointXY[0] = copy.deepcopy(random.randrange(19))
    Gen.startPointXY[1] = copy.deepcopy(random.randrange(19))
    
    #makes startpoint and startpoint XY the same
    Gen.startPoint = int((float(Gen.startPointXY[0]) * 20) + float(Gen.startPointXY[1]))
    print(Gen.startPointXY[0] * 20 + Gen.startPointXY[1])
    
    Gen.corridor = [copy.deepcopy(Gen.startPointXY[0]), copy.deepcopy(Gen.startPointXY[1])]
    
    for x in range(400):
    #makes all the level list and startpoint true
       Gen.level.append('')
       layout[1].append('')
       if(x == Gen.startPoint):
           Gen.level[x] = 'true'
           layout[1][x] = 'true'
    
    for x in range(Gen.amountOfRooms):   
        while(Gen.bigRooms > 0):
            
            Gen.levelOld = copy.deepcopy(Gen.level)
            for x in range(400):
                #checks if a tile is next to a true tile, in which case it becomes true
                    if(x < 380):
                        if(Gen.levelOld[x + 20] == 'true' and random.randrange(10) < 7):
                            Gen.level[x] = 'true'
                            Gen.bigRooms -= 1
                            
                    if(x > 19):
                        if(Gen.levelOld[x - 20] == 'true' and random.randrange(10) < 7):
                            Gen.level[x] = 'true'
                            Gen.bigRooms -= 1
                            
                    if(((x+1)/20).is_integer() == False):
                        if(Gen.levelOld[x + 1] == 'true' and random.randrange(10) < 7):
                            Gen.level[x] = 'true'
                            Gen.bigRooms -= 1
                            
                    if((x/20).is_integer() == False):
                        if(Gen.levelOld[x - 1] == 'true' and random.randrange(10) < 7):
                            Gen.level[x] = 'true'
                            Gen.bigRooms -= 1
                            
        while(Gen.madeCorridors == False):
            
            #makes corridors, this is where rooms connect to others
            Gen.level[Gen.corridor[0] * 20 + Gen.corridor[1]] = 'true'
            
            if(Gen.startPointXY[0] > Gen.corridor[0] and Gen.corridor[0] + 1 <= 20):
                Gen.corridor[0] += 1
                Gen.level[Gen.corridor[0] * 20 + Gen.corridor[1]] = 'true'
            if(Gen.startPointXY[0] < Gen.corridor[0] and Gen.corridor[0] - 1 >= 0):
                Gen.corridor[0] -= 1
                Gen.level[Gen.corridor[0] * 20 + Gen.corridor[1]] = 'true'
            if(Gen.startPointXY[1] > Gen.corridor[1] and Gen.corridor[1] + 1 <= 20):
                Gen.corridor[1] += 1
                Gen.level[Gen.corridor[0] * 20 + Gen.corridor[1]] = 'true'
            if(Gen.startPointXY[1] < Gen.corridor[1] and Gen.corridor[1] - 1 >= 0):
                Gen.corridor[1] -= 1
                Gen.level[Gen.corridor[0] * 20 + Gen.corridor[1]] = 'true'
            if(Gen.corridor[0] == Gen.startPointXY[0] and Gen.corridor[1] == Gen.startPointXY[1]):
                Gen.madeCorridors = True    
                
            
        Gen.bigRooms = 10
        
        #makes another startpoint 
        while(Gen.level[Gen.startPoint] == 'true'):
            Gen.startPointXY[0] = copy.deepcopy(random.randrange(19))
            Gen.startPointXY[1] = copy.deepcopy(random.randrange(19))
            
            Gen.startPoint = Gen.startPointXY[0] * 20 + Gen.startPointXY[1]
            layout[1][Gen.startPoint] = 'true'
             
        Gen.level[Gen.startPoint] = 'true'
        
            
        Gen.madeCorridors = False
        
        Gen.amountOfRooms += -1
    
    #prints out the finished product
    for x in range(20):
        for y in range(20): 
            if(Gen.level[x*20+y] == 'true'):
                print('@ ', end='')
            else:
                print('# ', end='')
        print('')
    layout[0] = Gen.level
        