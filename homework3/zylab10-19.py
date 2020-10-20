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
        print('ADD ITEM TO CART')
        item_name = input("Enter the item name:\n")
        item_description = input("Enter the item description:\n")
        item_price = int(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self):
        print('REMOVE ITEM FROM CART')
        i = 0
        remove_name = input("Enter name of item to remove:\n")
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
        print('CHANGE ITEM QUANTITY')
        name = input('Enter the item name:\n')
        new_num = int(input('Enter the new quantity:\n'))
        for items in self.cart_items:
            if (items.item_name == name):
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
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_shopping_cart()

    def print_descriptions(self):
        print('\nOUTPUT ITEMS\' DESCRIPTIONS')
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date), end='\n')
        print('\nItem Descriptions')
        for items in self.cart_items:
            print('{}: {}'.format(items.item_name, items.item_description), end='\n')

    def output_shopping_cart(self):
        new = ShoppingCart()
        print('OUTPUT SHOPPING CART')
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date), end='\n')
        print('Number of Items:', new.get_num_items_in_cart(), end='\n\n')
        self.total_cost = self.get_cost_of_cart()
        if (self.total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            pass
        tc = 0
        for items in self.cart_items:
            print('{} {} @ ${} = ${}'.format(items.item_name, items.item_quantity, items.item_price, (items.item_quantity * items.item_price)), end='\n')
            tc += (items.item_quantity * items.item_price)
        print('\nTotal: ${}'.format(tc), end='\n')




def print_menu(ShoppingCart):
    customers_cart = new_cart
    string = ''
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            "i - Output items' descriptions\n"
            'o - Output shopping cart\n'
            'q - Quit\n')
    command = ''
    while (command != 'q'):
        string = ''
        print(menu, end='\n')
        command = input('Choose an option:\n')
        while (command != 'a' and command != 'o' and command != 'i' and command != 'r' and command != 'c' and command != 'q'):
            command = input('Choose an option:\n')
        if (command == 'a'):
            customers_cart.add_item(string)
        if (command == 'o'):
            customers_cart.output_shopping_cart()
        if (command == 'i'):
            customers_cart.print_descriptions()
        if (command == 'r'):
            customers_cart.remove_item()
        if (command == 'c'):
            customers_cart.modify_item()




if __name__ == "__main__":
    customer_name = str(input("Enter customer's name:"))
    current_date = str(input("\nEnter today's date:\n"))
    print('\nCustomer name:', customer_name, end='\n')
    print("Today's date:", current_date, end='\n')
    new_cart = ShoppingCart(customer_name, current_date)
    print_menu(new_cart)
