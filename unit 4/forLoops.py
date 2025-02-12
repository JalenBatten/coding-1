# A For Loop is a type of loop that iterates over a list.
# It will go through your list and do whatever operation
# you want it to do

# for loops use and iterator, which is just a variable
# that is intended to repreesent a vaalue in the last. 

# the "IN" keyword gives us access to the list we want to go through

groceryList=['apple', 'water', 'milk', 'chicken']

def groceryFunction():
    for x in groceryList:
        if x == 'milk':
            continue
    print(x)

gradeList =[100,70,90,70,65,95]

def gradeRemove():
    for grade in gradeList:
        if grade < 75:
            continue
    print(grade)

for grade in gradeList:
    if grade == 6:
        gradeList.append(85)
    print(grade)
    




