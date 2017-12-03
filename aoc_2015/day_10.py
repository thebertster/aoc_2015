n1 = "1321131112"

for i in range(50):
    n2 = ""
    c = n1[0]
    r = 1
    for t in n1[1:]:
        if t == c:
            r += 1
        else:
            n2 += str(r) + c
            c = t
            r = 1
    n2 += str(r) + c
    n1 = n2

print(n1, len(n1))