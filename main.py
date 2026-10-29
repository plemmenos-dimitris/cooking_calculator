original_servings = float(input("HOW MANY SERVINGS DOES THE RECIPE MAKE: "))
while original_servings <= 0:
    print("THE SERVINGS MUST BE A POSITIVE NUMBER! ")
    original_servings = float(
        input("HOW MANY SERVINGS DOES THE RECIPE MAKE: "))

ingredients = int(input("HOW MANY INGREDIENTS DOES IT HAVE? "))
while ingredients <= 0:
    if ingredients == 0:
        print("YOU CAN'T MAKE A RECIPE WITHOUT ANY INGREDIENTS!")

    else:
        print("THE INGREDIENTS MUST BE A POSITIVE NUMBER! ")

    ingredients = int(input("HOW MANY INGREDIENTS DOES IT HAVE? "))

names = []
amounts = []
units = []

for i in range(ingredients):
    print(f"INGREDIENT {i+1}:")
    names.append(input("  NAME: "))
    amounts.append(float(input("  AMOUNT: ")))
    units.append(input("  UNIT(g, ml, pcs, tbsp,...): "))

print("1. I WANT TO CHANGE THE SERVINGS ")
print("2. I HAVE A LIMITED AMOUNT OF ONE INGREDIENT. ")
choice = input("CHOOSE 1 OR 2: ")
while choice != "1" and choice != "2":
    choice = input("PLEASE CHOOSE 1 OR 2: ")

if choice == "1":
    wanted_servings = float(input("HOW MANY SERVINGS DO YOU WANT? "))
    while wanted_servings < 0:
        print("THE SERVINGS CAN’T BE NEGATIVE! ")
        wanted_servings = float(input("HOW MANY SERVINGS DO YOU WANT? "))

    if wanted_servings == 0:
        print("THANKS FOR WASTING RESOURCES")

elif choice == "2":
    print("PLEASE CHOOSE A NUMBER FROM THE LIST")
    for i in range(len(names)):
        print(f"{i+1} {names[i]}")
    chosen_ingredient = int(input("""WHICH INGREDIENT : """))

    while chosen_ingredient < 1 or chosen_ingredient > ingredients:
        print("PLEASE CHOOSE A NUMBER FROM THE LIST")
        chosen_ingredient = int(input("""WHICH INGREDIENT : """))

    index = chosen_ingredient-1

    print(f"HOW MUCH {names[index]} DO YOU HAVE?")
    chosen_amount = float(input("- "))
    while chosen_amount < 0:
        print("THE AMOUNT CAN'T BE A NEGATIVE! ")
        print(f"HOW MUCH {names[index]} DO YOU HAVE?")
        chosen_amount = float(input("- "))
    wanted_servings = (chosen_amount*original_servings)/amounts[index]

k = wanted_servings/original_servings

if choice == "1":
    print(f"FOR {wanted_servings:g} SERVINGS YOU NEED: ")
    for i in range(len(names)):
        print(f"- {round(amounts[i]*k, 2):g} {units[i]} {names[i]}")

elif chosen_amount == 0:
    print(f"UNFORTUNATELY YOU CAN'T MAKE THE RECIPE WITHOUT {names[index]}")

else:
    print(
        f"FOR {chosen_amount:g} {units[index]} OF {names[index]} YOU NEED ({round(wanted_servings, 2):g} servings): ")
    for i in range(len(names)):
        if i != index:
            print(f"- {round(amounts[i]*k, 2):g} {units[i]} {names[i]}")
