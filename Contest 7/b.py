def foo(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    for i in s1:
        if i in s2:
            return "YES"
    
    return "NO"

cases = int(input())
l = []
for i in range(cases):
    s1 = input()
    s2 = input()
    l.append(foo(s1,s2))

for i in l:
    print(i)