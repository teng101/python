#dict taking input of string and number
my_dict = dict()

while True:
    item = input("Add an item:")
    amt = input("Add an amount:")
    my_dict[item] = amt
    exit = input("Enter y to exit")
    if exit == "y":
        break
    
print(f"Your list: {my_dict}")

while True:
    del_item = input("Delete item:")
    del my_dict[del_item]
    del my_dict[""]
    exit = input("Enter y to exit")
    if exit == "y":
        break

print(f"Your list: {my_dict}")
