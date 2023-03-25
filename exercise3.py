#add strings to the list
shopping_list = list()

while True:
    i = input("Add to the shopping list:")
    i = i.split(",")
    shopping_list += i
    a = input("Do you wish to exit?(enter y to exit)")
    if a == "y":
        break
print(shopping_list)

while True:
    remove = input("Remove item:")
    if remove not in shopping_list:
        break
    else:
        shopping_list.remove(remove)
print(shopping_list)
