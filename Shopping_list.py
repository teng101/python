class ShoppingList:
    def __init__(self):
        self.items = dict()

    def add_item(self, item_name, item_amt):
        self.items[item_name] = item_amt

    def delete_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print("Item not on the list")

    def print_list(self):
        if not self.items:
            print("Your list is empty.")
        else:
            print("Your list:")
            for item, amt in self.items.items():
                print(f"{item}: {amt}")

# Create a new shopping list object
my_list = ShoppingList()

# Prompt the user to add items to the list
while True:
    item = input("Add an item (or type 'y' to exit): ")
    if item.lower() == "y":
        break
    amt = input("Add an amount: ")    
    my_list.add_item(item, amt)

# Remove any empty keys from the dictionary
if "" in my_list.items:
    my_list.delete_item("")

# Print the updated list to the console
my_list.print_list()

# Prompt the user to delete items from the list
while True:
    del_item = input("Delete an item (or type 'y' to exit): ")
    if del_item.lower() == "y":
        break
    my_list.delete_item(del_item)

#prompt the user to edit the list
while True:
    edit_item = input("Edit the list (or type 'y' to exit): ")
    if edit_item.lower() == "y":
        break
    elif edit_item not in my_list.items:
        print("Item not on the list.")
        break
    amt = input("Add an amount: ")    
    my_list.add_item(edit_item, amt)

# Print the final list to the console
my_list.print_list()

        
        