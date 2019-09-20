#####     Adam Mansuri - 160483248 - Computing Assignment

import time
import math
import sys


### These are the tiles with the frogs and toads in their original positions
tileList= ['F','F','F',' ','T','T','T']


### This code will show a demonstration for the user, so they know how to play the game. This will be presented as a selection in a menu that i will create later on.
def demonstration():
    print("The starting positions are: ")
    time.sleep(1)
    print("")
    print(tileList)
    time.sleep(1)
    print("")
    print("To win, you would have to move like below: ")
    time.sleep(1)
    print("")
    print(3,4,['F','F',' ','F','T','T','T'])
    print(5,3,['F','F','T','F',' ', 'T', 'T'])
    print(6,5,['F','F','T','F','T',' ','T'])
    print(4,6,['F','F','T',' ', 'T', 'F','T'])
    print(2,4,['F', ' ', 'T', 'F', 'T', 'F', 'T'])
    print(1,2,[' ', 'F','T','F','T','F','T'])
    print(3,1,['T','F',' ', 'F', 'T','F', 'T'])
    print(5,3,['T','F','T','F',' ', 'F', 'T'])
    print(7,5,['T','F','T','F','T','F',' '])
    print(6,7,['T','F','T','F','T',' ', 'F'])
    print(4,6,['T','F','T',' ', 'T', 'F','F'])
    print(2,4,['T',' ','T','F','T','F','F'])
    print(3,2,['T','T',' ','F','T','F','F'])
    print(5,3,['T','T','T','F', ' ', 'F','F'])
    print(4,5,['T','T','T', ' ', 'F','F','F'])
    time.sleep(1)
    print("")
    print("You have won!")


### Here i will use a method(function) to declare a method called correctMove and define it so that it has everything to do with when the user enters something correct.
### In this function i will have to define that the user can move into an empty tile next to the current tile or can jump across another frog/toad to the next empty tile.
### the 'tileList', 'fromTile' and 'toTile' will be passed on so i will put them in as the parameters
def correctMove(tileList,fromTile,toTile):  
    if tileList[toTile]!=' ':
        return False
    if tileList[fromTile] == 'F':
        if fromTile>toTile or abs(toTile-fromTile)>2:
            return False
    else:
        if fromTile<toTile or abs(toTile-fromTile)>2:
            return False
    return True


### This is a function which will be called when the user wins the game.
### The code looks complex but its simple. It consisted of me creating 2  boolean flags which were originally false then after the piece of code which defined the user to win, the boolean flag change to true.
def winGame():
    flag=False
    flag2=False
    for i in range(0,3):
        if tileList[i] =='F':
            flag= True
    for i in range(4,len(tileList)):
        if tileList[i]=='T':
            flag2= True
    if flag==True and flag2== True:
        return True



### Now i will create a function so that the user can quit the game. Again i will put this in a menu later on
def quitGame():
    print("Game Over, You Quit!")
    sys.exit(1)


### Now using all the above functions of correctMove and winGame, i will implement them inside the actual game. 
def startGame(tileList):
    print(tileList)
    print("From which tile: ")
    fromTile= int(input())-1   ### I did -1 because the list starts from index 0, and i want the user to select a number starting from 1 and not 0
    print("To which tile: ")
    toTile = int(input())-1

    correct=correctMove(tileList,fromTile, toTile)

    if correct:
        value= tileList[fromTile]
        tileList[toTile]= value
        tileList[fromTile] = ' '
        print("new tileList:\t",tileList)
    else:
        print("Invalid jump!")
        
    if winGame==True:
        print("Congratulation, you have won the game!")

        quitGame()




### I will create a function so that the user can replay the game. Again i will put this in a menu later on
def replayGame(tileList):
    print("Starting positions are: ", tileList)
    startGame(tileList)

### Now i will build a menu to increase user interaction so that they can select one of the 3 choices: 1)demonstration, 2)play the game or 3)quit the game. Hence, these 3 methods will be implemented inside the menu
###For this i will use a while loop which will contain nested if/else statements
while True:
    print("To quit the game press 2")
    print("To replay the game press 0")
    print("To see the demonstration press 1")
    print("Press 3 to continue game!")
    
    userSelection= int(input())

    if(userSelection)==2:
        quitGame()
    elif(userSelection)==0:
        replayGame(tileList)
    elif(userSelection)==1:
        demonstration()
    elif(userSelection)==3:
        print("Lets Continue!")
        startGame(tileList)
    else:
        print()

    














        
    
