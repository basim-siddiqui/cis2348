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

# ~ checks to see if user's input matches with existing manufacturer and item type within the inventory, returns results
def item_search(manufacturer, item_type, inventory, past_list):
    search_results = []
    # ~ appends item to results list if there is an item of the same type and manufacturer as inputted
    for item in range(len(inventory)):
        if inventory[item][1] in manufacturer and inventory[item][2] in str(item_type):
            search_results.append(inventory[item])
            # ~ if the item matches the search words but is damaged or past service date, it's removed from the search results
            for date in range(len(past_list)):
                if "damaged" in inventory[item][5] or inventory[item][4] in past_list[date][4]:
                    search_results.pop()
                    break
    return search_results

# ~ iterates through inventory list to find the same item type the user inputted from a different manufacturer
def item_recommendation(brand, item_type, price, inventory, past_list):
    rec_results = []
    same_type = []
    item_price = copy.deepcopy(price)
    min = int(price) * int(price)
    for entry in range(len(inventory)):
        if inventory[entry][2] == item_type:
            if inventory[entry][1] != brand:
                same_type.append(inventory[entry])
                # ~ if the item matches the search words but is damaged or past service date, it's removed from the same item type list
                for date in range(len(past_list)):
                    if "damaged" in inventory[entry][5] or inventory[entry][4] in past_list[date][4]:
                        same_type.pop()
                        break
    # ~ if the same_type list has elements, the loop assigns the item with the closest price to the search result to rec_results
    if len(same_type) > 0:
        for items in range(len(same_type)):
            price_diff = abs(int(item_price) - int(same_type[items][3]))
            if price_diff < int(min):
                min = price_diff
                rec_results = same_type[items]
    return rec_results


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
# ~ each item row is assigned as a sublist element to its corresponding dictionary key (the item type)
for key in type_items:
    for entry in range(len(type_rows)):
        if type_rows[entry][2] == key:
            type_items[key].append(type_rows[entry])


# ~ loop asks for user input to begin query search; if "q" is entered, the programs ends
search_prompt = ''
while search_prompt != 'q':
    print('\nSEARCH MENU\n'
          'q - Quit')
    # ~ asks user for BOTH manufacturer and item type; extra words are ignored
    search_prompt = input('Please enter the manufacturer and item type:\n')
    if search_prompt == 'q':
        break


# ~ splits user's input into individual words and stores it as a list
    search_prompt = search_prompt.split()
    found_items = []
# ~ iterates through the item_type dictionary to see if the user inputted a valid item type
    for key, values in type_items.items():
        if key in search_prompt:
            # ~ iterates through sublists in a specific dictionary
            for sublist in range(len(values)):
                # ~ iterates through the user's entered words
                for word in range(len(search_prompt)):
                    # ~ checks to see if the user entered a manufacturer that is carried in inventory
                    if search_prompt[word] in values[sublist][1]:
                        # ~ calls search_items function for finding the appropriate item
                        found_items = item_search(values[sublist][1], key, inventory_lists, past_service_lists)
                        break


    # ~ section of code runs a loops with conditional statements to make sure the user entered only one manufacturer and item type
    multiple_item = 0
    manufacturers = []
    check_rows = copy.deepcopy(inventory_lists)
    # ~ appends manufacturers from inventory list
    for items in check_rows:
        if items[1] not in manufacturers:
            manufacturers.append(items[1])
    # ~ checks if the user entered multiple manufacturers
    for word in search_prompt:
        for brands in manufacturers:
            if word in brands:
                multiple_item += 1
    # ~ checks if the user entered multiple item types
    for key, values in type_items.items():
        for word in range(len(search_prompt)):
            if key in search_prompt[word]:
                multiple_item += 1
    # ~ if there are more than one manufacturer and item type entered by the user, the found_items list is reset to zero elements
    if multiple_item > 2:
        found_items = []


    # ~ if the user searches for a manufacturer or item type that isn't carried or searches for multiple item types, this statement is made
    if len(found_items) == 0:
        found_items = 'No such item in inventory'
        print(found_items)
    # ~ if items are found within the inventory, the loop iterates for each item and finds the most expensive one
    elif len(found_items) > 0:
        max_price = [0, 0, 0, 0, 0, 0]
        for results in range(len(found_items)):
            if int(found_items[results][3]) > int(max_price[3]):
                max_price = found_items[results]

        # ~ outputs the item for the user in this format
        print("Your item is:", max_price[0], max_price[1], max_price[2], '${}'.format(max_price[3]))
        # ~ calls item recommendation function to search for items of the same type from another manufacturer
        consideration = item_recommendation(max_price[1], max_price[2], max_price[3], inventory_lists, past_service_lists)
        # ~ if the function returns a list with an item recommendation, it is printed
        if len(consideration) > 0:
            print("You may, also, consider:", consideration[0], consideration[1], consideration[2], '${}'.format(consideration[3]))