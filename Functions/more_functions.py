#first function
def display_mailing_label(name, address, city, state, zip):
    return(f'''{name}\n{address}\n{city}, {state} {zip}''')
#had to use an f statement, otherwise the lines don't print as intended
print(f'{display_mailing_label('Elena Gilbert', '5354 Mystic Lane', 'Mystic Falls', 'Virginia', '76294')}\n')

#second function
import math
def add_numbers(*args):
    total = 0
    args_list = ""
    first = True #using to isolate the first number in output

    for numbers in args: #creating for loop so that it'll return the numbers added by index position only
        total += numbers
        if not first:
            args_list += "+"
        args_list += str(numbers) #i needs to be converted to string bc cannot concat
        first = False #if this isn't set to false, it will not put the plus signs after the first number
    return(f'''{[args_list]} = {total}''') #putting brackets here so that it doesn't put them around the answer as well

print(f'''{add_numbers(5, 6, 9, 48)}\n''')

#third function
def display_receipt(total_due, amount_paid):
    change_due = amount_paid - total_due
    
    print(f'Total Due: $ {total_due:.2f}')
    print(f'Amount Paid: ${amount_paid:.2f}')
    
    if change_due < 0: #need if statement to calculate if change is due or not
        remaining_balance = -change_due#if remaining balance is negative print below statement with what needs to be paid
        print(f'Please pay the remaining balance of: ${remaining_balance:.2f}')
    else:
        print(f'Change due: ${change_due:.2f}')

try: #I want for users to input their own values
    total_due = float(input("Enter the total due: $"))
    amount_paid = float(input("Enter the amount paid: $"))
    display_receipt(total_due, amount_paid)
except ValueError:
    print("Please enter a valid number.") #ensures that only float numbers as values are excepted and nothing more