# Define a function called count that has two arguments called sequence and item.
# Return the number of times the item occurs in the list.For example: count([1,2,1,1], 1)
# should return 3 (because 1 appears 3 times in the list).

import random
number = random.randint(2000, 3000)
list1 = [int(num) for num in str(number)]
print(f"Random list {list1}")
number2 = random.randint(0, 9)
print(f"Random number: {number2}")


def count(sequence, item):
    total = 0
    for x in sequence:
        if x == item:
            total += 1
    return total


def how_many_in():
    if count(list1, number2) == 0:
        return "zero"
    elif count(list1, number2) == 1:
        return "one"
    elif count(list1, number2) == 2:
        return "two"
    elif count(list1, number2) == 3:
        return "three"
    elif count(list1, number2) == 4:
        return "four"


print(f"There is {how_many_in()} {number2} in {list1}")
