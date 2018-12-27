#!/usr/bin/env python

# import required modules:
#
import os
import sys
import string



def jumper(A):

    i = 0
    counter = 0

    while i < len(A):
        if i < 0:
            return counter
        temp = A[i]
        A[i] += 1
        i += temp
        counter += 1
    return counter
                                                                
 

# main function
#
def main(argv):

    A = [0, 3, 0, 1, -3]

    mylist = []
    with open(argv[1], 'r') as fp:
        for line in fp.readlines():
            mylist.append(int(line))

    print jumper(mylist)

    
    # Exit gracefully
    #
    return

# Begin gracefully
#
if __name__ == "__main__":
        main(sys.argv[0:])
        #
        # End of file
