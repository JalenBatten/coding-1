def listReverse():
    numberList = [1,23,56,3,56,3,20,200]
    listCount= 7
    while len(numberList) >= 0:
         numberList.reverse()
         print(numberList)
         break
         
          

     


listReverse()


def passwordLoops():
    userPassword=input('What is your password')
    passwordOne='ABC'
    passwordTwo=100.22
    while passwordOne != userPassword:
         print("Wrong password. Try again.")
         userPassword=input('What is your password')
         
    while passwordOne==userPassword:
         userPasswordTwo=float(input('What is your second password'))
         if userPasswordTwo == passwordTwo:
             print('You have successfully logged in.')
             break
         else:
              print('Wrong password. Try again') 
         userPasswordTwo=float(input('What is your second password'))
         
passwordLoops()
        