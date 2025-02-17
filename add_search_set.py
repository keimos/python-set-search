# add_search_set.py

# number set definition
number_set = {23, 90, 78, 12, 34, 67}

# new data is added

number_set.add(50)

# set values printing
print(number_set)

_message = "that number is not available!"

# request use for a number value for search
search_val = int(input("Input a number:"))
# Search the numbers in the set
for val in number_set:
    if val == search_val:
        _message = "that number is available!"
    break

print(_message)

