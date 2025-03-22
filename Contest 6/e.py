def foo(s, q):
    answers = []
    if len(s) < 4:
        answers = ["NO" for i in q]
        return answers
    
    for i in q:
        temp = s
        temp[int(i[0])] = i[1]
        if "1100" in temp:
            answers.append("YES")
        else:
            answers.append("NO")
    
    return answers


n = int(input())

l = []
for i in range(n):
    binary = input()
    q = int(input())
    q_list = []
    for i in range(q):
        q_list = input().split()
        l = l + foo(binary, q_list)

for i in l:
    print(i)