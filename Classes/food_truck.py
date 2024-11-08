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

class FoodTruck(Restaurant):
    '''This is a child class of the parent class Restaurant.'''
    def __init__(self, restaurantName, restaurantType):
        super().__init__(restaurantName, restaurantType)
        self.private_bookings = 'N'
        self.truck_location = ""

    def accepts_private_bookings(self):
        private_book = input("Does this food truck accept private bookings? Y/N: ").upper()
        self.private_bookings = private_book
        if private_book == 'Y':
            print("This food truck currently accepts private bookings.")
        else:
            print("This food truck does not accept private bookings.")

    def relocate_truck(self):
        curr_loc = input("Please enter street address, city of truck location: ")
        print(f'The truck is currently located at {curr_loc}.')


#3 instances
r1 = Restaurant("Donkin\' Dunnts", "Coffee and Doughnuts")
r2 = Restaurant("Taco Baco", "American Tacos")
r3 = Restaurant("Weedy\'s", "Fast Food")

ft1 = FoodTruck("Taco Truck", "Mexican")
ft2 = FoodTruck("Lobster Truck", "Seafood")
ft3 = FoodTruck("Ice Cream Truck", "Dairy")

#Calling instances
ft1.accepts_private_bookings()
ft1.relocate_truck()
ft2.accepts_private_bookings()
ft2.relocate_truck()
ft3.accepts_private_bookings()
ft3.relocate_truck()