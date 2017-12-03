def IncPassword(p):
    carry = True
    n = len(p)-1
    while carry:
        if p[n] == "z":
            p[n] = "a"
            n -= 1
        else:
            p[n] = chr(ord(p[n]) + 1)
            carry = False
    return p

password = list("hepxxyzz")

validPassword = False

while not validPassword:
    password = IncPassword(password)
    test1 = False
    test2 = True
    test3 = False

    for c in range(len(password)-2):
        if ord(password[c]) == ord(password[c+1])-1 == ord(password[c+2])-2: test1 = True
    if any(x in [ "i", "o", "l" ] for x in password): test2 = False
    pairs = 0
    for c in range(len(password)-1):
        if password[c] == password[c+1] and (c==0 or (c>0 and password[c] != password[c-1])): pairs = pairs + 1
    if pairs >= 2: test3 = True

    validPassword = test1 and test2 and test3

print(password)