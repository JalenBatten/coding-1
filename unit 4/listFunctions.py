# - We can store any data type inside of a list, including other lists.
# - We can store dupilcate data inside of lists.
# - We can located and access data in a list by its index position.
# - Lists are changable. We can add and remove things from them.

skii_trip_items=['snow boots', 'heavy coat']

# append() method - allows us to add items to a list
# the new added item will be added to the back of the 
# list.
# method is a type of function that can be used on objects
skii_trip_items.append('gloves')
skii_trip_items.append('thick socks')
print(skii_trip_items)

# the insert() method allows us to add an item to a list, 
# and also dictate what position that item will be at.
# insert takes two arguments, 
# the index where you want to place the data, and the actual data

skii_trip_items.insert(2,'goggles')

print(skii_trip_items)

# pop() is a method thatt allows us to remove the last item in a list
skii_trip_items.pop()
print(skii_trip_items)

# remove() method allows us to remove an item from the list
# based specifically on the data's value

skii_trip_items.remove('snow boots')
print(skii_trip_items)

# clear() method- allows us to remove or delete the entire list.

skii_trip_items.clear()
print(skii_trip_items)

# del function 
# del skii_trip_items

def clothingBySeason(): 
    clothingSelection= input('What are you wearing?')
    summerClothes=[]
    winterClothes=[]
    if clothingSelection == 'tee-shirt':
        summerClothes.append('tee-shirt')
        print('Here is your summer collection')
        print(summerClothes)


clothingBySeason()

def favoriteRestuarant():
    restuarants =['Wendys', 'Chick-fil-a','KFC']
    print(restuarants)
    response= input('WHat is your favorite restuarant?')
    print('your favorite restuarant is' + response)

favoriteRestuarant()
    