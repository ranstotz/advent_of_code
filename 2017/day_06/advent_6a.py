#!/usr/bin/env python

# import required modules:
#
import os
import sys
import string

def dups(A):

    current = []
    counter = 0
    while True:
        maxbank = max(A)
        
        maxind = A.index(maxbank)

        A[maxind] = 0
        

        while maxbank > 0:
            # Check 
            if maxind == len(A)-1:
                A[0] += 1
            else:
                A[maxind+1] += 1
            maxbank -= 1
            maxind = (maxind+1) % len(A)
            #print A
            #print maxbank
        #print A

        # use A[:] since we need to pass a copy
        # of the list
        current.append(A[:])
        #print current
        tempcur = map(tuple, current)
        counter += 1
        #print tempcur
        #print set(tempcur)
        if len(tempcur) != len(set(tempcur)):
            # Here is where part 2 begins
            # starting from a state that has already been seen,
            # how many block redistribution cycles must be performed
            # before that same state is seen again?
            return counter, A, len(current)- 1 - current.index(A)

# main function
#
def main(argv):

    mytest = [0, 2, 7, 0]
    mylist = [5,1,10,0,1,7,13,14,3,12,8,10,7,12,0,6]
    print dups(mylist)

    # Exit gracefully
    #
    return

# Begin gracefully
#
if __name__ == "__main__":
        main(sys.argv[0:])
        #
        # End of file
