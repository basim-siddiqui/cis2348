# Basim Siddiqui
# PSID: 1517778

class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(self.item_name + ' '+ str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))

if __name__ == "__main__":
    print("Item 1")
    item_1 = ItemToPurchase()
    item_1.item_name = (input("Enter the item name:\n"))
    item_1.item_price = int(input("Enter the item price:\n"))
    item_1.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nItem 2")
    item_2 = ItemToPurchase()
    item_2.item_name = (input("Enter the item name:\n"))
    item_2.item_price = int(input("Enter the item price:\n"))
    item_2.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nTOTAL COST")
    item_1.print_item_cost()
    item_2.print_item_cost()
    total_cost = (item_1.item_price * item_1.item_quantity)+(item_2.item_price * item_2.item_quantity)
    print("\nTotal: $" + str(total_cost))