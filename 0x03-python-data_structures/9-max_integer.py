#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maximum = my_list[0]
        for m in range(len(my_list)):
            if my_list[m] > maximum:
                maximum = my_list[m]
                return maximum
