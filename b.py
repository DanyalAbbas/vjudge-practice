def foo(k : int, arr : list[int]):
    output = ""
    for i in arr:
        if i <= k:
            output += "1"
            k -= i
        else:
            output += "0"
    return output



n = int(input())
l = []
for i in range(n):
    n1,k, = input().split()
    n1,k = int(n1), int(k)
    arr = input().split()
    arr = [int(i) for i in arr] 
    l.append(foo(k,arr))
for i in l:
    print(i)