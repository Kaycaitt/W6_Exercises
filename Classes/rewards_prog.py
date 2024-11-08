cust_list = [] #so it can exist globally

class Rewards_Program:
    '''This class holds the names, phone numbers, and emails of customers.'''

    def __init__(self, cust_name, phone, email):
        self.name = cust_name #INDENTATION IS IMPORTANT
        self.phone = phone
        self.email = email

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

c1 = Rewards_Program('Bonnie Bennett', '978-624-9634', 'bbennett@gmail.com')
c2 = Rewards_Program('Liv Parker', '465-328-7619', 'livparker@gmail.com')
c3 = Rewards_Program('Katerina Petrova', '642-716-4935', 'kpierce@yahoo.com')

c1.thank_you() #remember to add the parenthesis, otherwise methods will not be called/executed
c1.add_to_cust_list()
c2.thank_you()
c2.add_to_cust_list()
c3.thank_you()
c3.add_to_cust_list()

print(cust_list)
