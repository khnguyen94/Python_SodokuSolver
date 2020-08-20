# Import all dependencies


# Initiate a sample sodoku board to be used in app
# Daily sudoku board from http://www.dailysudoku.com/sudoku/ (8/20/2020)
board = [
    [0, 0, 5, 0, 0, 8, 2, 0, 1],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [2, 1, 9, 0, 7, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 8, 4, 0, 9, 7, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 5, 0, 3, 4, 7],
    [0, 0, 0, 0, 0, 6, 0, 0, 0],
    [8, 0, 2, 7, 0, 0, 9, 0, 0]
]


# Function to print board to console
# Print rows in 3s, use a separator
# 9 rows
# Then within each row, print in columns in 3s, use a separator
# 9 columns in each row
def print_board(board):
    # Row, draw separator
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        # Column, draw separator
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end="")


# Run print_board, pass in board
print_board(board)

# Use Backtracking approach to find solution

# 1) Pick Empty Square
# Function to find an empty square, empty is when there is a 0 in that spot


def find_empty_func(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:  # empty is denoted by 0
                return (i, j)  # return (row, col) tuple

    # If no empty spaces left equal to 0, then return None, will trigger solution condition in solve_board function
    return None

# 2) Try All Numbers
# Function to check if current number being tried is valid
# Function will take 3 parameters: board, number, position


def is_valid_func(board, number, position):
    # Check Row
    for i in range(len(board[0])):
        # Check through each element of the row
        # No element in row can be the num
        # and that the position cannot be the position we just inserted a num into
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check Column
    for i in range(len(board)):
        # Check through each element of the column
        # No element in the column can be the num
        # and that position cannot be the position we just inserted a num into
        if board[i][position[1]] == number and position[0] != i:
            return False

        # Check Box
        # Figure out which box currently in

        # Boxes: (correlated to the board)
        # [0, 0], [0, 1], [0, 2]
        # [1, 0], [1, 1], [1, 2]
        # [2, 0], [2, 1], [2, 2]

        # Create variables to hold x and y for current box
        box_x = position[1] // 3 # take the col of position coordinate and divide by 3 to get box's x coordinate
        box_y = position[0] // 3 # take the row of position coordinate and divide by 3 to get box's y coordinate
        
        # Now that you have the x, y coordinate of the box youre in,
        # you need to use those x, y to get the range of indices (0-8) for the pos(row, col) you are in
        # EX: Box [2, 1] has indices of [x(3 -> 5), y(6 -> 8)]
        # EX: Box [2, 2] has indices of [x(6 -> 8), y(6 -> 8)]
    
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == number and (i, j) != position:
                    return False

        # If all these checks pass, return True
        return True

# 3) Solve the board
# Function that uses find_empty and is_valid functions to solve the board
def solve_board_func(board):
    # Initiate a variable and assign to it the active find_empty function
    find = find_empty_func(board)

    # if find_empty DOES NOT return a position tuple, then you have found the solution
    if not find:
        return True
    # else, if find_empty DOES return a position tuple, assign the x, y of that tuple to variables row and col
    else:
        row, col = find

        # 3) Find A Number that Works
        # 4) Repeat
        # 5) Backtrack (recursive checking)
