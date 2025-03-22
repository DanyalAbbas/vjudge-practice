def foo(s : str, t : str) -> str:
    s = list(s)
    t = list(t)
    val = "No"
    for i in range(len(t)):
        t.insert(0, t.pop())
        if s == t:
            val = "Yes"
            break
    return val
    
s = input()
t = input()
print(foo(s,t))