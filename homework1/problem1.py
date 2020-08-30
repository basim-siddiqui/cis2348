# Basim Siddiqui
# PSID: 1517778
print("This program will calculate your age.\n")
current_date = input("Enter the current date by month, day, and year.")
birthday = input("Enter you birthday by month, day, and year.")

print("Current Day Information:")
cmonth, cday, cyear = current_date.split("/")
print(cmonth)
print(cday)
print(cyear)

print("Birthday Information:")
month, day, year = birthday.split("/")
print(month)
print(day)
print(year)

age = int(cyear) - int(year)
if int(cmonth) < int(month):
    age = age - 1
if int(cmonth) == int(month) and int(cday) < int(day):
    age = age - 1
print("You are", age, "years old.")

if cmonth == month and cday == day:
    print("Happy Birthday!")