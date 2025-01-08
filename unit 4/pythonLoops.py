# Create a function that will determine what 
# level of education a college student is in, 
# based on the number of years they've been in school.

def gradeToTitle():
    year = int(input ('What grade are you in.'))
    if year == 1:
        print('You are a freshman in undergrad.')
    elif year == 2:
        print('You are a sophmore in undergrad.')
    elif year == 3:
        print('You are a junior in undergrad.')
    elif year == 4:
        print('You are a senior in undergrad.')
    elif year == 5 or year == 6:
        print('You are in a masters program and in grad school.')
    elif year >= 7 and year <= 10:
        print('you are in a doctorates program and in grad school.')
         
    else:
        print('Something went wrong. please check your input.')
    
gradeToTitle()