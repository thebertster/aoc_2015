import random

playerStart = {"hp":50, "mana":500, "armour":0}
bossStart = {"hp":71, "damage":10, "armour":0}

spells = [{"name":"Magic Missile", "cost":53, "actionStart":compile("boss['hp'] -= 4", "", "exec"), "action":None, "actionEnd":None, "length":0}, {"name":"Drain", "cost":73, "actionStart":compile("boss['hp'] -= 2\nplayer['hp'] += 2", "<string>", "exec"), "action":None, "actionEnd":None, "length":0}, {"name":"Shield", "cost":113, "actionStart":compile("player['armour'] += 7", "<string>", "exec"), "action":None, "actionEnd":compile("player['armour'] -= 7", "<string>", "exec"), "length":6}, {"name":"Poison", "cost":173, "actionStart":None, "action":compile("boss['hp'] -= 3", "<string>", "exec"), "actionEnd":None, "length":6}, {"name":"Recharge", "cost":229, "actionStart":None, "action":compile("player['mana'] += 101", "<string>", "exec"), "actionEnd":None, "length":5}]

minManaSpend = 9999
for spell in spells:
    if spell["cost"] < minManaSpend: minManaSpend = spell["cost"]

random.seed()

minMana = 99999
debug = False

while True:
    player = playerStart.copy()
    boss = bossStart.copy()
    manaSpent = 0
    activeSpells = []
    activeSpellNames = []
    spellList = []

    while True:
        if debug: print("Player's turn:", player, boss)
        # Player's turn

        player["hp"] -= 1

        if player["hp"] <= 0:
            if debug: print("Boss wins!", minMana)
            break

        finishedSpells = []

        for activeSpell in activeSpells:
            if activeSpell["action"] is not None:
                if debug: print(activeSpell["name"] + " in effect")
                exec(activeSpell["action"])
            activeSpell["length"] -= 1
            if activeSpell["length"] == 0:
                if debug: print(activeSpell["name"] + " ends")
                if activeSpell["actionEnd"] is not None: exec(activeSpell["actionEnd"])
                finishedSpells.append(activeSpell)

        for finishedSpell in finishedSpells:
            activeSpells.remove(finishedSpell)
            activeSpellNames.remove(finishedSpell["name"])

        if player["mana"] < minManaSpend:
            if debug: print("Player ran out of Mana", minMana)
            break

        if boss["hp"] <= 0:
            if manaSpent < minMana:
                minMana = manaSpent
                print(manaSpent)
            if debug: print("Player wins!", minMana)
            break

        while True:
            spell = random.choice(spells)
            if spell["cost"] <= player["mana"] and spell["name"] not in activeSpellNames: break

        player["mana"] -= spell["cost"]
        manaSpent += spell["cost"]
        spellList.append(spell["name"])

        if debug: print("Player casts " + spell["name"])

        if spell["actionStart"] is not None: exec(spell["actionStart"])
            
        if spell["length"] > 0:
            activeSpells.append(spell.copy())
            activeSpellNames.append(spell["name"])

        if boss["hp"] <= 0:
            if manaSpent < minMana:
                minMana = manaSpent
                print(minMana, spellList)
                if debug: input("")
            if debug: print("Player wins!", minMana)
            break

        if debug:
            print("End of player's turn:", player, boss)
            print()

        # Boss's turn

        if debug: print("Boss's turn", player, boss)

        finishedSpells = []

        for activeSpell in activeSpells:
            if activeSpell["action"] is not None:
                if debug: print(activeSpell["name"] + " in effect")
                exec(activeSpell["action"])
            activeSpell["length"] -= 1
            if activeSpell["length"] == 0:
                if debug: print(activeSpell["name"] + " ends")
                if activeSpell["actionEnd"] is not None: exec(activeSpell["actionEnd"])
                finishedSpells.append(activeSpell)

        for finishedSpell in finishedSpells:
            activeSpells.remove(finishedSpell)
            activeSpellNames.remove(finishedSpell["name"])

        if boss["hp"] <= 0:
            if manaSpent < minMana:
                minMana = manaSpent
                print(minMana, spellList)
                if debug: input("")
            if debug: print("Player wins!", minMana)
            break

        diff = boss["damage"] - player["armour"]
        player["hp"] -= diff if diff > 1 else 1
        if player["hp"] <= 0:
            if debug: print("Boss wins!", minMana)
            break

        if debug:
            print("End of boss's turn:", player, boss)
            print()
