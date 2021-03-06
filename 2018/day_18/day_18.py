# Advent of Code - Day 18
# Author: Ryan Anstotz

import os
import sys
import copy

class magic_lumber(object):
    """ class to solve Advent of Code 2018 Day 18 """
    
    def __init__(self, file_path):

        self.file_path = file_path
        self.land_matrix = []

        # types of ground
        self.open_ground = "."
        self.tree = "|"
        self.lumberyard = "#"

        # for storing the new matrix before copying contents to land_matrix
        self._gen_matrix()
        self._temp_matrix = [["" for i in range(len(self.land_matrix[0]))]
                             for i in range(len(self.land_matrix))]

        # part 2 hash map
        self.hash_map = {}
        self.resources = []
        self.tree_list = []
        self.lumber_list = []
        
    def _gen_matrix(self):
        """ read in file as rows/cols of individual characters """
        with open(self.file_path, 'r') as fp:
            for line in fp.readlines():
                self.land_matrix.append(list(line.strip('\n')))
        return
                
    def print_data(self):
        for row in self.land_matrix:
            print(row)
        # sanity check
        print("row is len: ", len(self.land_matrix))
        print("col is len: ", len(self.land_matrix[0]))
        return

    def print_temp(self):
        for row in self._temp_matrix:
            print(row)
        # sanity check
        print("row is len: ", len(self._temp_matrix))
        print("col is len: ", len(self._temp_matrix[0]))
        return

    
    # complete the requirements
    def _insert_trees(self, row, col):
        tree_threshold = 3
        adjacent_tree_count = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i < 0 or j < 0:
                    continue
                if i == row and j == col:
                    continue
                try: 
                    if self.land_matrix[i][j] == self.tree:
                        adjacent_tree_count += 1
                # list index out of range
                except:
                    pass
        if adjacent_tree_count >= tree_threshold:
            self._temp_matrix[row][col] = self.tree
        else:
            self._temp_matrix[row][col] = self.open_ground
        return

    # complete the requirements
    def _insert_lumberyard(self, row, col):
        lumberyard_threshold = 3
        adjacent_lumberyard_count = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i < 0 or j < 0:
                    continue

                if i == row and j == col:
                    continue
                try: 
                    if self.land_matrix[i][j] == self.lumberyard:
                        adjacent_lumberyard_count += 1
                # list index out of range
                except:
                    pass
        if adjacent_lumberyard_count >= lumberyard_threshold:
            self._temp_matrix[row][col] = self.lumberyard 
        else:
            self._temp_matrix[row][col] = self.tree 
        return
    
    def _insert_open_ground(self, row, col):
        lumberyard_flag = False
        tree_flag = False
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i < 0 or j < 0:
                    continue
                if i == row and j == col:
                    continue
                try: 
                    if self.land_matrix[i][j] == self.tree:
                        tree_flag = True
                    if self.land_matrix[i][j] == self.lumberyard:
                        lumberyard_flag = True
                # list index out of range
                except:
                    pass
        if lumberyard_flag == True and tree_flag == True:
            self._temp_matrix[row][col] = self.lumberyard 
        else:
            self._temp_matrix[row][col] = self.open_ground
        return
    
    
    def _run_app(self):

        # store as tuple to hash
        temp_land_matrix = tuple(tuple(i) for i in self.land_matrix)

        # this is a hash hit
        if temp_land_matrix in self.hash_map:
            self.land_matrix = self.hash_map[temp_land_matrix][1]
            self.resources.append(self.hash_map[temp_land_matrix][0])
            self.tree_list.append(self.hash_map[temp_land_matrix][2])
            self.lumber_list.append(self.hash_map[temp_land_matrix][3])
            
        else:
            tree_count = 0
            lumberyard_count = 0
            for row in range(len(self.land_matrix)):
                for col in range(len(self.land_matrix[row])):
                    # insert some trees and get resource value
                    if self.land_matrix[row][col] == self.open_ground:
                        self._insert_trees(row, col)
                    # insert the lumberyards
                    if self.land_matrix[row][col] == self.tree:
                        tree_count += 1
                        self._insert_lumberyard(row, col)
                    # insert ~~ open spaces ~~
                    if self.land_matrix[row][col] == self.lumberyard:
                        lumberyard_count += 1
                        self._insert_open_ground(row, col)
            resource_val = tree_count * lumberyard_count

            # store the data
            self.hash_map[temp_land_matrix] = [resource_val, self._temp_matrix,
                                               tree_count, lumberyard_count]
            self.resources.append(resource_val)
            self.tree_list.append(tree_count)
            self.lumber_list.append(lumberyard_count)
            
            # reset the matrix after the iteration
            self.land_matrix = self._temp_matrix
            self._temp_matrix = [["" for i in range(len(self.land_matrix[0]))]
                                 for i in range(len(self.land_matrix))]
        
        return

    def run_iterations(self, iterations):
        for runs in range(0, iterations):
            self._run_app()
        return
            
    def get_resource_value(self):
        tree_count = 0
        lumberyard_count = 0
        for row in range(len(self.land_matrix)):
            for col in range(len(self.land_matrix[row])):
                if self.land_matrix[row][col] == self.tree:
                    tree_count += 1
                if self.land_matrix[row][col] == self.lumberyard:
                    lumberyard_count += 1
        result = tree_count * lumberyard_count
        return result

# end of magic_lumber class         
        
def main(argv):

    # Part One
    minutes_one = int(argv[2])
    santa_land_part_one = magic_lumber(argv[1])
    santa_land_part_one.run_iterations(minutes_one)
    result_one = santa_land_part_one.get_resource_value()
    print("Part One resource value is: ", result_one)
    #print(santa_land_part_one.resources)
    #print(santa_land_part_one.tree_list)
    #print(santa_land_part_one.lumber_list)

    test = set()
    start = int(argv[3])
    for vals in range(start, len(santa_land_part_one.resources)):
        if santa_land_part_one.resources[vals] in test:
            print("resource val: ", santa_land_part_one.resources[vals], " at index: ", vals)
            print("period is: index - start = ", vals - start)
            break
        else:
            test.add(santa_land_part_one.resources[vals])
            

    # Part Two
    minutes_two = 1000000000

    index = minutes_two % 28
    print("my index is: ", index)
    print("my number is: ", santa_land_part_one.resources[index+148])
    
    santa_land_part_two = magic_lumber(argv[1])
    #santa_land_part_two.run_iterations(minutes_two)
    result_two = santa_land_part_two.get_resource_value()
    #print("Part One resource value is: ", result_two)

    return

# execute script
if __name__ == "__main__":
    main(sys.argv[:])
    
# end of file
