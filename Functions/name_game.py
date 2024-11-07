name = input('Please provide your name: ').lower() #to make output of name in lowercase

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