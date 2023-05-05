
#================================
def sort_list(list1, list2):
#=================================
    """
    This function sorts one list by another list. It can work with 1d arrays or lists. 

    Input:
    list1: list/array to be sorted
    list2: list/array to sort by

    Output:
    z: list1 sorted by list 2
    sorted(list2): list2 sorted
    """


    zipped_pairs = zip(list2, list1)
 
    z = [x for _, x in sorted(zipped_pairs)]
 
    return z, sorted(list2)


