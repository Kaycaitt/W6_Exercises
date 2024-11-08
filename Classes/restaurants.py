class Restaurant:
    '''This class holds restaurant names and food types.'''

    def __init__(self, restaurantName, restaurantType):
        self.name = restaurantName
        self.type = restaurantType

#methods (INDENTATION UNDER THE CLASS MATTERS)
    def describe_rest(self):
        print(f'{self.name} serves {self.type}.')

    def rest_open(self):
        print(f'{self.name} is open.')

#3 instances
r1 = Restaurant("Donkin\' Dunnts", "Coffee and Doughnuts")
r2 = Restaurant("Taco Baco", "American Tacos")
r3 = Restaurant("Weedy\'s", "Fast Food")

#Calling instances

r1.describe_rest()
r1.rest_open()
r2.describe_rest()
r2.rest_open()
r3.describe_rest()
r3.rest_open()
