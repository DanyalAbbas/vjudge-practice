from itertools import permutations

def foo(s):
    for i in permutations(s):
        print(i)
    

print(foo("voodoo"))