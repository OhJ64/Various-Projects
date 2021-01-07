#initalizes the computer and imports the random integer
from random import randint

#make options into list and computer chooses based on integer indexing
rpc = ["rock", "paper", "scissor"]
comp = rpc[randint(0,2)]

keepGoing = True

while keepGoing != False:
    choice = input("Choose either rock, paper, scissor or stop: ")

    #Exit out of the game
    if(choice == "stop"):
        keepGoing = False

    #both comp and user pick same choice
    elif(choice == comp):
        print("Lol it's a tie. the computer chose", comp)


    #user inputs an option of rock and comp outcome
    elif(choice == "rock"):
        if(comp == "scissor"):
            print("nice job, you won. comp chose", comp)
        else:
            print("son, you lost, computer chose", comp)
            
    #user inputs an option of scissor and comp outcome
    elif(choice == "scissor"):
        if(comp == "paper"):
             print("nice job, you won. comp chose", comp)
        else:
            print("son, you lost, computer chose", comp)

    #user inputs an option of paper and comp outcome
    elif(choice == "paper"):
        if(comp == "rock"):
             print("nice job, you won. comp chose", comp)
        else:
            print("son, you lost, computer chose", comp)

    #if user puts in something other than the 3 choices 
    else:
        print("Put in a valid option, you inputed something weird")

    #this line of code is imporant so the computer doesn't
    #give the same response and the person can repeat options.
    comp = rpc[randint(0,2)]    

    print("")


    
    
