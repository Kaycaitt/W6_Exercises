import math
def conv_c_to_f(celsius): #this formula works for proper rounding/conversions
    f_to_c = round((celsius * 9/5) + 32)
    return f_to_c

celsius_temps = [100, 45, 19, 0, -7, -40] #list of temperatures to cycle through instead of long print statements

for temp in celsius_temps: #need a for statement to loop through list of temps
    fahrenheit_temp = conv_c_to_f(temp)

    print(f'Temperature in Celsius: {temp} = Temperature in Fahrenheit: {fahrenheit_temp}') #line must be indented, otherwise it just takes the argument of last item in list
