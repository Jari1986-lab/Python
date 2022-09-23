def is_valid_move(array, row, col, number):
    for x in range(9):
        if array[row][x] == number:
            return False
    for x in range(9):
        if array[x][col] == number:
            return False
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if array[corner_row + x][corner_col + y] == number:
                return False
    return True

def solve(sudoku, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    if sudoku[row][col] > 0: 
        return solve(sudoku, row, col + 1)
    for num in range(1, 10):
        if is_valid_move(sudoku, row, col, num):
             sudoku[row][col] = num
             if solve(sudoku, row, col + 1):
                return True

        sudoku[row][col] = 0
    return False

sudoku = [
        [0,0,0,0,8,0,3,0,0],
        [7,0,0,2,0,0,0,0,0],
        [0,2,0,0,0,0,0,0,4],
        [2,0,0,0,0,0,0,0,0],
        [0,0,0,0,3,0,5,0,0],
        [0,0,0,0,5,0,4,0,0],
        [0,0,7,0,0,3,0,0,0],
        [0,1,0,0,0,0,0,0,3],
        [3,0,0,0,0,0,0,0,0]
        ]

if solve(sudoku, 0, 0):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=' ')
        print()
else:
    print('No Solution For This Sudoku')
