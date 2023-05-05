
#================================
def sort_2list(list1, list2):
#=================================
    """
    This function sorts one list by another list. It can work with 1d arrays or lists. 

    Input:
    list1: list/array to sort by
    list2: list/array to be sorted

    Output:
    sorted(list1): list1 sorted by itself
    z: list2 sorted by list 1
    """

    zipped_pairs = zip(list1, list2)
 
    z = [x for _, x in sorted(zipped_pairs)]
 
    return sorted(list1), z

