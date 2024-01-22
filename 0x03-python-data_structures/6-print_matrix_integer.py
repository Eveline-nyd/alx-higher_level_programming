#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for m in matrix:
            for n in m:
                print("{:d}".format(n), end=''if n != m[-1] else '')
                print()
