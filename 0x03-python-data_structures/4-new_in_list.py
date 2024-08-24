#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):  # Fixed the index check
        return my_list
    list_cpy = my_list.copy()  # Create a copy of the list
    list_cpy[idx] = element    # Modify the specific index
    return list_cpy
