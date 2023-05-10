import os
import numpy as np

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


#================================
def check_log(file_name, string):
#=================================

    """
    This function searches for a string in a log file, and returns a boolean if found.

    Inputs:
    file_name: name of log file to search
    string: string to search for

    Outputs:    
    True if string is found in log file, False if not

    """

    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            log = f.read()
        if string in log:
            return True
        else:
            return False
        
