# Exercise 10: Create a new list from two list using the following condition

# Create a new list from two list using the following condition

# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# Given:
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# Expected Output:
# result list: [25, 35, 40, 60, 90]

def combine_odd_list(list1, list2):
    combine_list = []

    for number in list1:
        if number % 2 == 0:
            combine_list.append(number)

    for number in list2:
        if number % 2 == 0:
            combine_list.append(number)
    return combine_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]