#!/usr/bin/env python3
''' Jacob Paquette vaccum02.py project -- Prof. Reagan - SLU'''

import random

# ---------------------------------------------------------------
def createCarpet(mySize=10, maxDirty=10):
    ''' return a list of length mySize containing ints from zero to
        maxDirty '''
    retVal = list()
    for i in range(0, mySize):
        retVal.append(random.randint(1, maxDirty))
    return retVal


# ---------------------------------------------------------------
def randomStartPosition(myCarpet):
    '''return a random position on the carpet, in 0...(len(carpet)-1) '''
    return random.randint(0, len(myCarpet) - 1)

# ---------------------------------------------------------------
def reportCarpet(myCarpet, myPosition=None):
    print('+' + '+----' * len(myCarpet) + '++')

    print('|', end='')
    for i in range(0, len(myCarpet)):
        if (i == myPosition):
            print(F"|*{myCarpet[i]:^3}", end='')
        else:
            print(F"|{myCarpet[i]:^4}", end='')
    print('||')

    print('+' + '+----' * len(myCarpet) + '++')


# ---------------------------------------------------------------
def canGoRight(myCarpet, myPosition):
    ''' return True if an agent at myPosition can go right and still remain
        on the carpet. '''
    return myPosition < (len(myCarpet) - 1)

    # ---------------------------------------------------------------


def canGoLeft(myCarpet, myPosition):
    ''' return True if an agent at myPosition can go right and still remain
        on the carpet '''
    return myPosition > 0
# ---------------------------------------------------------------
def isDirty(myCarpet, myPosition) :
    ''' return True if myCarpet is dirty at myPosition '''
    return myCarpet[myPosition] > 0
# ---------------------------------------------------------------
def goRight(myCarpet, myPosition) :
    '''return the new location for the agent if it moves right'''
    return min((myPosition+1), (len(myCarpet)-1))

# ---------------------------------------------------------------
def goLeft(myCarpet, myPosition) :
    '''return the new location for the agent if it moves left'''
    return max(0,myPosition-1)
# ---------------------------------------------------------------
def clean(myCarpet, myPosition) :
    ''' Clean the cell at myPosition on myCarpet, decrimenting the
        value by one'''
    myCarpet[myPosition] = max(myCarpet[myPosition]-1,0)
# ---------------------------------------------------------------
def runVacuum(myCarpet, myPosition) :
    ''' runs the vacuum program successfully '''
    START = 0
    GOINGRIGHT = 1
    GOINGLEFT = 2
    CLEANING = 3
    PARKING = 4
    DONE = 5
    stateText = ['START','GOINGRIGHT','GOINGLEFT','CLEANING',
                 'PARKING','DONE']
    position = myPosition
    time = 0
    state = START

    while (state != DONE ) and (time < 200) :
        print('Time:', time, 'Position:', position,
              'State:', stateText[state])
        reportCarpet(myCarpet,position)
        print()

        if state == START :
            if canGoRight(myCarpet,position) :
                state = GOINGRIGHT
            else :
                state = CLEANING
        elif state == GOINGRIGHT :
            position = goRight(myCarpet,position)
            if not canGoRight(myCarpet,position) :
                state = CLEANING
        elif state == GOINGLEFT :
            position = goLeft(myCarpet,position)
            state = CLEANING
        elif state == CLEANING :
            if isDirty(myCarpet,position) :
                clean(myCarpet,position)
            elif canGoLeft(myCarpet,position) :
                state = GOINGLEFT
            else :
                state = PARKING
        elif state == PARKING :
            state = DONE
        else :
            print('Error: invalid state ',state)
            state = DONE
                
        time = time +1
# ---------------------------------------------------------------
# MAIN Program
# ---------------------------------------------------------------
if __name__ == '__main__' :
    carpet = createCarpet()
    vacuumPosition = randomStartPosition(carpet)
    runVacuum(carpet, vacuumPosition)
# ---------------------------------------------------------------


