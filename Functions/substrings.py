name = 'Megan Thee Stallion'
blank_space = name.find(' ')
blank_space_2 = name.find(' ', blank_space + 1)
#since I added a middle name, I had to create a 2nd space variable so that it would pick up.
first_name = name[:blank_space]
middle_name = name[blank_space + 1:blank_space_2]
last_name = name[blank_space_2 + 1:]

print(f'''
    First Name: {first_name}
    Middle Name: {middle_name}
    Last Name: {last_name}''')

print(first_name + ' ' + middle_name + ' ' + last_name)