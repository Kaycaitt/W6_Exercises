cust_list = [] #so it can exist globally

class Rewards_Program:
    '''This class holds the names, phone numbers, and emails of customers.'''

    def __init__(self, cust_name, phone, email):
        self.name = cust_name #INDENTATION IS IMPORTANT
        self.phone = phone
        self.email = email
        self.restaurants_visited = {} #change to brackets to be a dictionary
        self.rewards_points = 0

    #adding methods
    def profile(self):
        print(f'''
            Name: {self.name}
            Phone: {self.phone}
            Email: {self.email} ''')
        
    def thank_you(self):
        print(f'Thank you, {self.name}, for visiting our restaurant!')

    def add_to_cust_list(self):
        global cust_list
        cust_list.append((self.name, self.phone, self.email))
    
    def visit_rest(self):
        restaurant_name = input("Please enter the name of the restaurant you have visited: ")
        if restaurant_name not in self.restaurants_visited:
            self.restaurants_visited[restaurant_name] = 0
        bill_total = float(input("What was the total food bill for this visit?: $"))
        self.rewards_points += int(bill_total)
        for i, x in self.restaurants_visited.items():
            print(f'{restaurant_name}: {self.rewards_points} points.')
        print(f'Points for this visit: {int(bill_total)}')
        print(f'Total rewards points earned: {self.rewards_points}')
        print(f'Thank you for visiting {restaurant_name}!')
        print("Total rewards points per restaurant: ")

c1 = Rewards_Program('Bonnie Bennett', '978-624-9634', 'bbennett@gmail.com')
c2 = Rewards_Program('Liv Parker', '465-328-7619', 'livparker@gmail.com')
c3 = Rewards_Program('Katerina Petrova', '642-716-4935', 'kpierce@yahoo.com')

c1.thank_you() #remember to add the parenthesis, otherwise methods will not be called/executed
c1.add_to_cust_list()
c1.visit_rest()
c1.visit_rest()
c1.visit_rest()
c2.thank_you()
c2.add_to_cust_list()
c2.visit_rest()
c3.thank_you()
c3.add_to_cust_list()
c3.visit_rest()

print(cust_list)
