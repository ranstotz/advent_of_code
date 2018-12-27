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
    
    d = {}
    maxes = []
    with open(argv[1], 'r') as fp:
        for line in fp.readlines():
            line = line.split()
            print line
            if line[0] not in d:
                d[line[0]] = 0
            if line[4] not in d:
                d[line[4]] = 0
            print d[line[4]]
            
            if eval("d[line[4]] " + line[5] + line[6]):
                if line[1] == 'inc':
                    d[line[0]] += int(line[2])
                elif line[1] == 'dec':
                    d[line[0]] -= int(line[2])
            maxes.append(max(d.values()))
                    
    # Part 1
    print max(d.values())
    # Part 2
    print max(maxes)
    #mydict = sorted(d.items(), key=lambda x: x[1])
    #print mydict
        
    
    # Exit
    return

# Begin gracefully
#
if __name__ == "__main__":
        main(sys.argv[0:])
        #
        # End of file
