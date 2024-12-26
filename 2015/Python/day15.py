from itertools import product


def main():
    partOne()
    partTwo()


def partOne():
    file = open("Inputs/15.txt", "r")
    lines = [line.strip().split() for line in file]
    ingredients = {}
    for line in lines:
        name = line[0][:-1]
        capacity = int(line[2][:-1])
        durability = int(line[4][:-1])
        flavor = int(line[6][:-1])
        texture = int(line[8][:-1])
        calories = int(line[10])
        ingredients[name] = [capacity, durability, flavor, texture, calories]
    maxScore = 0
    ingredientNames = list(ingredients.keys())
    numIngredients = len(ingredientNames)
    for amounts in product(range(101), repeat=numIngredients):
        if sum(amounts) == 100:
            totalCapacity = totalDurability = totalFlavor = totalTexture = 0
            for i in range(numIngredients):
                totalCapacity += amounts[i] * ingredients[ingredientNames[i]][0]
                totalDurability += amounts[i] * ingredients[ingredientNames[i]][1]
                totalFlavor += amounts[i] * ingredients[ingredientNames[i]][2]
                totalTexture += amounts[i] * ingredients[ingredientNames[i]][3]
            totalCapacity = max(0, totalCapacity)
            totalDurability = max(0, totalDurability)
            totalFlavor = max(0, totalFlavor)
            totalTexture = max(0, totalTexture)
            score = totalCapacity * totalDurability * totalFlavor * totalTexture
            maxScore = max(maxScore, score)
    print(maxScore)


def partTwo():
    file = open("Inputs/15.txt", "r")
    lines = [line.strip().split() for line in file]
    ingredients = {}
    for line in lines:
        name = line[0][:-1]
        capacity = int(line[2][:-1])
        durability = int(line[4][:-1])
        flavor = int(line[6][:-1])
        texture = int(line[8][:-1])
        calories = int(line[10])
        ingredients[name] = [capacity, durability, flavor, texture, calories]

    maxScore = 0
    ingredientNames = list(ingredients.keys())
    numIngredients = len(ingredientNames)

    for amounts in product(range(101), repeat=numIngredients):
        if sum(amounts) == 100:
            totalCapacity = totalDurability = totalFlavor = totalTexture = totalCalories = 0
            for i in range(numIngredients):
                totalCapacity += amounts[i] * ingredients[ingredientNames[i]][0]
                totalDurability += amounts[i] * ingredients[ingredientNames[i]][1]
                totalFlavor += amounts[i] * ingredients[ingredientNames[i]][2]
                totalTexture += amounts[i] * ingredients[ingredientNames[i]][3]
                totalCalories += amounts[i] * ingredients[ingredientNames[i]][4]

            if totalCalories == 500:
                totalCapacity = max(0, totalCapacity)
                totalDurability = max(0, totalDurability)
                totalFlavor = max(0, totalFlavor)
                totalTexture = max(0, totalTexture)
                score = totalCapacity * totalDurability * totalFlavor * totalTexture
                maxScore = max(maxScore, score)

    print(maxScore)


if __name__ == '__main__':
    main()