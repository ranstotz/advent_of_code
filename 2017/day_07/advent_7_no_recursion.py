#!/usr/bin/env python

# import required modules:
#
import os
import sys
import string


# main function
#
def main(argv):
    
    d = {}
    mylist = []
    with open(argv[1], 'r') as fp:
        for line in fp.readlines():
            line = line.split()
            if len(line) > 3:
                mylist.append(line[0])
                for i in line[3:]:
                    mylist.append(i)
                    

    print mylist
    
    # Exit
    return

# Begin gracefully
#
if __name__ == "__main__":
        main(sys.argv[0:])
        #
        # End of file
