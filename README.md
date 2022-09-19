# vdevaras-a0

## Part 1:

### Function: parse_map 

#### Argument: filename 

#### Action:
 This function takes file as an input and returns a 2D matrix as an output

### Function: valid_index_map 
#### Argument: pos, n, m pos = current position; n = row, m = column 

#### Action:
Checks whether the given position is valid or not

### Function: moves 
#### Argument: map, row, col 

#### Action
Returns all the valid positions that are possible  from current position

### Function: search 

#### Argument: house_map

#### Action:

This function performs search for the path from node p (source location) to @ (final location).
Here we create a new visited list which notes down whether the node is visited or not. y maintaing this node we try to avoid revisiting of nodes in loop. Here we consider, x2 and y2 as new position differences from current position. Based on x2 and y2 values, we decide the direction. Based on the values for the x2 and y2 we can decide which direction we can move (Up, Down, Left, Right). 
Once the node is visited, we change the value at position to 1, which avoids in further looping at same position.
Once a valid position is recieved, it's pushed to fringe and sorted in reverse order.
Once the fringe is empty, it represents that we are unable to find the path. or else it returns the exact path and breaks the loop.


## Part 2:

### Function: parse_map 

#### Argument: filename 

#### Action:
 This function takes file as an input and returns a 2D matrix as an output

### Function: count_pichus 
#### Argument: house_map 

#### Action:
Returns the count of pichus in the house_map

### Function: printable_house_map
#### Argument: house_map 

#### Action
Prints the current housemap in the @D matrix format

### Function: add_pichu
#### Argument: house_map, row, col

#### Action
Inserts pichu at given row and column position

### Function: is_goal
#### Argument: house_map, k

#### Action
Checks whether the given state has all the pichus or not

### Function: solve
#### Argument: house_map, k

#### Action
This function verifies it reached the final position or not and the calls the successor function from fringe

### Function: successors
#### Argument: house_map

#### Action
In this function, based on the flag variable it is decided whether it is valid position or not.

If the current position is '.','p','@', we ignore the postion
I twe encounter 'p', the flag_variable value is changed and next pichu is not inserted at that position.

This validation is done in 3 directions (Row, Column and Diagonal). If we encounter a 'p' in any of these directions, we move to the next node
