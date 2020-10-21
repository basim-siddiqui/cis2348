# Basim Siddiqui
# PSID: 1517778

user_list = input().split()
new_list = []
for i in user_list:
    i = int(i)
    if i >= 0:
        new_list.append(i)

new_list.sort()
for i in new_list:
    print(i, end = ' ')
