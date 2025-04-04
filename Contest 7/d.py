def foo(arr):
    towers = []
    for i in arr[1::]:
        hmm = True
        for j in range(len(towers)):
            if i < towers[j]:
                towers[j] = i
                hmm = False
                break
        if hmm:
            towers.append(i)
    return len(towers)


n = input()
l = list(map(int, input().split()))
print(foo(l))

