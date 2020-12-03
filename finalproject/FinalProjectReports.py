# Basim Siddiqui
# PSID: 1517778

# ~ import csv module for csv file functionality, import time and datetime for past service dates file, import copy for duplicating lists
# ~ import operator for sorting the past service dates sublists
import csv
import copy
import time
from datetime import datetime
import operator


# ~ each entry in the full_inventory_list is turned into a sublist and appended to a new list to separate them by rows
def sort_inventory_rows(inv_list):
    rows = len(inv_list) // 6
    inv_rows = []
    inv_start = 0
    inv_end = 6
    for i in range(rows):
        inv_rows.append(inv_list[inv_start:inv_end])
        inv_start += 6
        inv_end += 6
    # ~ sorts inventory_rows alphabetically by manufacturer name
    l = len(inv_rows)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (inv_rows[j][1] > inv_rows[j + 1][1]):
                tempo = inv_rows[j]
                inv_rows[j] = inv_rows[j + 1]
                inv_rows[j + 1] = tempo
    return inv_rows

# ~ sorts the past_dates list from oldest to newest date
def sort_past_dates(old_dates):
    l = len(old_dates)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if datetime.strptime(old_dates[j][4], "%m/%d/%Y") > datetime.strptime(old_dates[j + 1][4], "%m/%d/%Y"):
                tempo = old_dates[j]
                old_dates[j] = old_dates[j + 1]
                old_dates[j + 1] = tempo
    return old_dates


# ~ reads manufacturer list csv file
with open('ManufacturerList.csv', 'r') as csvfile:
    #~seperates fields by comma
    manufacturer_list = csv.reader(csvfile, delimiter = ",")
    #~initialize lists based on input fields
    manufacturer_ids = []
    manufacturer_brands = []
    manufacturer_type = []
    damage_indicator = []
    #~append to lists by row
    for row in manufacturer_list:
        manufacturer_ids.append(row[0])
        manufacturer_brands.append(row[1])
        manufacturer_type.append(row[2])
        damage_indicator.append(row[3])



with open('PriceList.csv', 'r') as csvfile:
    price_list = csv.reader(csvfile, delimiter = ",")
    price_ids = []
    price_numbers = []
    for row in price_list:
        price_ids.append(row[0])
        price_numbers.append(row[1])


with open('ServiceDatesList.csv', 'r') as csvfile:
    service_date_list = csv.reader(csvfile, delimiter = ",")
    service_ids = []
    service_dates = []
    for row in service_date_list:
        service_ids.append(row[0])
        service_dates.append(row[1])


 # ~ dictionaries from split files based on respective item ID
brand_dict = dict(zip(manufacturer_ids, manufacturer_brands))
type_dict = dict(zip(manufacturer_ids, manufacturer_type))
damage_dict = dict(zip(manufacturer_ids, damage_indicator))
price_dict = dict(zip(price_ids, price_numbers))
service_dict = dict(zip(service_ids, service_dates))

 # ~ adds values to the list from dictionaries
full_inventory_list = []
for id in range(len(manufacturer_ids)):
    full_inventory_list.append(manufacturer_ids[id])
    for brand in brand_dict:
        if brand == manufacturer_ids[id]:
            full_inventory_list.append(brand_dict[brand])
    for itemtype in type_dict:
        if itemtype == manufacturer_ids[id]:
            full_inventory_list.append(type_dict[itemtype])
    for damage in damage_dict:
        if damage == manufacturer_ids[id]:
            full_inventory_list.append(damage_dict[damage])

# ~ section appends prices and service dates to the lists
for ids in range(len(full_inventory_list)):
    for priceID in sorted(price_dict):
        if priceID == full_inventory_list[ids]:
            full_inventory_list.insert(ids + 3, price_dict[priceID])
for prices in price_dict:
    if price_dict[prices] not in full_inventory_list:
        full_inventory_list.insert(-1, price_dict[prices])

for ids in range(len(full_inventory_list)):
    for serviceID in sorted(service_dict):
        if serviceID == full_inventory_list[ids]:
            full_inventory_list.insert(ids + 4, service_dict[serviceID])
for dates in service_dict:
    if service_dict[dates] not in full_inventory_list:
        full_inventory_list.insert(-1, service_dict[dates])

# ~ calls function to separate full_inventory_list into sublists and sort by manufacturer name
inventory_rows = sort_inventory_rows(full_inventory_list)


# ~ each sublist is written as a row into a FullInventory.csv file
with open('FullInventory.csv', 'w', newline='') as inv_file:
    writer = csv.writer(inv_file)
    writer.writerows(inventory_rows)

# ~ new lists are made to be written to corresponding item type files
# ~ deepcopy of inventory_rows to keep original list unmodified
laptops = []
phones = []
towers = []
others = []
type_rows = copy.deepcopy(inventory_rows)

for entry in range(len(type_rows)):
    if type_rows[entry][2] == "laptop" or type_rows[entry][2] == "Laptop":
        laptops.append(type_rows[entry])
    elif type_rows[entry][2] == "phone" or type_rows[entry][2] == "Phone":
        phones.append(type_rows[entry])
    elif type_rows[entry][2] == "tower" or type_rows[entry][2] == "Tower":
        towers.append(type_rows[entry])
    else:
        others.append(type_rows[entry])

for laptop in laptops:
    laptop.remove("laptop")
for phone in phones:
    phone.remove("phone")
for tower in towers:
    tower.remove("tower")
for other in others:
    del other[2]

# ~ sorts these lists by the item ID
laptops.sort()
phones.sort()
towers.sort()
others.sort()

# ~ if the item type lists have elements within them, csv files are output for the respective item type
if len(laptops) > 0:
    with open('LaptopInventory.csv', 'w', newline='') as laptop_file:
        writer = csv.writer(laptop_file)
        writer.writerows(laptops)
if len(phones) > 0:
    with open('PhoneInventory.csv', 'w', newline='') as phone_file:
        writer = csv.writer(phone_file)
        writer.writerows(phones)
if len(towers) > 0:
    with open('TowerInventory.csv', 'w', newline='') as tower_file:
        writer = csv.writer(tower_file)
        writer.writerows(towers)
if len(others) > 0:
    with open('OtherInventory.csv', 'w', newline='') as other_file:
        writer = csv.writer(other_file)
        writer.writerows(others)

# ~ iterates through inventory_rows and determines if the date listed has passed
past_dates = []
today = time.strftime("%m/%d/%Y")
str(today)
today = datetime.strptime(today, "%m/%d/%Y")
date_rows = copy.deepcopy(inventory_rows)
for entry in range(len(date_rows)):
    serv_date = date_rows[entry][4]
    str(serv_date)
    serv_date = datetime.strptime(serv_date, "%m/%d/%Y")
    if serv_date < today:
        past_dates.append(date_rows[entry])

past_dates_inventory = sort_past_dates(past_dates)

# ~ csv file of past service dates is written
with open('PastServiceDateInventory.csv', 'w', newline='') as dates_file:
        writer = csv.writer(dates_file)
        writer.writerows(past_dates_inventory)