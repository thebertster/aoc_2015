def Fight(boss, player):
    defender = boss.copy()
    attacker = player.copy()
    defender["name"] = "boss"
    attacker["name"] = "player"
    while True:
        diff = attacker["damage"] - defender["armour"]
        defender["hp"] -= diff if diff > 1 else 1
        if defender["hp"] <=0: return attacker["name"]

        attacker, defender = defender, attacker

def BuyStuff(playerStart, itemList):
    player = playerStart.copy()
    goldSpent = 0
    for i in itemList:
        goldSpent += i["cost"]
        player["damage"] += i["damage"]
        player["armour"] += i["armour"]
    return player, goldSpent

boss = {"hp":100, "damage":8, "armour": 2}
you = {"hp":100, "damage":0, "armour": 0}
weapons = {"Dagger":{"cost":8, "damage":4, "armour":0}, "Shortsword":{"cost":10, "damage":5, "armour":0}, "Warhammer":{"cost":25, "damage":6, "armour":0}, "Longsword":{"cost":40, "damage":7, "armour":0}, "Greataxe":{"cost":74, "damage":8, "armour":0}}
armour = {"Nothing":{"cost":0, "damage":0, "armour":0}, "Leather":{"cost":13, "damage":0, "armour":1}, "Chainmail":{"cost":31, "damage":0, "armour":2}, "Splintmail":{"cost":53, "damage":0, "armour":3}, "Bandedmail":{"cost":75, "damage":0, "armour":4}, "Platemail":{"cost":102, "damage":0, "armour":5}}
rings = {"Damage +1":{"cost":25, "damage":1, "armour":0}, "Damage +2":{"cost":50, "damage":2, "armour":0}, "Damage +3":{"cost":100, "damage":3, "armour":0}, "Defense +1":{"cost":20, "damage":0, "armour":1}, "Defense +2":{"cost":40, "damage":0, "armour":2}, "Defense +3":{"cost":80, "damage":0, "armour":3}}

ringNames = list(rings.keys())

minGold = 0

for weaponName, weaponData in weapons.items():
    for armourName, armourData in armour.items():
        player, goldSpent = BuyStuff(you, [weaponData, armourData])
        if goldSpent > minGold and Fight(boss, player) == "boss":
            minGold = goldSpent
            print(goldSpent, weaponName, armourName)
        for ringName1 in range(len(ringNames)):
            player, goldSpent = BuyStuff(you, [weaponData, armourData, rings[ringNames[ringName1]]])
            if goldSpent > minGold and Fight(boss, player) == "boss":
                minGold = goldSpent
                print(goldSpent, weaponName, armourName, ringNames[ringName1])
            for ringName2 in range(ringName1+1, len(ringNames)):
                player, goldSpent = BuyStuff(you, [weaponData, armourData, rings[ringNames[ringName1]], rings[ringNames[ringName2]]])
                if goldSpent > minGold and Fight(boss, player) == "boss":
                    minGold = goldSpent
                    print(goldSpent, weaponName, armourName, ringNames[ringName1], ringNames[ringName2])
            