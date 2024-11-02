import random
import math
import statistics

#variables
vals1_100 = range(1,100)
vals_sample = random.sample (vals1_100, 75)
vals_choices = random.choices (vals1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

#Question 3: Use a combination of functions from all three models to create calculations that will support the following output:

sum_of_75 = math.fsum(vals_sample)
avg_of_75 = statistics.mean(vals_sample)
median_of_75 = statistics.median(vals_sample)

print(f'''_Experimenting with a subset of integers 1-100: \nSum of 75 sample values from 1 to 100: {sum_of_75}\nAverage of 75 sample values: {avg_of_75}\nMedian of 75 sample values: {median_of_75}\n''')

avg_of_200 = statistics.mean(vals_choices)
median_of_200 = statistics.median(vals_choices)
mode_of_200 = statistics.mode(vals_choices)
standard_of_200 = statistics.stdev(vals_choices)
variance_of_200 = statistics.variance(vals_choices)

print(f'''_Experimenting with a superset of 200 values, integers 1-100:\nAverage of 200 values: {avg_of_200}\nMedian of 200 values: {median_of_200}\nMode of 200 values: {mode_of_200}\nStandard deviation of 200 values: {standard_of_200}\nVariance of 200 values: {variance_of_200}''')

area = pi * (radius**2) #using ** to symbolize the square of a number / also have to add * between pi and radius equation so it evaluates properly
area_ceil = math.ceil(area) #created variables for the ceil/floor functions for the print statement
area_floor = math.floor(area)

print(f'''\n_Modeling a random circle:\nRadius = {radius}, area = {area_ceil}\nRadius = {radius}, area = {area_floor}''')