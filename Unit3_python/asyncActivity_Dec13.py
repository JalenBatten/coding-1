def numberTypeDetector(number):
    if number < 0:
       print('This is a negative number.')
    elif number > 0:
       print('This is a positive number.')
    elif number == 0:
       print('This is zero.')
    
    
numberTypeDetector(-1)
numberTypeDetector(1)
numberTypeDetector(0)


def ticketCostToAge(age):
   if age <= 10 or age >= 65:
      print('Ticket costs $5.')
   elif age >= 16:
      print('Ticket costs $10.')

    
ticketCostToAge(10)
ticketCostToAge(16)
ticketCostToAge(65)


def memberShipDiscount(discount, price, item):
   if discount == 'superShopper':
      print(item,'is', 0.9*price)
   elif discount == 'megaShopper':
      print(item,'is', 0.85*price)
   elif discount == 'ultraShopper':
      print(item,'is', 0.8*price)
   else:
      print('Discount is invalid.')
  
  


memberShipDiscount('superShopper', 10, 'Vacuum')
memberShipDiscount('megaShopper', 1600, 'Tv')
memberShipDiscount('ultraShopper', 100, 'Gift Card' )
