def block_correct(sudoku:list, row_no: int, column_no: int):
    test = sudoku[row_no]
    test2 = sudoku[column_no]
    for i in range(1, 10):
        for i in range(0, 9):
                test2.append(sudoku[i][column_no])
        if test.count(i) < 1 and test2.count(i) > 1:
    
         
            return False
    return True

sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0],
          [2, 0, 0, 2, 5, 0, 7, 0, 0],
          [0, 2, 0, 3, 0, 0, 0, 0, 4],
          [2, 9, 4, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 7, 3, 0, 5, 6, 0],
          [7, 0, 5, 0, 6, 0, 4, 0, 0],
          [0, 0, 7, 8, 0, 3, 9, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 3],
          [3, 0, 0, 0, 0, 0, 0, 0, 2]]

print(block_correct(sudoku, 0, 0))
print(block_correct(sudoku, 1, 2))

