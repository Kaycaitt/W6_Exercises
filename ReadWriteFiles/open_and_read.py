me = open("about_me.txt", "r")
lines = []
# # print(me.read(50)) #without character limit, prints the entire output of file
# # print(me.read(50))#2nd print statement continues after the first read limitation ends
# # print(me.readline(10)) #reads first 10 characters seemingly
# # print(me.readline()) #reads each line after the first readline individually as they appear in txt file.
# # for i in range (1,5): #this output takes the remaining lines and wraps them
# #     print(me.readline()) 
# # print(me.readlines()) #output is a list with the next lines separated by commas
# # print(me.readlines(1)) #output is similar to the above print statement, but it adds a blank list after the initial one
# # print(me.readlines(10)) #similar output to the above, but adds 2 blank lists after the initial. Commenting out first 2 statements gives me a list of the first escape charactered item in list.
# # print(me.readlines(100)) #content ends after 3 line of content "Klaus."
# print(me.readlines(-1)) #for me, it prints out the entire text include in the file in list format. Changing the negative to another negative number makes no difference.

read = me.read(50)

while True:
    line = me.readline()
    if not line:
        break
    lines.append(line.strip())

readlines = me.readlines(100)

print(f'''First 50 characters: {read}\nNext four lines, as list by line: {lines}\nNext 100 characters, as list by line, rounded up to complete lines: {readlines}''')

me.close()