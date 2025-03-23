def foo(n, x, y):
    i = 0
    h = min(x,y)

    val = n/h
    if val.is_integer():
        return int(val)
    else:
        return int(val)+1

cases = int(input())
l = []
for i in range(cases):
    n = int(input())
    x,y = input().split()
    x,y = int(x), int(y)
    l.append(foo(n,x,y))

for i in l:
    print(i)
    


