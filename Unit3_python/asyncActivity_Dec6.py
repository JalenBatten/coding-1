def flipWords(word):
    txt=word[::-1]
    print(txt)

print('Number 1')
flipWords('Hello')

print ('Number 2')
def stateLandmarks(state):
    if state == "Florida":
       print('A landmark in Flordia is Everglades National Park, and it is home to many rare and endangered species.')
    else: 
       print('Information for this state is not available.')
    

stateLandmarks("Florida")

stateLandmarks("California")


