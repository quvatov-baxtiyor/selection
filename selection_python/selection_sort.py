import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# selection_sort
# definition: find the smallest value in the list and swap it with the value in the first position
# then find the second smallest value and swap it with the value in the second position
# continue until the list is sorted

# this function should implement selection sort by swapping values
def selection_sort_swap(values):
    for i in range(len(values)):
        # find the index of the smallest value in the list
        # we need to start at i because the values before i are already sorted
        index_of_min = i
        for j in range(i + 1, len(values)):
            if values[j] < values[index_of_min]:
                index_of_min = j
        # swap the value at i with the smallest value
        values[i], values[index_of_min] = values[index_of_min], values[i]


# another way of doing selection sort 
# will use additional list to keep track of the sorted items
# find the smallest value in the list and append it to the sorted list
# remove the value from the original list
# continue until the original list is empty

def selection_sort(values):
    sorted_list = []
    while values:
        # print("%-25s %25s" % (values, sorted_list))
        smallest = min(values)
        sorted_list.append(smallest)
        values.remove(smallest)
    return sorted_list

def find_min_index(values):
    index_of_min = 0
    for i in range(1, len(values)):
        if values[i] < values[index_of_min]:
            index_of_min = i
    return index_of_min

selection_sort(numbers)
