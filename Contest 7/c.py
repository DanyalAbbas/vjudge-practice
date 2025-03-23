import math

def foo(n, k):
    return k *  (k - 1)**(n-1)

n, k = input().split()
print(foo(int(k), int(n)))