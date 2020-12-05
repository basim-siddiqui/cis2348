# Basim Siddiqui
# PSID: 1517778

import csv


# ~ function removes "\n" from each line, splits each line with a comma delimiter, and appends it to a new list
def inv_sublists(inv_list):
    removed_space = []
    inventory_lines = []
    for line in inv_list:
        line = line.rstrip()
        if len(line) != 0:
            removed_space.append(line)
    for line in removed_space:
        removed_space = line.split(",")
        inventory_lines.append(removed_space)
    return inventory_lines

# ~ reads full inventory csv file by each line
with open('FullInventory.csv', 'r') as csvfile:
    # ~ seperates fields by comma
    inventory_list = csvfile.readlines()
    inventory_lists = inv_sublists(inventory_list)

print(inventory_lists)



item_prompt = ''
manu_prompt = ''
#while item_prompt != 'q' or manu_prompt != 'q':
    #print('\nMENU\n'
          #'Enter "q" at either prompt to quit this search.\n'
          #'Search for an item:\n')
    #manu_prompt = input('Please enter the manufacturer:\n')
    #item_prompt = input('Please enter the item type:\n')

#if manu_prompt == 'Apple':
    #if item_prompt == 'phone':
    #if item_prompt == 'laptop':
    #if item_prompt == 'tower':