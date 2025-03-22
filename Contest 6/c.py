from itertools import combinations

def foo(S):
    n = len(S)
    total_sum = 0
    
    for i in range(n):
        for j in combinations(range(1, n), i): 
            expr = S[0]
            for k in range(1, n):
                if k in j:
                    expr += '+'
                expr += S[k]
            total_sum += eval(expr)
    
    return total_sum

s = input()
print(foo(s))
