# Loops  A construct in programming 
# where instructions will repeat over and over
# until a specific condition is met.

# While - is a special type of loop where
# instructions will repeat themselves so long as 
# a condition is true.

def repeatMs():
    x=2 
    while x == 2:
       print('This message will repeat forever.')


def passwordLoops():
    correctPw= '123abc'
    userPw=''
    userPw= input('please enter your password')
    while userPw != correctPw:
        print('incorrect pw. Try again.')
        if userPw == correctPw:
           print('Congrats')

#passwordLoops()


def inventoryLoop():
    userInventory=[]
    pickupItem=input('Pick up item')
    while len(userInventory) < 4:
        userInventory.append(pickupItem)
        print('these are the items in your bag')
        print(userInventory)
        pickupItem=input('Pick up item')
        if len(userInventory) == 4:
            print('Max Inventory Storage')
            break

        
inventoryLoop()



def rngGame():
    import random
    randomNumber= random.randrange(1,11)
    print(randomNumber)
    userGuess=''
    while randomNumber != userGuess:
        userGuess= int(input("Guess a number from 1 through 10:"))
        print('Incorrect guess. Try again')
    else:
        print('Correct Guess')

# rngGame()



def passwordSystem():
    password='fastCar'
    userPassword=''
    whileusr 

