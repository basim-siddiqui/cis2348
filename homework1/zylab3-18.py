# Basim Siddiqui
# PSID: 1517778

import math
height = input("Enter wall height (feet):\n")
width = input("Enter wall width (feet):\n")
print("Wall area:", int(height) * int(width), "square feet")
paint = int(height) * int(width) / 350.0
print("Paint needed:", '{:.2f}'.format(paint), 'gallons')
cans = math.ceil(paint)
print("Cans needed:", cans, 'can(s)\n')
colors = {'red': 35, 'blue': 25, 'green': 23}
paint_color = input("Choose a color to paint the wall:\n")
print("Cost of purchasing", paint_color, 'paint:', '${}'.format(colors[paint_color] * cans))
