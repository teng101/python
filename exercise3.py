#add strings to the list
shopping_list = list()

while True:
    i = input("Add strings to the list:")
    shopping_list.append(i)
    a = input("Do you wish to exit?(enter y to exit)")
    if a == "y":
        break
print(shopping_list)