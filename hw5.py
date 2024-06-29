# 1
strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

longest_string = ""
index_of_longest = -1

for index, string in enumerate(strings):
    if len(string) > len(longest_string):
        longest_string = string
        index_of_longest = index

print("The longest string in the list is:", longest_string)
print("The index of the longest string is:", index_of_longest)

# 2

strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

capitalized_strings = [string.capitalize() for string in strings]

for string in capitalized_strings:
    print(string[0])

# 3

my_list = [1, "apple", 3.14, True, None, "banana"]

for element in reversed(my_list):
    print(element)

# 4

my_list = [1, 3, 5, 7, 9, 11, 13, 15]

number = int(input("Enter an integer: "))

if number in my_list:
    print("YES")
else:
    print("NO")

# 5
from collections import Counter

strings = ["apple", "banana", "apple", "cherry", "banana", "banana", "fig", "apple"]

string_counts = Counter(strings)

for string, count in string_counts.items():
    print(f"{string}: {count}")

# 6

def rearrange_array(arr):
    even_part = []
    odd_part = []

    for num in arr:
        if num % 2 == 0:
            even_part.append(num)
        else:
            odd_part.append(num)

   
    rearranged_array = even_part + odd_part[::-1]

    return rearranged_array


array = [3, 5, 2, 8, 1, 6, 7, 4]
result = rearrange_array(array)
print("Original Array:", array)
print("Rearranged Array:", result)

# 7
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print() 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix elements:")
print_matrix(matrix)
