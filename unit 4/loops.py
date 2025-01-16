# What are loops
# Python Loop is a programming concept where
# code repeats itself under specific conditions.

# In python, there are 2 versions of loops; for loop; and while loop.

# While Loops - A type of loop that will repeat a
# set of instructions so long as some condition is true.

normalAttack = 2 
specialAttack = 4
increaseHealth= 3

def battleFunction():
    hp = 10
    if hp > 0: 
        print('Do you want to attack')
        print(hp)
    normalAttack = 2 
    hp -= normalAttack
    keepGoing= input('Do you want to keep playing?')
    if keepGoing == 'y':
        print('run function again')
    else: 
          print('game over')
    
#battleFunction()


# For Loops- This is a type of loop that iterates over a collection
# of data and will run a specific set of instructions on data.

# for every number, we want to simply print it out.


numbers = [1,2,3,4,5,6,7,8]

for x in numbers:
     print(x)

attackValues=[10,25,59,90]

for attacks in attackValues:
     print('attack index')
     print(attacks*2)

# Create a functtion where items over $50 get a 10% discount
def shoppingDiscountFunction():
     shoppingCart=['demo']
     cartCount= len(shoppingCart)
     while cartCount > 0:
        customerItem= input('How much does this item cost?')
        shoppingCart.append(customerItem)
        print('here is the item price of your cart')
        print(shoppingCart)

shoppingDiscountFunction()