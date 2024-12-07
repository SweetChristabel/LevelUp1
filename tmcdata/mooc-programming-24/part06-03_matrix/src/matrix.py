# write your solution here
def read_matrix(matrix: list):
    masterlist = []
    for line in matrix:
        linenrs = []
        nrs = line.split(",")
        for i in nrs:
            linenrs.append(int(i))
        masterlist.append(linenrs)    
    return masterlist

def matrix_sum():
    with open("matrix.txt") as matrix:
        masterlist = read_matrix(matrix)
        sum = 0
        for row in masterlist:
            for i in row:
                sum += i
    return sum


def matrix_max():
    with open("matrix.txt") as matrix:
        masterlist = read_matrix(matrix)
        winner = 0
        for row in masterlist:
            for i in row:
                winner = max(winner, i)
    return winner

def row_sums():
    with open("matrix.txt") as matrix:
        masterlist = read_matrix(matrix)
        rowsums = []
        for row in masterlist:
            rowsums.append(sum(row))
    return rowsums

if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()