## Radosław Sajdak
import numpy as np
from random import randint

numbers = [randint(0,1000) for i in range(50)]

def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for i in array:
        if i < pivot:
            low.append(i)
        elif i == pivot:
            same.append(i)
        elif i > pivot:
            high.append(i)

    return quicksort(low) + same + quicksort(high)

   
def sort(array, reverse=False):
    array = quicksort(array)
    if reverse:
        return array[::-1]
    else:
        return array


print(sort(numbers, True))

