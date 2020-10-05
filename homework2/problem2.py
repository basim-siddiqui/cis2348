# Basim Siddiqui
# PSID: 1517778

month_dict = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

input_file = open('inputDates.txt', 'r')
dates = input_file.readlines()

for line in dates:
        if '-1' in line:
            break
        str_div = line.split()
        digit = len(str_div)
        if digit != 3:
            continue
        m_str = str_div[0]
        d = str_div[1]
        da = d.split(',')
        day = da[0]
        year = str_div[2]
        if m_str not in month_dict:
            continue

        for ind in range(12):
            if line.find(month_dict[ind]) >= 0:
                m_num = str(ind+1)
                complete = m_num + '/' + day + '/' + year
                print(complete)

print('-1')
input_file.close()



