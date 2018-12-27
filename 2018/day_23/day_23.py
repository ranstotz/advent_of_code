# Advent of Code - Day 23
# Author: Ryan Anstotz

import os
import sys

class nanobot(object):

    def __init__(self, line_input):
        self.rad = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self._get_data(line_input)


    def _get_data(self, line):
        ''' this parses the line input '''
        line = line[5:]
        line = line.split(',')
        # get radius
        self.rad = int(line[3].split('=')[1])
        # get coordinates
        self.x = int(line[0])
        self.y = int(line[1])
        self.z = int(line[2].rstrip('>'))

    def print_data(self):
        print("x is: ", self.x, " | y is: ", self.y, " | z is: ", self.z,
              " | rad is: ", self.rad)
        

def main(argv):

    nanobot_list = []
    
    with open(argv[1], 'r') as fp:
        for line in fp.readlines():
            bot = nanobot(line.strip('\n'))
            nanobot_list.append(bot)

    for thing in nanobot_list:
        thing.print_data()
    
    # return from main
    return


if __name__ == "__main__":
    main(sys.argv[:])
    
