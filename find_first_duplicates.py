"""
Problem : find the indices of the first duplicate elements for given input list
Example Input list [ 5, 17, 3, 17, 4, -1, -1, -1 ] ----> we need to return duplicate_list_idx = [3, 6]
"""

"""
This fucntion will return indices of first duplicated elements in given input list
I used property in set data structture "set does not have multiple occurrences of the same element" 
to loop over all items in the given input list and put them in set and
if any item is duplicated will be putted in duplicate_list list and its index will be putted in duplicate_list_idx list
"""

def index_of_first_duplicate(input_list):
    # Initialize varaibales
    duplicate_list = []
    duplicate_list_idx = []
    input_list_set = set()
    set_size_before_add = 0
    set_size_after_add = 0
    input_list_len = len(input_list)
    #Loop over input list
    for i in range(input_list_len):
        #Get list lenght before add item to the list
        set_size_before_add = len(input_list_set)
        #Current element will be added to set if it is not duplicated
        input_list_set.add(input_list[i])
        # Get list lenght after add item to the list
        set_size_after_add = len(input_list_set)
        #If lists before and after have same length means that current element is duplicated but also we check currennt element if exsist or not
        #in duplicate list because we are intersted only in first duplicate elements
        if (set_size_after_add == set_size_before_add) and (input_list[i] not in duplicate_list) :
            duplicate_list_idx.append(i)
            duplicate_list.append(input_list[i])
    #Check if duplicate_list_idx is empty return -1 which means no duplicated elements
    if len(duplicate_list_idx) == 0:
        #print("No duplicated elements found")
        duplicate_list_idx.append(-1)
    return duplicate_list_idx

"""
Test Cases
"""
print(index_of_first_duplicate( [ 5, 17, 3, 17, 4, -1, -1, -1 ] ))
print(index_of_first_duplicate( [1, 2, 2, 2, 2, 2, 1 ] ))
print(index_of_first_duplicate( [2, 2, 2, 2, 2 ] ))
print(index_of_first_duplicate( [1, 2, 3, 4, 5, 6 ] ))
