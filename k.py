def foo(arr : list[int]):
    l = [0,0]
    choice = False
    for i in range(len(arr)):
        l[choice] += max(arr)
        arr.remove(max(arr))
        choice = not(choice)
    return l

n = int(input())
arr = input().split()
arr = [int(i) for i in arr]
print(*foo(arr))