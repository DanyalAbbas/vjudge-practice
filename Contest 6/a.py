def foo(arr):
    vals = (min(arr) + max(arr)) / 2

    if vals.is_integer(): 
        vals = [int(vals)]
    else:
        vals = [int(vals), int(vals) + 1]

    min_cost = float("inf")
    for x in vals:
        cost = sum((y - x) ** 2 for y in arr) 
        min_cost = min(min_cost, cost)

    return min_cost

n = int(input())
arr = list(map(int, input().split()))
print(foo(arr))
