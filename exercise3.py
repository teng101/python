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
    remove = remove.split(",")
    for i in remove:
        if i not in shopping_list:
            break
        else:
            shopping_list.remove(i)
    print(shopping_list)
