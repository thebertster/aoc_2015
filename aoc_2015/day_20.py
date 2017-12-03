import math

def GetPresents(n):
    v = 0
    for i in range(1, 1 + math.floor(math.sqrt(n))):
        d, m = divmod(n, i)
        if m == 0:
            if d <= 50: v += 11 * i
            if i <= 50 and i != d: v+= 11 * d
    return v

target = 33100000

guess = target//22

found = target * 2

offset = 0
while guess > 0:
    presents = GetPresents(guess + offset)
    if presents >= target and guess + offset < found:
        found = guess + offset
        print(found, presents)
        guess = found//2
        print("GUESS = %d" % guess)
        offset = 0
    if offset > guess:
        print("REACHED: %d " % (guess+offset))
        guess = guess//2
        print("GUESS = %d" % guess)
        offset = 0
    else:
        offset += 1
