class PuzzleState:
    def __init__(self, prevPuzzleState, spell):
        self.prevPuzzleState = prevPuzzleState
        if prevPuzzleState == None:
            self.playerState = playerStart.copy()
            self.bossState = bossStart.copy()
            self.manaSpent = 0
            self.activeSpells = []
        else:  
            self.playerState = prevPuzzleState.playerState.copy()
            self.bossState = prevPuzzleState.bossState.copy()
            self.manaSpent = prevPuzzleState.manaSpent
        self.spell = spell
    def PlayState(self):
        boss = self.bossState
        player = self.playerState

        player["hp"] -= 1

        if player["hp"] <= 0: return 2

        activeSpells = []

        for activeSpell in self.prevPuzzleState.activeSpells:
            if activeSpell["length"] > 1:                    
                if self.spell["name"] == activeSpell["name"]: return 2
                activeSpellCopy = activeSpell.copy()
                activeSpellCopy["length"] -= 1
                activeSpells.append(activeSpellCopy)
            else:
                if activeSpell["actionEnd"] is not None: exec(activeSpell["actionEnd"])
            if activeSpell["action"] is not None: exec(activeSpell["action"])

        if boss["hp"] <= 0: return 1

        self.playerState["mana"] -= spell["cost"]
        self.manaSpent += self.spell["cost"]

        if self.spell["actionStart"] is not None: exec(self.spell["actionStart"])

        if boss["hp"] <= 0: return 1

        if self.spell["length"] > 0:
            activeSpells.append(self.spell.copy())

        self.activeSpells = []

        if activeSpells is not None:
            for activeSpell in activeSpells:
                if activeSpell["action"] is not None: exec(activeSpell["action"])
                if activeSpell["length"] > 1:
                    activeSpellCopy = activeSpell.copy()
                    activeSpellCopy["length"] -= 1
                    self.activeSpells.append(activeSpellCopy)
                else:
                    if activeSpell["actionEnd"] is not None: exec(activeSpell["actionEnd"])

        if boss["hp"] <= 0: return 1

        diff = boss["damage"] - player["armour"]
        player["hp"] -= diff if diff > 1 else 1
        if player["hp"] <= 0: return 2

        return 0

playerStart = {"hp":50, "mana":500, "armour":0}
bossStart = {"hp":71, "damage":10, "armour":0}

spells = [{"name":"Magic Missile", "cost":53, "actionStart":compile("boss['hp'] -= 4", "", "exec"), "action":None, "actionEnd":None, "length":0}, {"name":"Drain", "cost":73, "actionStart":compile("boss['hp'] -= 2\nplayer['hp'] += 2", "<string>", "exec"), "action":None, "actionEnd":None, "length":0}, {"name":"Shield", "cost":113, "actionStart":compile("player['armour'] += 7", "<string>", "exec"), "action":None, "actionEnd":compile("player['armour'] -= 7", "<string>", "exec"), "length":6}, {"name":"Poison", "cost":173, "actionStart":None, "action":compile("boss['hp'] -= 3", "<string>", "exec"), "actionEnd":None, "length":6}, {"name":"Recharge", "cost":229, "actionStart":None, "action":compile("player['mana'] += 101", "<string>", "exec"), "actionEnd":None, "length":5}]

puzzleStates = [PuzzleState(None, None)]

minMana = 999999

while len(puzzleStates) > 0:
    print(len(puzzleStates))
    newPuzzleStates = []
    for puzzleState in puzzleStates:
        if puzzleState.manaSpent < minMana:
            for spell in spells:
                newPuzzleState = PuzzleState(puzzleState, spell)
                if newPuzzleState.playerState["mana"] >= spell["cost"]:
                    outcome = newPuzzleState.PlayState()
                    if outcome == 0:
                        newPuzzleStates.append(newPuzzleState)
                    elif outcome == 1:
                        if newPuzzleState.manaSpent < minMana:
                            minMana = newPuzzleState.manaSpent
                            print("->", minMana)
    puzzleStates = newPuzzleStates
