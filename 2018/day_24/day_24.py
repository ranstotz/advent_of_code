# Advent of Code 2018 - Day 24
# Author: Ryan Anstotz

import os
import sys

class Unit(object):
    def __init__(self, hit_points, weakness, immune,
                 attack_damage, attack_type, initiative):
        self.hit_points = hit_points
        self.weakness = weakness # list of strings
        self.immune = immune # list of strings
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative

# combine unit and group into the class below. 
class Group(object):
    def __init__(self, length, unit):
        self.length = length
        self.unit = 0
        return
    

class System(object):
    def __init__(self):
        self.group_list = []

    # made it to here. Add the groups, add methods to the Group class and handle accordingly
    def add_group(self, line):
        
        return

def main(argv):

    # parse data
    with open(argv[1], 'r') as fp:
        fp.readline()
        for line in fp.readlines():
            line = line.rstrip('\n')
            if line == "Infection:":
                break
            print(line)
        fp.seek(0,0)
        infection_flag = False
        for line in fp.readlines():
            line = line.rstrip('\n')
            if line == "Infection:":
                infection_flag = True
                continue
            
            if infection_flag == True:
                print("infection stuff")
                print(line)

    
    # exit main
    return

# execute
if __name__ == "__main__":
    main(sys.argv[:])
    
