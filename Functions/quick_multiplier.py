doubler = lambda n: n*2

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

tripler = lambda n: n*3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

def multipliers():
    return{
            "quadrupler": lambda x: x*4,
            "quintupler": lambda x: x*5,
            "sextupler": lambda x: x*6,
            "septupler": lambda x: x*7,
            "octupler": lambda x: x*8,
            "nonupler": lambda x: x*9,
            "decupler": lambda x: x*10
        }


multiplier_function = multipliers()
data = (8, -4, 'banana')

for name, lamb in multiplier_function.items():
    for value in data:
        try:
            result = lamb(value)
            print(f'{name} of {value} is {result}')
        except TypeError:
            print(f'{name} of {value} is not a valid operation')