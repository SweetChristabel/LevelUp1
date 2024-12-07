# Write your solution here
def row_correct(sudoku: list):
    for i in range(1, 10):
        amt = sudoku[i-1].count(i)
        if amt == 0 or amt == 1:
            continue
        else:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no])
    for i in range(1, 10):
        nr = column.count(i)
        if nr == 0 or nr == 1:
            continue
        else:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    for a in range(0, 3):    
        for i in range(0, 3):
            block.append(sudoku[row_no][column_no+i])
        row_no += 1
    
    for i in range(1, 10):
        if block.count(i) == 0 or block.count(i) == 1:
            continue
        else:
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    if row_correct(sudoku) == False:
        return False
        
    for i in range(0, len(sudoku)):
        if column_correct(sudoku, i) == False:
            return False
    
    row = [0, 3, 6]
    col = [0, 3, 6]

    for x in row:
        for y in col:
            if block_correct(sudoku, x, y) == False:
                return False
    return True        
        
if __name__ == "__main__":

    sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
