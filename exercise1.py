# remove the vowels from the string
vowels = ["a","e","i","o","u","A","E","I","O","U"]
my_string = str(input())
new_string = ""

for i in my_string:
    if i not in vowels:
        new_string += i
print(new_string)

"""
my_list = [i for i in my_string if i not in vowels]
another_string = " ".join(my_list)

print(another_string)
"""
my_list = list(new_string.split())# create a list out of string parsing on white space
print(my_list)

new_list = [len(i) for i in my_list]# counting the length of each element of the list
print(new_list)

new_list.reverse()# reversing the list
print(f"Printed in reverse: {new_list}")
