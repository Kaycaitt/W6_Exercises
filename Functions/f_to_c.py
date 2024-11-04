import math
def conv_f_to_c(fahrenheit): #this formula works for proper rounding/conversions
    f_to_c = round((fahrenheit - 32) * 5/9)
    return f_to_c

fahrenheit_temps = [212, 90, 72, 32, 0, -40] #list of temperatures to cycle through instead of long print statements

for temp in fahrenheit_temps: #need a for statement to loop through list of temps
    celsius_temp = conv_f_to_c(temp)

    print(f'Temperature in Fahrenheit: {temp} = Temperature in Celsius: {celsius_temp}') #line must be indented, otherwise it just takes the argument of last item in list
