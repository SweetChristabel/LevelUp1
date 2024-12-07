def count_matching_elements(my_matrix: list, element: int):
    result = 0
    for row in my_matrix:
        result += row.count(element)
    return result

if __name__ == "__main__":
    matroopster = [[1, 2, 6, 3, 4],[5, 2, 6, 3, 5], [1, 2, 0, 2, 5], [3, 1, 5, 2, 1], [2, 1, 5, 2, 4]]
    print(count_matching_elements(matroopster, 5))