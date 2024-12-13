

def welcomeMsgByTime(number, time):
    if time == 'am':
      print('good morning')
      print(str(number) + time)
    elif time == 'pm':
      print('good evening') 
      print(str(number) + time)
    elif number > 12:
       print("sorry, number can't be greater than 12")
    else:
       print('sorry, did not understand your input')

# welcomeMsgByTime(15,'pm')

# Create a functtion that will give someone a 
# letter grade based on their numerical grade score

def letterGrade(score):
   if score >= 90 and score <= 100 :
     print('A')
   elif score >= 80 and score < 90:
     print('B')
   elif score >= 70 and score < 80:
      print('C')
   elif score >= 60 and score < 70:
      print('D')
   elif score < 60:
      print('F')

letterGrade()