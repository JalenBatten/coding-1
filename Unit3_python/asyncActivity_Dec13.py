def numberTypeDetector(number):
    if number < 0:
       print('This is a negative number.')
    elif number > 0:
       print('This is a positive number.')
    elif number == 0:
       print('This is zero.')
    
    
# numberTypeDetector(-1)
# numberTypeDetector(1)
# numberTypeDetector(0)


def ticketCostToAge(age):
   if age <= 10 or age >= 65:
      print('Ticket costs $5.')
   elif age >= 16:
      print('Ticket costs $10.')

    
# ticketCostToAge(10)
# ticketCostToAge(16)
# ticketCostToAge(65)


def memberPrice(membership, price):
   print('function working')
   if membership == 'superShopper':
      discount= 0.1*price
      total = price- discount
      print(discount)
   elif membership == 'megaShopper':
      discount= 0.15*price
      print(discount)
   elif membership == 'ultraShopper':
      discount= 0.2*price
      print(discount)
      total = price- discount
      print(total)
   else:
      print('Discount is invalid.')

memberPrice('ultraShopper', 143);
  


# memberShipDiscount('superShopper', 10, 'Vacuum')
# memberShipDiscount('megaShopper', 1600, 'Tv')
# memberShipDiscount('ultraShopper', 100, 'Gift Card' )
