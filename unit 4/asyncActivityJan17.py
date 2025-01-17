campingSupplies = ['tent','sleeping bag','flash light','camping knife']

def listReverse():
    campingSupplies.reverse()
    print(campingSupplies)

listReverse()

def addCampSupplies(item):
    campingSupplies.append(item)
    print(campingSupplies)

addCampSupplies('Lighter')

campingFood = ['marshmellows','gram crackers','chocolate','chicken hot dogs','water',]

def campListCombiner():
    campingSupplies.append(campingFood)
    print(campingSupplies)


campListCombiner()


def flashlightReplacement():
    campingSupplies.remove('flash light')
    campingSupplies.insert(1, 'camp fire kit')
    print(campingSupplies)

flashlightReplacement()