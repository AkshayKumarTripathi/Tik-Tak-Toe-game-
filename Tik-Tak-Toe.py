#creating a tiktaktoe game 
#to see the functions and their work check the image in the folder

import random
import os

print("---------------------------------------------------------------------------------------------")
print("                                   welcome to tik tak toe                                    ")
print("---------------------------------------------------------------------------------------------")


def players(num=1):  #Takes in the Player names and also checks if the player wants to play again
    if num:
        playerlist=[]
        player1=input("enter the name of player 1")
        player2=input("enter the name of player 2")
        playerlist.append(player1)
        playerlist.append(player2)
        playerchooser(playerlist)
    print("thanks for playing!")

def playerchooser(playerlist):           #This function chooses a player randomly so that both the players have equal advantage
    i=random.randrange(0,2)     
    first=playerlist[i]
    print("{} will go first!".format(first))
    a=1
    if i==1:
        a=0
    second=playerlist[a]
    play(first,second)

def play(first,second):                               #creates a sample gameboard so that the player knows where to put the marker
    gameboard=[x for x in range(1,10)]
    char1=input("{} enter your character".format(first)).upper()
    char2=input("{} enter your character".format(second)).upper()
    x=0
    printer(gameboard)
    maingame(char1,char2,gameboard,first,second,x)

def maingame(c1,c2,gameboard,first,second,x):              #the function where the game runs and it is the main function
    while x<9:
        if x%2==0:
            placer=int(input(" {} where you want to put the character".format(first)))
        else:
            placer=int(input(" {} where you want to put the character".format(second)))
        
        if x%2==0 and verifier(placer,c1,c2,gameboard,x,first,second):
            gameboard.pop(placer-1)
            gameboard.insert(placer-1,c1)
            os.system("cls")
            printer(gameboard)
            if checker(gameboard,c1):
                print("{} has won!".format(first))
                players(int(input("want to play again? press 1 for yes and 0 for no")))
                break
        
        if x%2!=0 and verifier(placer,c1,c2,gameboard,x,first,second):
            gameboard.pop(placer-1)
            gameboard.insert(placer-1,c2)
            os.system("cls")
            printer(gameboard)
            if checker(gameboard,c2):
                print("{} has won!".format(second))
                players(int(input("want to play again? press 1 for yes and 0 for no")))
                break
        x+=1
    if x==9:
        print("the match was a draw....Want to play again? ")
        players(int(input("press 1 for yes and 0 for no")))


def printer(gameboard):         #Prints the game board
    print(gameboard[0],"|",gameboard[1],"|",gameboard[2])
    print(gameboard[3],"|",gameboard[4],"|",gameboard[5])
    print(gameboard[6],"|",gameboard[7],"|",gameboard[8])
    
def verifier(placer,c1,c2,gameboard,x,first,second):           #This function checks if the player is playing a valid miove
    if gameboard[placer-1]!=c1 and gameboard[placer-1]!=c2:
        return True
    else:
        print("The move is invalid enter the new number where you want to place the character")
        maingame(c1,c2,gameboard,first,second,x)
    
def checker(gameboard,character):                 #function which checks whether any player has won
    if gameboard[0]==gameboard[1]==gameboard[2]==character:
        return True
    if gameboard[3]==gameboard[4]==gameboard[5]==character:
        return True   
    if gameboard[6]==gameboard[7]==gameboard[8]==character:
        return True
    if gameboard[0]==gameboard[3]==gameboard[6]==character:
        return True
    if gameboard[1]==gameboard[4]==gameboard[7]==character:
        return True
    if gameboard[2]==gameboard[5]==gameboard[8]==character:
        return True
    if gameboard[0]==gameboard[4]==gameboard[8]==character:
        return True
    if gameboard[2]==gameboard[4]==gameboard[6]==character:
        return True
    else:   return False

players()
          



            

        
            
        
    
    