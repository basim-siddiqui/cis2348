# Basim Siddiqui
# PSID: 1517778

month_dict = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
dates = []
user_val = 1
while user_val != -1:
    user_val = input("Enter a date in the format of Month Day, Year:\n")
    if '-1' in user_val:
        break
    else:
        dates.append(user_val)
        continue

for entry in dates:
    str_div = entry.split()
    digit = len(str_div)
    if digit != 3:
        print("Incorrect format, try again.")
        continue
    m_str = str_div[0]
    d = str_div[1]
    da = d.split(',')
    day = da[0]
    year = str_div[2]

    for ind in range(12):
        if entry.find(month_dict[ind]) >= 0:
            m_num = str(ind+1)
            complete = m_num + '/' + day + '/' + year
            print(complete)

print(user_val)



