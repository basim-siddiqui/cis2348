# Basim Siddiqui
# PSID: 1517778

first_pass = input()
password = ""

for char in first_pass:
    if char == 'i':
        password += '!'
    elif char == 'a':
        password += '@'
    elif char == 'm':
        password += 'M'
    elif char == 'B':
        password += '8'
    elif char == 'o':
        password +='.'
    else:
        password += char

password += 'q*s'
print(password)
