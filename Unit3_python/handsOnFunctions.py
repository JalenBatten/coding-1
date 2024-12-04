
# A function definition tells the computer
# the instructions on what we want to do with the data.

# data just means data types

# curly brackets = passing in data into 
# the function definition. This is formally
# called a parameter

# parameter = placeholder for data

def modifyMyName(name): 
    print('Your new modified name is the great '+ name)

# when we pass data into a function call an
# argument
# argument = evidence, facts, real data.

# modifyMyName('Jalen')

# Lesson on Conditional Statements 
# Conditional statements use the 'IF' and 'ELSE'
# keyswords to filter and create sepecific outcomes based on data.

def verifyAge(age):
    if age > 17 and  age < 20:
        print('Congrats you can buy GTA VI.')
    elif age > 20:
        print('Sorry, youre to old for this game.')
    else:
        print('Sorry, you need an adult to buy this game.') 
    

verifyAge(18)


def minuteConverter(hours): 
    print(hours*60," minutes")

 
minuteConverter(100)

# Conditional Statements

# food expiration software is an example of
# using conditional statements. If the food expires
# it needs to be thrown away, or else it can be eaten

def foodExpiration(month, date, year):
    expirationYear= 2026
    expirationMonth= 12
    expirationDate = 5
    if date > expirationDate and year > expirationYear and month > expirationMonth:
        print('throw food away')
    else: 
        print('food is still good')
    
foodExpiration(12,10,2027)


