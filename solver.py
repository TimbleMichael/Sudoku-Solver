import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,7],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

## Function for printing the grid in the sudoku format for easy reading
def printGrid(board):

    # This FOR loop, loops through each ROW that satisifies the conditions (i != 0 and i%3 = 0)
    # Then prints the line after the THIRD and SIXTH line, as when you i=3/3 and i=6/3, has 0-remainder. 
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        # This FOR loop, is used to create 
        for j in range(len(board)):
            if j%3 == 0 and j != 0:
                print(" | ",end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ",end="")

def possible(row,column,number):
    global grid

    for i in range(0,9):
        if grid[row][i] == number:
            return False
    
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    x0 = (column//3) * 3
    y0 = (row//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0 + i] [x0 + j] == number:
                return False
                
    return True

def solve():
    global grid

    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row,column,number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return 
    
    print (np.matrix(printGrid(grid)))
    

solve()
   
       





