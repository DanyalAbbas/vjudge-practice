def foo(x, arr):
    SummedValue = 1
    for i in arr:
        SummedValue *= (x-i)
    if SummedValue > 0:
        return "POSITIVE"
    elif SummedValue < 0:
        return "NEGATIVE"
    else:
        return 0


n, q = input().split()
arr = input().split()
arr = [int(i) for i in arr]
l = []
for i in range(int(q)):
    x = int(input()) 
    l.append(foo(x, arr))
for i in l:
    print(i)