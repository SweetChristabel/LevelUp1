# Write your solution here
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
    
    



if __name__ == "__main__":
    sudoku = [
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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))