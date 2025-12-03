import copy


def main():
    partOne()
    partTwo()


def getSpells():
    return {
        1: {"name": "Magic Missile", "cost": 53, "damage": 4, "heal": 0, "armor": 0, "effect": None},
        2: {"name": "Drain", "cost": 73, "damage": 2, "heal": 2, "armor": 0, "effect": None},
        3: {"name": "Shield", "cost": 113, "damage": 0, "heal": 0, "armor": 7, "effect": {"duration": 6, "type": "armor"}},
        4: {"name": "Poison", "cost": 173, "damage": 0, "heal": 0, "armor": 0, "effect": {"duration": 6, "type": "damage", "value": 3}},
        5: {"name": "Recharge", "cost": 229, "damage": 0, "heal": 0, "armor": 0, "effect": {"duration": 5, "type": "mana", "value": 101}}
    }


def applyEffects(player, boss, effects):
    for effect in effects:
        if effect["type"] == "damage":
            boss["hitPoints"] -= effect["value"]
        elif effect["type"] == "mana":
            player["mana"] += effect["value"]
        effect["duration"] -= 1
    effects[:] = [effect for effect in effects if effect["duration"] > 0]


def simulateRound(bossHp, playerHp, currentMana, shield, poison, restore, nextSpell, manaSpent, minMana):
    spells = getSpells()
    effects = []
    if shield > 0:
        effects.append({"type": "armor", "duration": shield, "value": 7})
    if poison > 0:
        effects.append({"type": "damage", "duration": poison, "value": 3})
    if restore > 0:
        effects.append({"type": "mana", "duration": restore, "value": 101})

    player = {"hitPoints": playerHp, "mana": currentMana}
    boss = {"hitPoints": bossHp, "damage": 9}

    applyEffects(player, boss, effects)
    if boss["hitPoints"] <= 0:
        return min(minMana, manaSpent)

    spell = spells[nextSpell]
    if player["mana"] < spell["cost"]:
        return minMana
    player["mana"] -= spell["cost"]
    player["hitPoints"] += spell["heal"]
    boss["hitPoints"] -= spell["damage"]
    if spell["effect"]:
        effects.append(copy.deepcopy(spell["effect"]))
    manaSpent += spell["cost"]

    applyEffects(player, boss, effects)
    if boss["hitPoints"] <= 0:
        return min(minMana, manaSpent)

    damage = max(1, boss["damage"] - player.get("armor", 0))
    player["hitPoints"] -= damage
    if player["hitPoints"] <= 0:
        return minMana

    for i in range(1, 6):
        minMana = simulateRound(boss["hitPoints"], player["hitPoints"], player["mana"],
                                shield - 1 if shield > 0 else 0,
                                poison - 1 if poison > 0 else 0,
                                restore - 1 if restore > 0 else 0,
                                i, manaSpent, minMana)
    return minMana


def partOne():
    file = open("Inputs/22.txt", "r")
    lines = [line.strip() for line in file]
    bossStats = [int(line.split(": ")[1]) for line in lines]
    boss = {"hitPoints": bossStats[0], "damage": bossStats[1]}
    player = {"hitPoints": 59, "mana": 500}
    minMana = float('inf')
    for i in range(1, 6):
        minMana = simulateRound(boss["hitPoints"], player["hitPoints"], player["mana"], 0, 0, 0, i, 0, minMana)
    print(minMana)


def partTwo():
    pass


if __name__ == '__main__':
    main()