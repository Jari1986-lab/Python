def sarake_oikein(sudoku:list, rivi_nro: int, sarake_nro: int):
    test = [sarake_nro]
    test2 = [rivi_nro]
    for i in range(0, 9):
        test.append(sudoku[i][sarake_nro])
        for i in range(1, 10):
            if test.count(i) > 1 or test2.count(i) > 1:
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

print(sarake_oikein(sudoku, 0, 0))
print(sarake_oikein(sudoku, 1, 2))
