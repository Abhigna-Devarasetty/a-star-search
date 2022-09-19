#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : Venkata Sai Abhigna Devarasetty (vdevarase@iu.edu)
#
# Based on skeleton code in CSCI B551, Fall 2022.
import sys
# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    a=house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]
    #print(printable_house_map(a))
    return a
    
#generating successors based on the house map,
# checking diagonally, row and column
def successors(house_map):

    length_row = len(house_map)
    length_col = len(house_map[0])
    flag_variable = True
    new_list = []
    for row in range(0,length_row):
        for column in range(0,length_col):
            flag_variable = True
            if house_map[row][column] == '.':
                for i,j in zip(range(0,length_row),range(column-1,-1,-1)):
                    if i!=row:
                        if house_map[i][j] == 'p':
                            flag_variable = False
                            break
                        if house_map[i][j] == 'X':
                            break
                        if house_map[row][j] == '@':
                            break

                for i,j in zip(range(0,length_row),range(column+1,length_col)):
                        if i!=row:
                            if house_map[i][j] == 'p':
                                flag_variable = False
                                break
                            if house_map[i][j] == 'X':
                                break
                            if house_map[row][j] == '@':
                                break
                for i in range(0,length_row):
                        if i!=row:
                            if house_map[i][column] == 'p':
                                flag_variable = False
                                break
                            if house_map[i][column] == 'X':
                                break
                            if house_map[row][j] == '@':
                                break
                for j in range(0,length_col):
                        if j!=column:
                            if house_map[row][j] == 'p':
                                flag_variable = False
                                break
                            if house_map[row][j] == 'X':
                                break
                            if house_map[row][j] == '@':
                                break
                if (flag_variable):
                    new_list.append(add_pichu(house_map, row, column))
    print(new_list)
    return new_list

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop() ):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)
            
    #False is returned when we can't find a solution
    if len(fringe) == 0:
        return(0,False)
# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")
