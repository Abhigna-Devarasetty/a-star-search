#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
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
    print("in add pichi",row,col)
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' and canBeAttacked(r,c,len(house_map),len(house_map[0])) == False]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

def canBeAttacked(i,j,r,c):
    for k in range(0,r):
        if house_map[k][j]=='p':
            print("returning true horizontal:",i,j)
            return True
    for k in range(0,c):
        if house_map[i][k]=='p':
            print("returning true vertical:",i,j)
            return True
    #checking diagonally
    for k in range(0,r):
        for l in range(0,c):
            if (k+l==i+j) or (k-l==i-j):
                if house_map[k][l]=='p':
                    print("returning true diagonal",i,j)
                    return True
    print("returning false",i,j)
    return False

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
            print("new hose map-----",new_house_map)
            # printable_house_map(new_house_map)
            fringe.append(new_house_map)

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print(solution)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


