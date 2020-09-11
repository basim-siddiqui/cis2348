# Basim Siddiqui
# PSID: 1517778

print("This program will calculate your age.\n")
current_date = input("Enter the current date by month, day, and year.\n")
birthday = input("Enter your birthday by month, day, and year.\n")

print("\n-Current Day-")
cmonth, cday, cyear = current_date.split("/")
print('Month:', cmonth)
print('Day:', cday)
print('Year:', cyear)

print("\n-Birthday-")
month, day, year = birthday.split("/")
print('Month:', month)
print('Day:', day)
print('Year:', year)

age = int(cyear) - int(year)
if int(cmonth) < int(month):
    age = age - 1
if int(cmonth) == int(month) and int(cday) < int(day):
    age = age - 1

print("\nYou are", age, "years old.")

if cmonth == month and cday == day:
    print("Happy Birthday!")
