import itertools


def main():
    partOne()
    partTwo()


def getShop():
    weapons = [
        (8, 4, 0),  # Dagger
        (10, 5, 0),  # Shortsword
        (25, 6, 0),  # Warhammer
        (40, 7, 0),  # Longsword
        (74, 8, 0)  # Greataxe
    ]
    armor = [
        (13, 0, 1),  # Leather
        (31, 0, 2),  # Chainmail
        (53, 0, 3),  # Splintmail
        (75, 0, 4),  # Bandedmail
        (102, 0, 5),  # Platemail
        (0, 0, 0)  # Nothing
    ]
    rings = [
        (25, 1, 0),  # Damage +1
        (50, 2, 0),  # Damage +2
        (100, 3, 0),  # Damage +3
        (20, 0, 1),  # Defense +1
        (40, 0, 2),  # Defense +2
        (80, 0, 3),  # Defense +3
        (0, 0, 0),  # Nothing 1
        (0, 0, 0)  # Nothing 2
    ]
    return weapons, armor, rings


def simulateBattle(php, pdmg, parmr, bhp, bdmg, barmr):
    while True:
        bhp -= max(1, pdmg - barmr)
        if bhp <= 0:
            return True
        php -= max(1, bdmg - parmr)
        if php <= 0:
            return False


def partOne():
    weapons, armor, rings = getShop()
    file = open("Inputs/21.txt", "r")
    lines = [line.strip() for line in file]
    bossStats = [int(line.split(": ")[1]) for line in lines]
    boss = {"hitPoints": bossStats[0], "damage": bossStats[1], "armor": bossStats[2]}
    minCost = float('inf')
    for weapon in weapons:
        for arm in armor:
            for r1, r2 in itertools.combinations(rings, 2):
                cost = weapon[0] + arm[0] + r1[0] + r2[0]
                pdmg = weapon[1] + arm[1] + r1[1] + r2[1]
                parmr = weapon[2] + arm[2] + r1[2] + r2[2]
                if simulateBattle(100, pdmg, parmr, boss["hitPoints"], boss["damage"], boss["armor"]):
                    minCost = min(minCost, cost)
    print(minCost)


def partTwo():
    weapons, armor, rings = getShop()
    file = open("Inputs/21.txt", "r")
    lines = [line.strip() for line in file]
    bossStats = [int(line.split(": ")[1]) for line in lines]
    boss = {"hitPoints": bossStats[0], "damage": bossStats[1], "armor": bossStats[2]}
    maxCost = 0
    for weapon in weapons:
        for arm in armor:
            for r1, r2 in itertools.combinations(rings, 2):
                cost = weapon[0] + arm[0] + r1[0] + r2[0]
                pdmg = weapon[1] + arm[1] + r1[1] + r2[1]
                parmr = weapon[2] + arm[2] + r1[2] + r2[2]
                if not simulateBattle(100, pdmg, parmr, boss["hitPoints"], boss["damage"], boss["armor"]):
                    maxCost = max(maxCost, cost)
    print(maxCost)


if __name__ == '__main__':
    main()