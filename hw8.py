# 1
def are_arrays_same(array1, array2):
    
    if len(array1) != len(array2):
        return False
    
  
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    
    return True


array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 3, 4, 5]
array3 = [1, 2, 3, 4, 6]

print(are_arrays_same(array1, array2))  
print(are_arrays_same(array1, array3))  

# 2
def get_user_input():
    n = int(input("Enter the number of elements in the array: "))
    array = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        array.append(element)
    return array

def find_index_difference(array):
    if len(array) == 0:
        return None
    
    min_index = 0
    max_index = 0
    
    for i in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
        if array[i] > array[max_index]:
            max_index = i
    
    return abs(max_index - min_index)


user_array = get_user_input()
difference = find_index_difference(user_array)

if difference is not None:
    print(f"The difference between the indices of the largest and smallest elements is: {difference}")
else:
    print("The array is empty.")

# 3

def get_square_matrix():
    n = int(input("Enter the size of the square matrix (n x n): "))
    matrix = []
    
    print("Enter the elements row by row:")
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    print("The matrix is:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


square_matrix = get_square_matrix()
print_matrix(square_matrix)

# 4
def get_square_matrix():
    n = int(input("Enter the size of the square matrix (n x n): "))
    matrix = []
    
    print("Enter the elements row by row:")
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    print("The matrix is:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def swap_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        
        matrix[i][i], matrix[i][n-i-1] = matrix[i][n-i-1], matrix[i][i]


square_matrix = get_square_matrix()
print("Original matrix:")
print_matrix(square_matrix)

swap_diagonals(square_matrix)
print("Matrix after swapping diagonals:")
print_matrix(square_matrix)

# 5
def get_square_matrix():
    n = int(input("Enter the size of the square matrix (n x n): "))
    matrix = []
    
    print("Enter the elements row by row:")
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    print("The matrix is:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def sum_main_diagonal(matrix):
    n = len(matrix)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

square_matrix = get_square_matrix()
print_matrix(square_matrix)

main_diagonal_sum = sum_main_diagonal(square_matrix)
print(f"The sum of the elements of the main diagonal is: {main_diagonal_sum}")

# 6
def get_square_matrix():
    n = int(input("Enter the size of the square matrix (n x n): "))
    matrix = []
    
    print("Enter the elements row by row:")
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    print("The matrix is:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def sum_auxiliary_diagonal(matrix):
    n = len(matrix)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][n-i-1]
    return diagonal_sum


square_matrix = get_square_matrix()
print("The entered matrix is:")
print_matrix(square_matrix)

auxiliary_diagonal_sum = sum_auxiliary_diagonal(square_matrix)
print(f"The sum of the elements of the auxiliary diagonal is: {auxiliary_diagonal_sum}")

# 7
def get_matrix():
    n = int(input("Enter the number of rows (N): "))
    m = int(input("Enter the number of columns (M): "))
    matrix = []
    
    print("Enter the elements row by row:")
    for i in range(n):
        row = []
        for j in range(m):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    
    return matrix

def print_matrix(matrix):
    print("The matrix is:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def find_max_value(matrix):
    max_value = matrix[0][0]
    for row in matrix:
        for element in row:
            if element > max_value:
                max_value = element
    return max_value


matrix = get_matrix()
print_matrix(matrix)

max_value = find_max_value(matrix)
print(f"The largest value in the matrix is: {max_value}")
