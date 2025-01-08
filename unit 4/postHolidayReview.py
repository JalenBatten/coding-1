# Billing System Function
# Goal: To be able to check and see if a user is past due or up-to-date on their subscription.

def checkSubscription(userDueDate, userMoneyInAccount):
    if int(userDueDate) == 6:
        print('Payment Due')
    else: 
        print('payment still due')
    
    if userMoneyInAccount ==True:
        print('subscription is paid') 
    