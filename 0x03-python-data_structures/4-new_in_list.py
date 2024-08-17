#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx + 1 > len(my_list):
        return my_list
    list_cpy = [list_cpy.append(i) for i in my_list]
    list_cpy[idx] = element
    return list_cpy