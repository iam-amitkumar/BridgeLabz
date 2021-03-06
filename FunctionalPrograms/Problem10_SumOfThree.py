""" Sum_Of_Three is a program with cubic running time. Read in N
integers and counts the number of triples that sum to exactly 0
with input of user-input integer list.

@author Amit Kumar
@version 1.0
@since 31/12/2018
"""
# importing important modules
import utility.Utility

global int_arr


# declaration of a function which finds the triplets whose is zero
def triplet_sum_zero(arr, array_len):
    increment = 1  # to count the number of triplets and print al the triplets serial wise
    '''check_unique_triplet = []  # a blank list to store triplets to match further triplets to avoid duplication'''
    for i in range(0, array_len-2):
        out = 0
        out1 = 0
        for j in range(i+1, array_len-1):
            for k in range(j+1, array_len):
                if (arr[i] + arr[j] + arr[k]) == 0 and out == 0 and out1 == 0:  # checking is sum of elements is
                    '''
                    # zero or not
                    # checking whether all three numbers of the triplet is repeating or unique
                    # if (arr[i] not in check_unique_triplet) and (arr[j] not in check_unique_triplet) and (arr[k] not
                    # in check_unique_triplet) :
                    #     check_unique_triplet.append(arr[i])  # adding first element of desired triplet to the list
                        # check_unique_triplet.append(arr[j])  # adding second element of desired triplet to the list
                        # check_unique_triplet.append(arr[k])  # adding third element of desired triplet to the list '''

                    print("Triplet no. ", increment, "----> ", arr[i], " ", arr[j], " ", arr[k])
                    increment += 1
                    out = + 1
                    out1 = + 1
    print("\nTotal number of triplets: ", increment-1)  # print total number of triplets


try:
    list_size = int(input("Enter the size of the list: "))
    int_arr = utility.Utility.user_int_list(list_size)  # creating a user-input list
except Exception as e:
    print(e)

len_int_arr = len(int_arr)  # extracting length of list
print()
triplet_sum_zero(int_arr, len_int_arr)
