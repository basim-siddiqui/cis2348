# Basim Siddiqui
# PSID: 1517778

import csv

frequency_dict = {}
user_file = input()

with open(user_file, 'r') as csv_file:
    readcsv = csv.reader(csv_file)
    for line in readcsv:
        for words in line:
            if words in frequency_dict:
                frequency_dict[words] = frequency_dict[words] + 1
            else:
                frequency_dict[words] = 1

for key in frequency_dict.keys():
    print(key + ' ' + str(frequency_dict[key]))
