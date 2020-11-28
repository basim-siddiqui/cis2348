# Basim Siddiqui
# PSID: 1517778

#import csv module for csv file functionality
import csv

class Items:
    def __init__(self):
        self.dict = {}
        self.itemID = ''
        self.manufacturer = []
        self.itemType = []
        self.price = []
        self.serviceDate =[]
        self.damaged = []

    def itemID(self, itemID):
        print(itemID)


with open('ManufacturerList.csv', 'r') as csvfile:
    manufacturer_list = csv.reader(csvfile, delimiter = ",")
    row_num = 1
    manufacturer_list_fields = Items()
    for row in manufacturer_list:
        manufacturer_list_fields.itemID = row

with open('PriceList.csv', 'r') as csvfile:
    price_list = csv.reader(csvfile, delimiter = ",")
    row_num = 1
    for row in price_list:
        print(row)
        row_num += 1

with open('ServiceDatesList.csv', 'r') as csvfile:
    service_date_list = csv.reader(csvfile, delimiter = ",")
    row_num = 1
    for row in service_date_list:
        print(row)
        row_num += 1