# Write your solution here
def transpose(matrix: list):
    output = []
    index = 0
    while index < len(matrix):
        row = []
        for item in matrix:
            row.append(item[index])
        output.append(row)
        index += 1
    matrix[:] = output





if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    transpose(matrix)
    print(matrix)