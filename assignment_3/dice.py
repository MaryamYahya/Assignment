import random

dice=random.randint(1,6)
print(dice)
if dice==6:
    while True:
        dices=random.randint(1,6)
        print(dices)
        dice+=dices
        if dices!=6:
            break
print(f"sum of number:{dice}")