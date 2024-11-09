# name = input('Please provide your name: ').lower() #to make output of name in lowercase
name = None
while name == None:
    try:
        name = input('Please provide your name: ').lower()
        int(name)
    except ValueError:
        pass
    else:
        print("Not a valid name (must be 2 or more letters long.)")
        name = None
n = None
while n == None:
    try:
        n = name[0]
    except IndexError:
        print(f'''Error:. '{name}' is not a valid name.''')
        raise SystemExit(0)

n1 = None
while n1 == None:
    try:
        n1 = name[1]
    except IndexError:
        print("Not a valid name (must be 2 or more letters long.)")
        raise SystemExit(0)    

def trunc_name(name2):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    n = name2[0] #index position of first letter
    n1 = name2[1] #index position of 2nd letter
    if n in vowels: #this is looking for the 1st position of a vowel in a name up to 2 consonants
        return name2
    elif n1 not in vowels:
        return name2[2:]
    else:
        return name2[1:]


# print(trunc_name(name))

def name_game(ngen):
    yield f'{ngen.capitalize()}, {ngen.capitalize()}, bo-b{trunc_name(name)}' #name name bo-
    yield f'banana fana fo-f{trunc_name(name)}' 
    yield f'me my mo-m{trunc_name(name)}'
    yield f'{ngen.capitalize()}!' #name


for i in name_game(name):
    print(i)

#the bonus
def name_game_b(b):
    yield f'{b.capitalize()}, {b.capitalize()}, bo-{trunc_name(name)}'
    yield f'banana fana fo-f{trunc_name(name)}'
    yield f'me my mo-m{trunc_name(name)}'
    yield f'{b.capitalize()}!'

def name_game_f(f):
    yield f'{f.capitalize()}, {f.capitalize()}, bo-{trunc_name(name)}'
    yield f'banana fana fo-{trunc_name(name)}'
    yield f'me my mo-m{trunc_name(name)}'
    yield f'{f.capitalize()}!'

def name_game_m(m):
    yield f'{m.capitalize()}, {m.capitalize()}, bo-b{trunc_name(name)}'
    yield f'banana fana fo-f{trunc_name(name)}'
    yield f'me my mo-{trunc_name(name)}'
    yield f'{m.capitalize()}!'

#initial errors thrown: (blank entry) index error at end
#initial errors thrown: (integers) no error, works and replaces with numbers
# initial errors thrown: (single letter) index error at end

#Question 7: For input that may be unexpected, but meets parameters so it's a silent error and the game can proceed. Maybe things like accented letters?

#Question 8: Raise is used to trigger exceptions automatically, so we would like to stop the program from proceeding if there is improper input.
#I think it's used rather than a break because it doesn't terminate the loop completely and move on to the next line of code. 