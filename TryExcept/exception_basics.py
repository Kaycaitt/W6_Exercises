#value error
# try:
#    age = int(input("Please enter your age: "))
# except ValueError:
#     print("Please use numerical values for your input.")
# else:
#     print(f'Your age is: {age}')
# finally:
#     print("Let\'s try another one.")

# #name error
# names = 'Katherine Pierce'
# try:
#     ({name})
# except NameError:
#     print(f'This variable does not exist.')
# else:
#     print(f'Your name is {names}.')
# finally:
#     print('Let\'s try another one.')

#type error
# try:
#     result = 5 + "10"
# except TypeError:
#     print('Error: You cannot combine 2 or more data types.')
# else:
#     print(f'The result is: {result}')
# finally:
#     print('Let\'s try another one.')

#syntax error
try:
    var = print("Hello world!!")
    raise SyntaxError("This is a simulated syntax error.") #I couldn't figure out how to trigger a syntax error without manually raising it.
except SyntaxError:
    print('Please check your syntax!')
else:
    print('Code has completed successfully!')
finally:
    print(f'Let\'s try another one.')