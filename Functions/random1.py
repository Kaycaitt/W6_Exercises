import random

sample_list = ['water', 'orange juice', 'cranberry juice', 'milk'] #needs to be created for the choiice method
sample_list2 = ['apple', 'banana', 'cherry', 'peach',
'plum', 'watermelon'] #Using this list for sample/shuffle method, had to use single quotes and not double

random_int = random.randint(0,100)
random_float = random.random() 

print(f'''{random_int}
{random_float}''')

random_choice = random.choice(sample_list)
random_choices = random.choices(sample_list)

print(f'''{random_choice}
{random_choices}''')

random_sample = random.sample(sample_list2, k=3)#k to return 3 of the items from the list

print(f'''{random_sample}''')

random_shuffle = random.shuffle(sample_list2)
print(sample_list2) #cannot print the random_shuffle variable as it will always return none. need to print the list itself to see changes
