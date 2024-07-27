# 1
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = [list(row)[::-1] for row in matrix[::-1]]

for row in rotated_matrix:
    print(row)

#   2
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

for row in transpose_matrix:
    print(row)

    # 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

for row in transposed:
    print(row)
      