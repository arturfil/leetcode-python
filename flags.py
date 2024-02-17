
import argparse

parser = argparse.ArgumentParser() # initialize argument parser

def return_flags():
    parser.add_argument("-exclude",  "--exclude",  default=True,  help="Exclude problems not in 75 LC list")
    parser.add_argument("-category", "--category", default="all", help="Which category of problems")

    args = parser.parse_args()

    return args

'''
    Possible categories:
        binary-tree
        heaps
        sort-search
        systems-design
        matrix
        linked-lists
        intervals
        graphs
        dynamic-programming
        arrays

    run example command:
        make run category=intervals exclude=True
'''




