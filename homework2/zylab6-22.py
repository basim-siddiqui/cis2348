# Basim Siddiqui
# PSID: 1517778
co1 = int(input())
co2 = int(input())
ans1= int(input())
co3 = int(input())
co4 = int(input())
ans2 = int(input())
test = 0

for x in range(-10, 11):
    for y in range(-10, 11):
        if co1*x + co2*y == ans1 and co3*x + co4*y == ans2:
            print(x, y)
            test = 1
            break

if test == 0:
    print('No solution')

