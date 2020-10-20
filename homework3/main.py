# Basim Siddiqui
# PSID: 1517778


#class from lab 10.17
class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(self.item_name + ' '+ str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))

    def print_item_description(self):
        print(self.item_name + ": " + self.item_description)


#new class
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, string):
        print('\nADD ITEM TO CART\n')
        item_name = input("Enter item name:")
        item_description = input("\nEnter the item description: ")
        item_price = int(input("\nEnter the item price: "))
        item_quantity = int(input("\nEnter the item quantity: "))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self):
        print('\nREMOVE ITEM FROM CART\n')
        i = 0
        remove_name = input("Enter name of item to remove: ")
        for items in self.cart_items:
            if items.item_name == remove_name:
                del self.cart_items[i]
                i += 1
                iteration = True
                break
            else:
                iteration = False
        if iteration == False:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self):
        print('\nCHANGE ITEM QUANTITY\n')
        name = input('Enter the item name: ')
        for items in self.cart_items:
            if (items.item_name == name):
                new_num = int(input('Enter the new quantity: '))
                items.item_quantity = new_num
                iteration = True
                break
            else:
                iteration = False
        if (iteration == False):
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for items in self.cart_items:
            num_items = num_items + items.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for items in self.cart_items:
            item_cost = (items.item_quantity * items.item_price)
            total_cost += item_cost
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    def print_descriptions(self):
        print('\nOUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('\nItem Descriptions\n')
        for items in self.cart_items:
            print('{}: {}'.format(items.item_name, items.item_description), end='\n')

    def



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
