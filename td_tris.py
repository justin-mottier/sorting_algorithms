"""
TD noté sur les algos de tri
"""

import random
import time
import sys

def create_array(size):
    """
    create an array of size numbers between 0 and 100
    """
    array = []
    for _ in range(size):
        array.append(random.randint(0, 100))
    return array

def swap(array, index_a, index_b):
    """
    swap the index of two elements in an array
    """
    tmp = array[index_a]
    array[index_a] = array[index_b]
    array[index_b] = tmp

def bubble_sort(array):
    """
    sort an array with the bubble sort method
    """
    for _ in array:
        for cpt_a in range(len(array) - 1):
            if array[cpt_a] > array[cpt_a + 1]:
                swap(array, cpt_a, cpt_a + 1)

def quicksort(array, first_index=0, last_index=-1):
    """
    sort an array with the quicksort method
    """
    if last_index == -1:
        last_index = len(array) - 1

    if last_index <= first_index:
        return
    pivot_index = last_index
    pivot = array[pivot_index]
    index = first_index
    while index < pivot_index:
        if array[index] > pivot:
            array.insert(pivot_index, array.pop(index))
            pivot_index -= 1
        else:
            index += 1
    quicksort(array, first_index, pivot_index - 1)
    quicksort(array, pivot_index + 1, last_index)

def merge(tab):
    """
    sort an array with the merge sort method
    """
    if len(tab) == 1:
        return tab
    return join(merge(tab[:len(tab)//2]), merge(tab[len(tab)//2:]))

def join(arr_a, arr_b):
    """
    merge two sorted arrays
    """
    if not arr_a:
        return arr_b
    if not arr_b:
        return arr_a
    if arr_a[0] < arr_b[0]:
        return [arr_a.pop(0)] + join(arr_a, arr_b)
    return [arr_b.pop(0)] + join(arr_a, arr_b)

TAILLES = [10, 100, 1000, 10000, 100000]

sys.setrecursionlimit(100000)

for _ in range(1):
    for taille in TAILLES:
        tab_a = create_array(taille)
        tab_b = tab_a.copy()
        tab_c = tab_a.copy()

        start_a = time.time()
        bubble_sort(tab_a)
        end_a = time.time()
        output_a = str(end_a - start_a)
        print(output_a)
        res_a = open("benchmark/bubble_" + str(taille), "a")
        res_a.write(output_a + "\n")
        res_a.close()

        start_b = time.time()
        quicksort(tab_b)
        end_b = time.time()
        output_b = str(end_b - start_b)
        print(output_b)
        res_b = open("benchmark/quicksort_" + str(taille), "a")
        res_b.write(output_b + "\n")
        res_b.close()

        start_c = time.time()
        merge(tab_c)
        end_c = time.time()
        output_c = str(end_c - start_c)
        print(output_c)
        res_c = open("benchmark/merge_" + str(taille), "a")
        res_c.write(output_c + "\n")
        res_c.close()
