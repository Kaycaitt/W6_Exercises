# import os
# print("Current working directory:", os.getcwd()) #noting that working directory does not equal where the file is saved

pi = open(r"C:\Users\Mochi\YUU-LearnToCode\Data Analytics\Week_6\W6_Exercises\ReadWriteFiles\pi_million_digits.txt", "r") #put r in front of full path to treat as raw string
# print(pi.read(250))
pi_lines = pi.readlines()
# print(pi_lines)

user_birthday = input("Enter your birthday in the format MMDDYY: ") #no need to use int because values are already string

birthday_found = None

for i in pi_lines:
    if user_birthday in i:
        print("Your birthday is in the first million digits of pi!")
        birthday_found = 1
        break
    else:
        continue

#first two list items
# print(f'''First line: {pi_lines[0].strip()}\nLength of 1st: {len(pi_lines[0])}\nSecond line: {pi_lines[1].strip()}\nLength of 2nd: {len(pi_lines[1])}''')

pi_string = ''

for i in pi_lines:
    pi_string += i.strip()

if birthday_found != 1:
    print("Sorry, your birthday was not found in the first million digits of pi.")
else:
    birthday_position = pi_string.index(user_birthday) - 1
    #we are subtracting 1 so that 3 starts at -1 and after the ., we begin at index position 1 to feel human-readable
    print(f'Your birthday begins at decimal place {birthday_position}')
    
pi.close()