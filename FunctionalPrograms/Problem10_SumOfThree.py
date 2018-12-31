""" Sum_Of_Three is a program with cubic running time. Read in N
integers and counts the number of triples that sum to exactly 0
with input of user-input integer list.

@author Amit Kumar
@version 1.0
@since 31/12/2018
"""
import utility.Utility
list_size = int(input("Enter the size of the list: "))
int_arr = utility.Utility.user_int_list(list_size)
len_int_arr = len(int_arr)
print()
# print(int_arr)


def triplet_sum_zero(arr, array_len):
    increment = 1
    check_unique_triplet = []
    for i in range(0, array_len-2):
        for j in range(i+1, array_len-1):
            for k in range(j+1, array_len):
                if (arr[i] + arr[j] + arr[k]) == 0:
                    # print("\nTriplet number ", increment, "> ",  arr[i], " ", arr[j], " ", arr[k])

                    if (arr[i] not in check_unique_triplet) and (arr[j] not in check_unique_triplet) and (arr[k] not in check_unique_triplet) :
                        check_unique_triplet.append(arr[i])
                        check_unique_triplet.append(arr[j])
                        check_unique_triplet.append(arr[k])
                        print("Triplet no. ", increment, "----> ", arr[i], " ", arr[j], " ", arr[k])
                        increment += 1
                        # check_unique_triplet.clear()
    print("\nTotal number of triplets: ", increment-1)


triplet_sum_zero(int_arr, len_int_arr)


