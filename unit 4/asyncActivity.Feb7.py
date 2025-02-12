# A "for" loop iterates over a collection of data and runs a specific set of instructions on it, 
# and a "while loop" will repeat a set of intructions as long as a condition is met.


# You would use a while loop for a login system.

def passwordSystem():
    userName = input('What is your user')
    name= 'Jalen'
    password="System"
    while userName == name:
        userPassword= input('What is your password?')
        if userPassword == password:
            print('You have successfully logged in.')
            break
            
# passwordSystem()

def graduationChecker():
    studentGrades=[72,85,70,88,92,98]
    for x in studentGrades:
        if x == max(studentGrades):
            print('Your highest grade is', max(studentGrades))
graduationChecker()

            





