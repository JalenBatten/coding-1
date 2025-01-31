# ROCK, PAPER, SCISSOR GAME APP
# You are working on a game concept with several 
# other engineers and you need to provide them with a
#  simple proof of concepts. 
# For now, you have suggested that your 
# game work on a RPS (rock, paper, scissors) loop. 
# When a user plays, rock, paper, or scissors, 
# the computer will randomly select one of the 3 
# options as well. Your program will then determine 
# who won, based on the values. The game should only 
# allow the player to play 3 hands, and inform the 
# player if the won or lost (best 2 out of 3 format.) 

#  1. What is the problem asking you to do?
"To create a rock papor scissors game with a best 2 out of 3 format."

# 2. What are some keywords and phrases ? 
"Loop, randomly select, 3 hands."
# 3. Is there input data that the question provides ?
"Take in the users RPS selection."

# 4. What is the desired output?
"Determing who won based on their selections"

# 5. Pseudocode Steps & Additional Notes 
# import random
# random.range()
# random.choice
# needs to determine
# need a variable to track if player or cpu won
# needs to have logic to determine who won or loss after 3 turns as well as ask the player if
# they want to play again
# We need to while loop
# we need to use if or else conditional statements



# Solution

def rock_paper_scissors_loop():
    userHand= input("Which hand would you like to choose?")
    hands=["Rock","Scissors", "Paper"]
    hp = 2
    cpuHp=2
    import random
    while userHand == "rock" or "scissors" or "paper":
         
         random.choice(hands)
         if hands == "Rock" and userHand == "scissors":
            print("You have lost this round. Computer chose", hands)
         
            
        
        
rock_paper_scissors_loop()
            

        
    
    