#!/usr/bin/env python

# import required modules:
#
import os
import sys
import string
from collections import OrderedDict

# main function
#
def main(argv):

    # Read in file and convert to list of characters
    with open(argv[1], 'r') as fp:
        mystring = list(fp.read())

    # Strip all garbage characters
    count = 1
    while count < len(mystring):

        if mystring[count] == '<' and mystring[count-1] != '!':
            seccount = count+1
            while True:
                
                if mystring[seccount] == '!' and mystring[seccount+1] == '>':
                    seccount += 2
                elif mystring[seccount] == '>':
                    del mystring[count:seccount+1]
                    break
                else:
                    seccount += 1
        count += 1

    # Remove commas from list
    mystring = [x for x in mystring if x != ',']
    # Remove linefeed
    mystring.pop()
    print mystring
    # Find total score for all groups
    depth = 0
    mysum = 0
    count = 0
    openbrace = 0
    closebrace = 0
    while count < len(mystring):
        if mystring[count] == '{':
            depth += 1
            mysum += depth
            openbrace += 1
        elif mystring[count] == '}':
            closebrace += 1
            depth -= 1
        count += 1

    print mysum
    print openbrace, closebrace
    
    # Exit
    return

# Execute script
#
if __name__ == "__main__":
    main(sys.argv[0:])
    #
    # End 
