# Basim Siddiqui
# PSID: 1517778

import csv
import copy

# ~ function removes "\n" from each line, splits each line with a comma delimiter, and appends it to a new list
def make_sublists(inv_list):
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

def item_search(manufacturer, item_type, inventory, past_list):
    search_results = []
    for item in range(len(inventory)):
        if inventory[item][1] in manufacturer and inventory[item][2] in str(item_type):
            search_results.append(inventory[item])
            for date in range(len(past_list)):
                if "damaged" in inventory[item][5] or inventory[item][4] in past_list[date][4]:
                    search_results.pop()
                    break
    if len(search_results) == 0:
        search_results = 'No such item in inventory'
    return search_results



# ~ reads inventory csv files by each line, each file opened calls make_sublists
with open('FullInventory.csv', 'r') as csvfile:
    inventory_list = csvfile.readlines()
    inventory_lists = make_sublists(inventory_list)

with open('PastServiceDateInventory.csv', 'r') as csvfile:
    pastdates_list = csvfile.readlines()
    past_service_lists = make_sublists(pastdates_list)


# ~ dictionary key created for each item type from input files
type_rows = copy.deepcopy(inventory_lists)
types = []
type_items = {}
for entry in range(len(type_rows)):
    if type_rows[entry][2] not in types:
        type_items[type_rows[entry][2]] = []
# ~ each item is assigned as a sublist element to its corresponding dictionary key
for key in type_items:
    for entry in range(len(type_rows)):
        if type_rows[entry][2] == key:
            type_items[key].append(type_rows[entry])


# ~ loop asks for user input to begin query search; if "q" is entered, the programs ends
search_prompt = ''
while search_prompt != 'q':
    print('\nSEARCH MENU\n'
          'q - Quit')
    search_prompt = input('Please enter the manufacturer and item type:\n')
    if search_prompt == 'q':
        break

    search_prompt = search_prompt.split()

    for key, values in type_items.items():
        if key in search_prompt:
            for sublist in range(len(values)):
                for word in range(len(search_prompt)):
                    if search_prompt[word] in values[sublist][1]:
                        found_items = item_search(values[sublist][1], key, inventory_lists, past_service_lists)
                        print(found_items)
        else:
            print("No such item in inventory")
            break

