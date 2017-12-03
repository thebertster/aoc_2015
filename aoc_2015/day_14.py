class Reindeer:
    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest
        self.flyingCounter = time
        self.restingCounter = 0
        self.distance = 0
        self.points = 0
    def DoTick(self):
        if self.flyingCounter > 0:
            self.distance += self.speed
            self.flyingCounter -= 1
            if self.flyingCounter == 0:
                self.restingCounter = self.rest
        else:
            self.restingCounter -= 1
            if self.restingCounter == 0:
                self.flyingCounter = self.time

import re

input = [ "Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.", "Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.", "Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.", "Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.", "Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.", "Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.", "Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.", "Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.", "Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds." ]

regex = re.compile("^(.+) can fly (\d+) km/s for (\d+) seconds?, but then must rest for (\d+) seconds?\.$")

reindeers = []

for reindeerRule in input:
    match = regex.match(reindeerRule)
    if match is not None:
        reindeerName = reindeerRule[match.regs[1][0]:match.regs[1][1]]
        reindeerSpeed = int(reindeerRule[match.regs[2][0]:match.regs[2][1]])
        reindeerTime = int(reindeerRule[match.regs[3][0]:match.regs[3][1]])
        reindeerRest = int(reindeerRule[match.regs[4][0]:match.regs[4][1]])
        reindeers.append(Reindeer(reindeerName, reindeerSpeed, reindeerTime, reindeerRest))

for t in range(2503):
    for r in reindeers:
        r.DoTick()
    maxDistance = -1
    winner = None
    for r in reindeers:
        if r.distance > maxDistance:
            maxDistance = r.distance
            winner = r
    winner.points += 1

for reindeer in reindeers:
    print("%s has gone %d km and has %d points" % (reindeer.name, reindeer.distance, reindeer.points))