#dict taking input of string and number
my_dict = dict()

while True:
    item = input("Add an item/y to exit:")
    if item == "y":
        break
    amt = input("Add an amount:")
    my_dict[item] = amt

if "" in my_dict:
    del my_dict[""]
        
print(f"Your list: {my_dict}")


while True:
    del_item = input("Delete item/y to exit:")
    if del_item == "y":
        break
    elif del_item not in my_dict:
        print("Item not on the list")
        continue
    del my_dict[del_item]

print(f"Your list: {my_dict}")
