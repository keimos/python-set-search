# add_search_set.py

# number set definition
def create_number_set():
    "Create and return the initial number set"
    return {23, 90, 78, 12, 34, 67}

def add_number_to_set(number_set, number):
    "Add a number to the set"
    number_set.add(number)

def print_number_set(number_set):
    "Print the current values in the set"
    print(number_set)

def number_search(number_set, search_val):
    "Search for a number in the set and return the appropriate message"
    if search_val in number_set:
        return "That number is available!"
    else:
        return "That number is NOT available!"

def main():
    number_set = create_number_set()

    # Add new data to the set
    add_number_to_set(number_set, 50)

    # Print the number set
    print_number_set(number_set)

    # Request user input for a number value to search
    search_val = int(input("Input a number:"))

    # Search the number and print the message
    message = number_search(number_set, search_val)
    print(message)

if __name__ == "__main__":
    main()

