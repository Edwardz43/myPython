import random
import time
import sys


def swap(array, num1, num2):
    temp = array[num1]
    array[num1] = array[num2]
    array[num2] = temp


def selection_sort(input_array):
    start_time = time.time()
    length = input_array.__len__() - 1
    for i in range(length):
        index_of_smallest = i

        for j in range(i + 1, length + 1):
            if input_array[j] < input_array[index_of_smallest]:
                index_of_smallest = j

        swap(input_array, i, index_of_smallest)

    total_time = time.time() - start_time
    print(total_time)


def bubble_sort(input_array):
    start_time = time.time()
    length = input_array.__len__()
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if input_array[j] > input_array[j + 1]:
                swapped = True
                swap(input_array, j, j + 1)

        if not swapped:
            pass

    total_time = time.time() - start_time
    print(total_time)


def merge(arr, l, m, r):
    len_left = m - l + 1
    len_right = r - m
    left = [0] * len_left
    right = [0] * len_right

    for i in range(len_left):
        left[i] = arr[l + i]

    for j in range(len_right):
        right[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r - 1)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


test_array = []
for index in range(5000):
    tmp = random.uniform(-100, 101)
    test_array.append(tmp)

random.shuffle(test_array)
bubble_sort(test_array)
# print(test_array)
random.shuffle(test_array)
selection_sort(test_array)
# print(test_array)
random.shuffle(test_array)
s = time.time()
merge_sort(test_array, 0, test_array.__len__() - 1)
print(time.time() - s)
# print(test_array)
