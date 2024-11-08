class Restaurant:
    '''This class holds restaurant names and food types.'''

    def __init__(self, restaurantName, restaurantType):
        self.name = restaurantName
        self.type = restaurantType
        self.number_served = 0
        self.customer_ratings = []

#methods (INDENTATION UNDER THE CLASS MATTERS)
    def describe_rest(self):
        print(f'{self.name} serves {self.type}.')

    def rest_open(self):
        print(f'{self.name} is open.')

    def add_num_served(self):
        try:
            num_served = int(input("How many customers served today?: "))
            self.number_served += num_served
        except ValueError:
            print("Please enter a valid number.")

    def print_num_served(self):
        print(f'{self.name} has served {self.number_served} customers')

    def customer_rating(self):
        while True: #to account for numbers outside of what's required
            try:
                rating = int(input("How would you rate your experience today on a scale of 1-5 (5 being excellent)?: "))
                if rating <1 or rating >5:
                    print("Please enter a rating between 1 and 5.")
                    continue
                self.customer_ratings.append(rating) #use customer_ratings because its the attribute
                avg_ratings = sum(self.customer_ratings) / len(self.customer_ratings) #divide sum of ratings by the length of amount of ratings
                print(f'Your rating was {rating}. The average rating for this restaurant is {avg_ratings}')           
                break
            except ValueError:
                print("Please enter a valid number between 1 and 5.")

#3 instances
r1 = Restaurant("Donkin\' Dunnts", "Coffee and Doughnuts")
r2 = Restaurant("Taco Baco", "American Tacos")
r3 = Restaurant("Weedy\'s", "Fast Food")

#Calling instances

r1.describe_rest()
r1.rest_open()
r1.add_num_served()
r1.print_num_served()
r1.customer_rating()

r2.describe_rest()
r2.rest_open()
r2.add_num_served()
r2.print_num_served()
r2.customer_rating()

r3.describe_rest()
r3.rest_open()
r3.add_num_served()
r3.print_num_served()
r3.customer_rating()
