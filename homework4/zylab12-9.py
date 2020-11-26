# Basim Siddiqui
# PSID: 1517778

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError as ex:
        age = 0

    # Get next line
    print('{} {}'.format(name, age))
    parts = input().split()
    name = parts[0]