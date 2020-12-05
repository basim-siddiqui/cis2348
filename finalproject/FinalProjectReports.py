# Basim Siddiqui
# PSID: 1517778

# ~ import csv module for csv file functionality, import time and datetime for past service dates file, import copy for duplicating lists
import csv
import copy
import time
from datetime import datetime


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
            # ~ strptime used again for comparing past service dates
            if datetime.strptime(old_dates[j][4], "%m/%d/%Y") > datetime.strptime(old_dates[j + 1][4], "%m/%d/%Y"):
                tempo = old_dates[j]
                old_dates[j] = old_dates[j + 1]
                old_dates[j + 1] = tempo
    return old_dates


# ~ reads manufacturer list csv file
with open('ManufacturerList.csv', 'r') as csvfile:
    # ~ seperates fields by comma
    manufacturer_list = csv.reader(csvfile, delimiter = ",")
    # ~ initialize lists based on input fields, same operation done for pricelist and servicedateslist csv files
    manufacturer_ids = []
    manufacturer_brands = []
    manufacturer_type = []
    damage_indicator = []
    # ~ append to lists by row, same operation done for pricelist and servicedateslist csv files
    for row in manufacturer_list:
        manufacturer_ids.append(row[0])
        manufacturer_brands.append(row[1])
        manufacturer_type.append(row[2])
        damage_indicator.append(row[3])


# ~ reads price list csv file
with open('PriceList.csv', 'r') as csvfile:
    price_list = csv.reader(csvfile, delimiter = ",")
    price_ids = []
    price_numbers = []
    for row in price_list:
        price_ids.append(row[0])
        price_numbers.append(int(row[1]))

# ~ reads service dates csv file
with open('ServiceDatesList.csv', 'r') as csvfile:
    service_date_list = csv.reader(csvfile, delimiter = ",")
    service_ids = []
    service_dates = []
    for row in service_date_list:
        service_ids.append(row[0])
        service_dates.append(row[1])


 # ~ dictionaries created from lists by their respective item ID
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

type_rows = copy.deepcopy(inventory_rows)
types = []
type_items = {}

for entry in range(len(type_rows)):
    if type_rows[entry][2] not in types:
        type_items[type_rows[entry][2]] = []

for key in type_items:
    for entry in range(len(type_rows)):
        if type_rows[entry][2] == key:
            type_items[key].append(type_rows[entry])

for key, value in type_items.items():
    with open('{}Inventory.csv'.format(key), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(value)


# ~ iterates through copied inventory_rows list and determines if the date listed has passed to append to past_dates list
past_dates = []
# ~ strftime method used from imported time module to fetch date when program runs
today = time.strftime("%m/%d/%Y")
str(today)
# ~ strptime method from imported datetime module to format today's date for comparison with service dates, used again for service dates in the for loop
today = datetime.strptime(today, "%m/%d/%Y")
date_rows = copy.deepcopy(inventory_rows)
for entry in range(len(date_rows)):
    serv_date = date_rows[entry][4]
    str(serv_date)
    serv_date = datetime.strptime(serv_date, "%m/%d/%Y")
    if serv_date < today:
        past_dates.append(date_rows[entry])

# ~ call function to sort the past service dates from oldest to most recent
past_dates_inventory = sort_past_dates(past_dates)

# ~ csv file of past service dates is written
with open('PastServiceDateInventory.csv', 'w', newline='') as dates_file:
        writer = csv.writer(dates_file)
        writer.writerows(past_dates_inventory)

# ~ create list of only damaged goods
damaged = []
damage_rows = copy.deepcopy(inventory_rows)
for entry in range(len(damage_rows)):
    if damage_rows[entry][5] == "damaged":
        damaged.append(damage_rows[entry])

# ~ removes the damaged indicator element from each sublist
for damaged_item in damaged:
    damaged_item.remove("damaged")

# ~ sort damaged items list by order of most expensive to least expensive
damaged.sort(key = lambda x: x[3], reverse=True)

# ~ csv file of damaged inventory is written
with open('DamagedInventory.csv', 'w', newline='') as damaged_file:
    writer = csv.writer(damaged_file)
    writer.writerows(damaged)