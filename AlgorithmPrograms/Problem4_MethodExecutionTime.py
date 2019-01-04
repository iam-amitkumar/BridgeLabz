"""This program call these utility function:
i.binarySearch method for integer
ii.binarySearch method for String
iii.insertionSort method for integer
iv.insertionSort method for String
v.bubbleSort method for integer
vi.bubbleSort method for String
Checking using "Stopwatch" function the Elapsed Time for every method call
Printing output the Search and Sorted List elapsed time
performance in descending order

@author Amit Kumar
@version 1.0
@since 04/01/2019
"""
# importing important modules
import utility.Utility
import time
import operator


def execution_time():
    # binary search for integers
    int_list = [64, 34, 25, 12, 22, 11, 90]  # initializing the integer unsorted list for sorting
    t1 = time.time()  # assigning current time to t1 before execution of the function
    utility.Utility.binary_search(int_list, 22)  # searching the element in the integer list through
    # "Binary Search" technique
    t2 = time.time()  # assigning current time to t2 after execution of the function
    int_binary = (t2-t1) * (10 ** 6)  # to get the total execution time in pico-seconds unit subtracting t1 from t2

    # binary search for string
    str_list = ["zoom", "drift", "python", "devops", "bridgelabz", "acknowledge"]  # initializing the string unsorted
    # list for sorting
    t3 = time.time()
    utility.Utility.binary_search(str_list, "bridgelabz")  # searching the element in the string list through
    # "Binary Search" technique
    t4 = time.time()
    str_binary = (t4 - t3) * (10 ** 6)

    # insertion sort for integers
    int_list = [64, 34, 25, 12, 22, 11, 90]  # initializing the integer unsorted list for sorting
    t5 = time.time()
    utility.Utility.insertion_sort(int_list)  # sorting the integer list through "Insertion Sort" technique
    t6 = time.time()
    int_insertion = (t6 - t5) * (10 ** 6)

    # insertion sort for string
    str_list = ["zoom", "drift", "python", "devops", "bridgelabz", "acknowledge"]  # initializing the string unsorted
    # list for sorting
    t7 = time.time()
    utility.Utility.insertion_sort(str_list)  # sorting the string list through "Insertion Sort" technique
    t8 = time.time()
    str_insertion = (t8 - t7) * (10 ** 6)

    # bubble sort for integers
    int_list = [64, 34, 25, 12, 22, 11, 90]  # initializing the integer unsorted list for sorting
    t9 = time.time()
    utility.Utility.bubble_sort(int_list)  # sorting the integer list through "Bubble Sort" technique
    t10 = time.time()
    int_bubble = (t10 - t9) * (10 ** 6)

    # bubble sort for integers
    str_list = ["zoom", "drift", "python", "devops", "bridgelabz", "acknowledge"]  # initializing the string unsorted
    # list for sorting
    t11 = time.time()
    utility.Utility.bubble_sort(str_list)  # sorting the string list through "Bubble Sort" technique
    t12 = time.time()
    str_bubble = (t12 - t11) * (10 ** 6)

    # initializing the dictionary to fetch the respective technique name used for searching and sorting by their sorted
    # executed time in descending order
    sorted_time = {
        int_binary: "Binary Search for Integer",
        str_binary: "Binary Search for String",
        int_insertion: "Insertion Sort for Integer",
        str_insertion: "Insertion Sort for String",
        int_bubble: "Bubble Sort for Integer",
        str_bubble: "Bubble Sort for String"
    }

    # utility.Utility.bubble_sort(sorted_time)
    sorted_d = sorted(sorted_time.items(), key=operator.itemgetter(0), reverse=True)  # sorting the above dictionary
    # using the in-built function based on keys
    print("\n", sorted_d)  # printing the sorted based on keys dictionary(key:value pair)

    print("\nTime elapsed in pico-seconds(10^-6):\n")
    print("\nTime elapsed by functions in descending order: ")
    for i in range(0, len(sorted_d)):
        print(sorted_d[i][1])  # printing only values of the respective element of the list


execution_time()  # calling the above function for execution
