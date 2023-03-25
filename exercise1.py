# remove the vowels from the string
vowels = ["a","e","i","o","u","A","E","I","O","U"]
my_string = str(input())
"""new_string = list()

for i in my_string:
    if i in vowels:
        continue
    else:
        new_string.append(i)
print(" ".join(new_string))
"""
new_string = [i for i in my_string if i not in vowels]

print(" ".join(new_string))