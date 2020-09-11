# Basim Siddiqui
# PSID: 1517778

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")
auto_service = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 'No service'}

service1 = input("Select first service:\n")
service2 = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")
if service1 != '-' and service2 != '-':
    print("Service 1:", '{},'.format(service1), '${}'.format(auto_service[service1]))
    print("Service 2:", '{},'.format(service2), '${}'.format(auto_service[service2]))
    total_price = auto_service[service1] + auto_service[service2]
    print('\nTotal:', '${}'.format(total_price))
elif service1 == '-' and service2 != '-':
    print("Service 1:", auto_service[service1])
    print("Service 2:", '{},'.format(service2), '${}'.format(auto_service[service2]))
    total_price = auto_service[service2]
    print('\nTotal:', '${}'.format(total_price))
elif service1 != '-' and service2 == '-':
    print("Service 1:", '{},'.format(service1), '${}'.format(auto_service[service1]))
    print("Service 2:", auto_service[service2])
    total_price = auto_service[service1]
    print('\nTotal:', '${}'.format(total_price))
else:
    print("Service 1:", auto_service[service1])
    print("Service 2:", auto_service[service2])
    print('\nTotal:', '${}'.format(0))