def foo(a : int, b : int, c : int) -> str:
    d = {
        "A" : a,
        "B" : b,
        "C" : c
     }
    if max(d.values()) > 50:
        return max(d, key=d.get)
    else:
        return "NOTA"
    

     

n = int(input())
l = []
for i in range(n):
    a,b,c = input().split()
    a,b,c = int(a), int(b), int(c) 
    
    l.append(foo(a,b,c))
for i in l:
    print(i)