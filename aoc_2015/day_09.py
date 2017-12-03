import itertools

input = [ "AlphaCentauri to Snowdin = 66", "AlphaCentauri to Tambi = 28", "AlphaCentauri to Faerun = 60", "AlphaCentauri to Norrath = 34", "AlphaCentauri to Straylight = 34", "AlphaCentauri to Tristram = 3", "AlphaCentauri to Arbre = 108", "Snowdin to Tambi = 22", "Snowdin to Faerun = 12", "Snowdin to Norrath = 91", "Snowdin to Straylight = 121", "Snowdin to Tristram = 111", "Snowdin to Arbre = 71", "Tambi to Faerun = 39", "Tambi to Norrath = 113", "Tambi to Straylight = 130", "Tambi to Tristram = 35", "Tambi to Arbre = 40", "Faerun to Norrath = 63", "Faerun to Straylight = 21", "Faerun to Tristram = 57", "Faerun to Arbre = 83", "Norrath to Straylight = 9", "Norrath to Tristram = 50", "Norrath to Arbre = 60", "Straylight to Tristram = 27", "Straylight to Arbre = 81", "Tristram to Arbre = 90" ]

allPlaces = set()
distances = {}

for i in input:
    s1 = i.split(" = ")
    places = sorted(s1[0].split(" to "))
    allPlaces.update(places)
    distances[":".join(places)] = int(s1[1])

minDistance = 9999999
maxDistance = 0

for route in itertools.permutations(allPlaces):
    distance = 0
    for r in range(len(route)-1):
        pair = sorted(route[r:r+2])
        distance += distances[":".join(pair)]
    if distance < minDistance: minDistance = distance
    if distance > maxDistance: maxDistance = distance

print(minDistance, maxDistance)
