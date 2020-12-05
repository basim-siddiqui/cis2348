# Basim Siddiqui
# PSID: 1517778

import csv

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

def item_search(manufacturer, item_list, past_list):
    search_results = []
    for item in range(len(item_list)):
        if str(manufacturer) in str(item_list[item][1]):
            search_results.append(item_list[item])
    return search_results



# ~ reads inventory csv files by each line, each file opened calls make_sublists
with open('FullInventory.csv', 'r') as csvfile:
    inventory_list = csvfile.readlines()
    inventory_lists = make_sublists(inventory_list)

with open('LaptopInventory.csv', 'r') as csvfile:
    laptops_list = csvfile.readlines()
    laptop_lists = make_sublists(laptops_list)

with open('PhoneInventory.csv', 'r') as csvfile:
    phones_list = csvfile.readlines()
    phone_lists = make_sublists(phones_list)

with open('TowerInventory.csv', 'r') as csvfile:
    towers_list = csvfile.readlines()
    tower_lists = make_sublists(towers_list)

with open('PastServiceDateInventory.csv', 'r') as csvfile:
    pastdates_list = csvfile.readlines()
    past_service_lists = make_sublists(pastdates_list)

# ~ loop asks for user input to begin query search; if "q" is entered, the programs ends
search_prompt = ''
while search_prompt != 'q':
    print('\nSEARCH MENU\n'
          'q - Quit')
    search_prompt = input('Please enter the manufacturer and item type:\n')
    if search_prompt == 'q':
        break

    if 'Apple' in search_prompt or 'apple' in search_prompt:
        if 'phone' in search_prompt:
            apple_phone = item_search('Apple', phone_lists, past_service_lists)
            print(apple_phone)
        if 'laptop' in search_prompt or 'computer' in search_prompt:
            apple_laptop = item_search('Apple', laptop_lists, past_service_lists)
            print(apple_laptop)
        if 'tower' in search_prompt:
            apple_tower = item_search('Apple', tower_lists, past_service_lists)
            print(apple_tower)

    if 'Samsung' in search_prompt or 'samsung' in search_prompt:
        if 'phone' in search_prompt:
            samsung_phone = item_search('Samsung', phone_lists, past_service_lists)
            print(samsung_phone)
        if 'laptop' in search_prompt or 'computer' in search_prompt:
            samsung_laptop = item_search('Samsung', laptop_lists, past_service_lists)
            print(samsung_laptop)
        if 'tower' in search_prompt:
            samsung_tower = item_search('Samsung', tower_lists, past_service_lists)
            print(samsung_tower)

    if 'Dell' in search_prompt or 'dell' in search_prompt:
        if 'phone' in search_prompt:
            dell_phone = item_search('Dell', phone_lists, past_service_lists)
            print(dell_phone)
        if 'laptop' in search_prompt or 'computer' in search_prompt:
            dell_laptop = item_search('Dell', laptop_lists, past_service_lists)
            print(dell_laptop)
        if 'tower' in search_prompt:
            dell_tower = item_search('Dell', tower_lists, past_service_lists)
            print(dell_tower)

    if 'Lenovo' in search_prompt or 'lenovo' in search_prompt:
        if 'phone' in search_prompt:
            lenovo_phone = item_search('Lenovo', phone_lists, past_service_lists)
            print(lenovo_phone)
        if 'laptop' in search_prompt or 'computer' in search_prompt:
            lenovo_laptop = item_search('Lenovo', laptop_lists, past_service_lists)
            print(lenovo_laptop)
        if 'tower' in search_prompt:
            lenovo_tower = item_search('Lenovo', tower_lists, past_service_lists)
            print(lenovo_tower)
