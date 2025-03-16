def foo(a: str, b: str) -> bool:
    n = len(a)
    if len(b) != n:
        return "NO"

    i = 0
    j = n - 1

    while i < j and a[i] == b[i]:
        i += 1
    while j >= 0 and a[j] == b[j]:
        j -= 1

    if i < j:
        a_list = list(a)
        a_list[i], a_list[j] = a_list[j], a_list[i]
        a = ''.join(a_list)
    return "YES" if a == b else "NO"

a = input()
b = input()
print(foo(a,b))