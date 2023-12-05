#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for value in matrix:
            for val in value:
                print("{:d}".format(val), end=" "
                        if val != value[-1] else '\n')
    else:
        print()
