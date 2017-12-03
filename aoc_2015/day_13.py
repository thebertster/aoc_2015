import re
import itertools

input = [ "Alice would gain 54 happiness units by sitting next to Bob.", "Alice would lose 81 happiness units by sitting next to Carol.", "Alice would lose 42 happiness units by sitting next to David.", "Alice would gain 89 happiness units by sitting next to Eric.", "Alice would lose 89 happiness units by sitting next to Frank.", "Alice would gain 97 happiness units by sitting next to George.", "Alice would lose 94 happiness units by sitting next to Mallory.", "Bob would gain 3 happiness units by sitting next to Alice.", "Bob would lose 70 happiness units by sitting next to Carol.", "Bob would lose 31 happiness units by sitting next to David.", "Bob would gain 72 happiness units by sitting next to Eric.", "Bob would lose 25 happiness units by sitting next to Frank.", "Bob would lose 95 happiness units by sitting next to George.", "Bob would gain 11 happiness units by sitting next to Mallory.", "Carol would lose 83 happiness units by sitting next to Alice.", "Carol would gain 8 happiness units by sitting next to Bob.", "Carol would gain 35 happiness units by sitting next to David.", "Carol would gain 10 happiness units by sitting next to Eric.", "Carol would gain 61 happiness units by sitting next to Frank.", "Carol would gain 10 happiness units by sitting next to George.", "Carol would gain 29 happiness units by sitting next to Mallory.", "David would gain 67 happiness units by sitting next to Alice.", "David would gain 25 happiness units by sitting next to Bob.", "David would gain 48 happiness units by sitting next to Carol.", "David would lose 65 happiness units by sitting next to Eric.", "David would gain 8 happiness units by sitting next to Frank.", "David would gain 84 happiness units by sitting next to George.", "David would gain 9 happiness units by sitting next to Mallory.", "Eric would lose 51 happiness units by sitting next to Alice.", "Eric would lose 39 happiness units by sitting next to Bob.", "Eric would gain 84 happiness units by sitting next to Carol.", "Eric would lose 98 happiness units by sitting next to David.", "Eric would lose 20 happiness units by sitting next to Frank.", "Eric would lose 6 happiness units by sitting next to George.", "Eric would gain 60 happiness units by sitting next to Mallory.", "Frank would gain 51 happiness units by sitting next to Alice.", "Frank would gain 79 happiness units by sitting next to Bob.", "Frank would gain 88 happiness units by sitting next to Carol.", "Frank would gain 33 happiness units by sitting next to David.", "Frank would gain 43 happiness units by sitting next to Eric.", "Frank would gain 77 happiness units by sitting next to George.", "Frank would lose 3 happiness units by sitting next to Mallory.", "George would lose 14 happiness units by sitting next to Alice.", "George would lose 12 happiness units by sitting next to Bob.", "George would lose 52 happiness units by sitting next to Carol.", "George would gain 14 happiness units by sitting next to David.", "George would lose 62 happiness units by sitting next to Eric.", "George would lose 18 happiness units by sitting next to Frank.", "George would lose 17 happiness units by sitting next to Mallory.", "Mallory would lose 36 happiness units by sitting next to Alice.", "Mallory would gain 76 happiness units by sitting next to Bob.", "Mallory would lose 34 happiness units by sitting next to Carol.", "Mallory would gain 37 happiness units by sitting next to David.", "Mallory would gain 40 happiness units by sitting next to Eric.", "Mallory would gain 18 happiness units by sitting next to Frank.", "Mallory would gain 7 happiness units by sitting next to George." ]

regex = re.compile("^(.+) would (gain|lose) (\d+) happiness units? by sitting next to (.+)\.$")

people = { "Me":{} }

for i in input:
    iMatch = regex.match(i)
    if iMatch is not None:
        parsed = iMatch.regs
        p1 = i[parsed[1][0]:parsed[1][1]]
        gl = 1 if i[parsed[2][0]:parsed[2][1]] == "gain" else -1
        u = int(i[parsed[3][0]:parsed[3][1]])       
        p2 = i[parsed[4][0]:parsed[4][1]]
        if p1 not in people:
            people[p1] = {}

        people[p1][p2] = gl*u

for p in people.keys():
    if p != "Me":
        people["Me"][p] = 0
        people[p]["Me"] = 0

peopleList = list(people.keys())

perms = itertools.permutations(peopleList[1:])

maxHappiness = 0
maxHappinessArrangement = None

for perm in perms:
    happiness = people[peopleList[0]][perm[0]] + people[peopleList[0]][perm[-1]]
    for i in range(len(perm)):
        cur = perm[i]
        left = perm[i-1] if i>0 else peopleList[0]
        right = perm[i+1] if i<len(perm)-1 else peopleList[0]
        happiness += people[cur][left] + people[cur][right]
    if happiness > maxHappiness:
        maxHappiness = happiness
        maxHappinessArrangement = list(perm)
        maxHappinessArrangement.append(peopleList[0])

print(maxHappiness, maxHappinessArrangement)