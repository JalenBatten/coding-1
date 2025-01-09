# Create a function that will determine what 
# level of education a college student is in, 
# based on the number of years they've been in school.

def gradeToTitle():
    year = int(input ('What grade are you in.'))
    if year == 0:
        print(collegeTitles[0])
    collegeTitles= ['You dont have a college title yet', 'freshman', 'sophmore', 'junior', 'senior']
    if year == 1:
        print(collegeTitles[1])
    elif year == 2:
        print(collegeTitles[2])
    elif year == 3:
        print(collegeTitles[3])
    elif year == 4:
        print(collegeTitles[4])
    elif year == 5 or year == 6:
        print('You are in a masters program and in grad school.')
    elif year >= 7 and year <= 10:
        print('you are in a doctorates program and in grad school.')
         
    else:
        print('Something went wrong. please check your input.')
    
gradeToTitle()


# A list is a data type for collecting
# and organizng other data types.
# You create a list with a variable name and by square brackets.

listB = [10, 102, 4904]

listOfData = ['words and characters', 10, 10.2324, True, False, listB]

# print(listOfData)

collegeTitles= ['You dont have a college title yet', 'freshman', 'sophmore', 'junior', 'senior']

