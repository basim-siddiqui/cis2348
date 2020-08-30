# Basim Siddiqui
# PSID: 1517778

lem_juice = int(input("Enter amount of lemon juice (in cups):\n"))
water = int(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
serving = float(input("How many servings does this make?\n"))
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(serving), "servings")
print('{:.2f}'.format(lem_juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar")
print()
make = int(input("How many servings would you like to make?\n"))
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(make), "servings")
lem_juice = make / 3
print('{:.2f}'.format(lem_juice), "cup(s) lemon juice")
water = make * 2.6667
print('{:.2f}'.format(water), "cup(s) water")
agave = make / 2.4
print('{:.2f}'.format(agave), "cup(s) agave nectar")
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(make), "servings")
lem_juice = lem_juice / 16
print('{:.2f}'.format(lem_juice), "gallon(s) lemon juice")
water = water / 16
print('{:.2f}'.format(water), "gallon(s) water")
agave = agave / 16
print('{:.2f}'.format(agave), "gallon(s) agave nectar")
