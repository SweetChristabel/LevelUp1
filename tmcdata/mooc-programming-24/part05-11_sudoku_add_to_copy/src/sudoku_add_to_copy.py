def print_sudoku(sudoku: list):
    rep2 = 0
    for row in sudoku:
        if rep2 != 0 and rep2 % 3 == 0:
            print()
        printrow = ""
        rep = 0
        for i in row:
            if rep != 0 and rep % 3 == 0:
                printrow += " "    
            if i == 0:
                printrow += "_ "
            else:
                printrow += str(i)+" "
            rep +=1
        rep2 += 1
        print(printrow)

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku2 = []
    for row in sudoku:
        sudoku2.append(row[:])
    sudoku2[row_no][column_no] = number
    return sudoku2



if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)