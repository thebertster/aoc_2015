f = open("input8.txt", "r")

oLengthTotal = 0
pLengthTotal = 0
inQuotedString = False

parsedInput = []
curString = ""

while True:
    c = f.read(1)
    if c == "":
        break

    if inQuotedString:
        if c == '"':
            inQuotedString = False
            oLengthTotal += 1
            parsedInput.append(curString)
            curString = ""
        elif c == "\\":
            c = f.read(1)
            if c == "\\":
                curString += "\\"
                pLengthTotal += 1
                oLengthTotal += 2
            elif c == '"':
                curString += '"'
                pLengthTotal += 1
                oLengthTotal += 2
            elif c == "x":
                b = f.read(2)
                curString += chr(int(b, 16))
                pLengthTotal += 1
                oLengthTotal += 4
            else:
                oLengthTotal += 1
        else:
            curString += c
            pLengthTotal += 1
            oLengthTotal += 1
    else:
        if c == '"':
            inQuotedString = True
            oLengthTotal += 1

print(oLengthTotal - pLengthTotal)

f.seek(0)

oLengthTotal = 0
eLengthTotal = 0

for l in f.readlines():
    eLengthTotal += 1
    for c in l:
        if c == '\\' or c == '"': eLengthTotal += 1
        if c != '\n':
            eLengthTotal += 1
            oLengthTotal += 1
    eLengthTotal += 1

print(eLengthTotal - oLengthTotal)

f.close()

