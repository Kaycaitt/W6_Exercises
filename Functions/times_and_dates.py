import datetime

today = datetime.datetime.now()

print(f'''Today is {today.strftime("%A")}, {today.strftime("%B")} {today.strftime("%d")}, {today.strftime("%Y")}''')

my_birthday = datetime.date(1997, 11, 16)

print(f'''My birthday is {my_birthday.strftime("%m/%d/%Y")}''')

ninety_d = today + datetime.timedelta (days=90) #this is setting variable to calculate date 90 days from now

print(f'''90 days from today is {ninety_d.strftime("%B %d, %Y")}''')

dinner_time = datetime.time(18,30)#need to set time values similar to date values, no need for colon here, just list numbers

print(f'''Let's meet for dinner at {dinner_time.strftime("%H:%M %p")}''')