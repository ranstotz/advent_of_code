# Advent of Code 2018 - Day 23
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
    strong_nanobot_ind = 0
    strong_nanobot_signal = 0

    # store puzzle input to list of nanobot objects
    with open(argv[1], 'r') as fp:
        for line in fp.readlines():
            bot_line = nanobot(line.strip('\n'))
            nanobot_list.append(bot_line)

    # get the strongest nanobot index and signal, signal may be redundant...
    counter = 0
    for bot in nanobot_list:
        #bot.print_data()
        if bot.rad > strong_nanobot_signal:
            strong_nanobot_signal = bot.rad
            strong_nanobot_ind = counter
        counter += 1
    
    print("strongest nanobot signal is: ", strong_nanobot_signal, " at index ", strong_nanobot_ind)

    # calculate how many nanobots are within range
    in_range = 0
    for ind in range(len(nanobot_list)):
        distance = manhattan_distance(nanobot_list[strong_nanobot_ind], nanobot_list[ind])
        if strong_nanobot_signal >= distance:
            in_range += 1
    # print part one answer (correct)
    print("nanbots in range are: ", in_range)

    # move to part two
    # well I guess get the average position (x,y,z) of all the nanobots and start from there?
    # print out the number of nanobots
    print("part 2!")
    print("number of nanobots: ", len(nanobot_list))

    avg_x, avg_y, avg_z = get_avg_positions(nanobot_list)
    
    print("avg x: ", avg_x, " avg y: ", avg_y, " avg z: ", avg_z)
    
    # return from main
    return

def get_avg_positions(bots):
    total_bots = len(bots)
    tot_x = 0
    tot_y = 0
    tot_z = 0
    for bot in bots:
        tot_x += bot.x
        tot_y += bot.y
        tot_z += bot.z

    return total_bots//tot_x, total_bots//tot_y, total_bots//tot_z
    

def manhattan_distance(reference_nanbot, compare_nanobot):
    """ calculate the manhattan distance of two nanobot objects """
    total_distance = 0
    x_distance = abs(reference_nanbot.x - compare_nanobot.x)
    y_distance = abs(reference_nanbot.y - compare_nanobot.y)
    z_distance = abs(reference_nanbot.z - compare_nanobot.z)

    total_distance = x_distance + y_distance + z_distance

    return total_distance

# execute
if __name__ == "__main__":
    main(sys.argv[:])
    
# end of file
