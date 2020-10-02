# Basim Siddiqui
# PSID: 1517778

def exact_change(user_total):
    dollar = user_total // 100
    user_total = user_total % 100
    quarter = user_total // 25
    user_total = user_total % 25
    dime = user_total // 10
    user_total = user_total % 10
    nickel = user_total // 5
    user_total = user_total % 5
    penny = user_total

    return dollar, quarter, dime, nickel, penny


def coin_count():
    coins = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(coins)
    if coins <= 0:
        print('no change')
    else:
        if num_dollars == 1:
            print("%d dollar" % num_dollars)
        elif num_dollars > 1:
            print('%d dollars' % num_dollars)

        if num_quarters == 1:
            print("%d quarter" % num_quarters)
        elif num_quarters > 1:
            print('%d quarters' % num_quarters)

        if num_dimes == 1:
            print("%d dime" % num_dimes)
        elif num_dimes > 1:
            print('%d dimes' % num_dimes)

        if num_nickels == 1:
            print("%d nickel" % num_nickels)
        elif num_nickels > 1:
            print('%d nickels' % num_nickels)

        if num_pennies == 1:
            print("%d penny" % num_pennies)
        elif num_pennies > 1:
            print('%d pennies' % num_pennies)

coin_count()