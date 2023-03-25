print('Commission Calculator for Cricket')

accessories = int(input('How many accessories did you sell this week so far? '))
upgrades = int(input('How many upgrades have you sold this week? '            ))
activations = int(input('How many activations have you done this week? '      ))



def accessories_com(x):
    if x < 3:
        return 0
    elif 4 >= x >= 3:
        return x * 1.5
    elif  8 >= x > 4:
        return x * 2.5
    elif x > 9:
        return x * 3.5


def upgrades_com(x):
    if x < 2:
        return 0
    elif 4 >= x >= 2:
        return x * 3
    elif  7 >= x > 4:
        return x * 5
    elif x > 8:
        return x * 7


def activations_com(x):
    if x < 3:
        return 0
    elif 5 >= x >= 3:
        return x * 5
    elif  8 >= x > 5:
        return x * 7
    elif x > 9:
        return x * 10



acc = accessories_com(accessories)
ups = upgrades_com(upgrades)
act = activations_com(activations)

print("You have made")
print(" $",acc," by selling " ,accessories, "accessories")
print(" $",ups,"by selling" ,upgrades, "upgrades")
print(" $",acc,"by selling" ,activations, "activations")
print("bringing you to a grand total of $" ,acc+ups+act)