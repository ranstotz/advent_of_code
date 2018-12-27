#!/usr/bin/env python

# import required modules:
#
import os
import sys
import string


def recursion(d):

    for key, value

# main function
#
def main(argv):
    
    d = {}
    with open(argv[1], 'r') as fp:
        for line in fp.readlines():
            line = line.split()
            if len(line) > 3:
                d[line[0]] = line[3:]
            else:
                d[line[0]] = []

    for key, value in d.iteritems():
        
    
    # Exit
    return

# Begin gracefully
#
if __name__ == "__main__":
        main(sys.argv[0:])
        #
        # End of file
