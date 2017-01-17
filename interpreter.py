'''
Brainfuck interpreter commands

There are eight commands:
+ : Increments the value at the current cell by one.
- : Decrements the value at the current cell by one.
> : Moves the data pointer to the next cell (cell on the right).
< : Moves the data pointer to the previous cell (cell on the left).
. : Prints the ASCII value at the current cell (i.e. 65 = 'A').
, : Reads a single input character into the current cell.
[ : If the value at the current cell is zero, skips to the corresponding ] .
    Otherwise, move to the next instruction.
] : If the value at the current cell is zero, move to the next instruction.
    Otherwise, move backwards in the instructions to the corresponding [ .

[ and ] form a while loop. Obviously, they must be balanced.

'''
import sys

cell = [0 for x in range(0, 10000)] # Create 10000 empty cells
position = 0
bfstack = [] # stack used for brainfuck while loops only
ifile = open(sys.argv[1]) # open up the .bf file supplied in command-line arguments
code = ifile.read()
code = code.replace("\n", "")
stop = len(code)
ifile.close()

# functions for brainfuck operations

# increments value of cell at current position
def inc_cell():
    global cell
    global position
    cell[position] += 1

# decrements value of cell at current position
def dec_cell():
    global cell
    global position
    cell[position] -= 1

# move position one over to the right
def move_cell_right():
    global position
    if position == 9999:
        position = 0
    else:
        position += 1

# move position one over to the left
def move_cell_left():
    global position
    if position == 0:
        position = 9999
    else:
        position -= 1

# Print ASCII value of decimal number of cell at current position
def print_cell_chr():
    global cell
    global position
    print(chr(cell[position]), end="")
    
# end functions

def bfeval(index):
    # reference the variables outside the function for use in function
    global code
    global cell
    global position
    global bfstack

    # while loop traverses the entire string in code which contains brainfuck code
    while index < stop:

        # evaluate brainfuck code based on which of the 8 commands it sees
        if code[index] == '+':
            inc_cell()
        elif code[index] == '-':
            dec_cell()
        elif code[index] == '.':
            print_cell_chr()
        elif code[index] == '>':
            move_cell_right()
        elif code[index] == '<':
            move_cell_left()
        elif code[index] == ',':
            print(input())

        # The '[' and ']' indicate a loop in brainfuck
        # When if first encounters '[', it checks whether the current cell
        # is 0.
        # If it is, go to the next ']' and continue evaluating the
        # rest of the code.
        # Else, add the current index into bfstack which keeps track of
        # the spots in the string 'code' containing all the brainfuck
        # code where the start and end of the brainfuck loop is.
            
        elif code[index] == '[':
            if cell[position] == 0:
                while code[index] != ']':
                    index += 1
            else:
                bfstack.append(index)
        elif code[index] == ']':
            if cell[position] != 0:
                index = bfstack[-1]
            else:
                bfstack.pop()

        index += 1

# start evaluating the brainfuck code from the left of the string
bfeval(0)
