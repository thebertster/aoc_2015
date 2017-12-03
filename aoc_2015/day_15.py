def StarsAndBars(bins, stars):
    bars = [ ([0] * bins + [ stars ], 1) ]
    while len(bars)>0:
        b = bars.pop()
        if b[1] == bins:
            yield tuple(b[0][x] - b[0][x-1] for x in range(1, bins+1))
        else:
            bar = b[0][:b[1]]
            for x in range(b[0][b[1]], stars+1):
                newBar = bar + [ x ] * (bins - b[1]) + [ stars ]
                bars.append( (newBar, b[1]+1) )
            

def GetScore(quantities, ingredients):
    scores = {}
    for ingredient,spoons in quantities.items():
        for prop,v in ingredients[ingredient].items():
            if prop not in scores: scores[prop] = 0
            scores[prop] += spoons * v

    totalCalories = scores.pop("calories",0)

    if totalCalories == 500:

        totalScore = 1

        for x in scores.values():
            totalScore *= 0 if x<0 else x

        return totalScore
    else:
        return -1

ingredients = { "sugar":{"capacity":3, "durability":0, "flavour":0, "texture":-3, "calories":2}, "sprinkles":{"capacity":-3, "durability":3, "flavour":0, "texture":0, "calories":9}, "candy":{"capacity":-1, "durability":0, "flavour":4, "texture":0, "calories":1}, "chocolate":{"capacity":0, "durability":0, "flavour":-2, "texture":2, "calories":8} }

ingredientList = list(ingredients.keys())

numIngredients = len(ingredientList)

quantities = {}

highestScore = 0
highestScoreQuantities = {}

for s in StarsAndBars(3, 5):
    pass

input("")

for s in StarsAndBars(numIngredients, 100):
    print(s)
    input("")
    quantities = dict(zip(ingredientList, s))
    score = GetScore(quantities, ingredients)
    if score > highestScore:
        highestScore = score
        highestScoreQuantities=quantities
        
print(highestScore, highestScoreQuantities)
