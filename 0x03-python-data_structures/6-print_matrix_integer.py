#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for value in matrix:
        for val in value:
            print("{:d}".format(val), end=" ")
        print()
