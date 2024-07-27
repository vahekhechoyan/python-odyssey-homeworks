# 1
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

num = 5
print(f"the factorial of {num} is {recursive_factorial(num)}")

# 2
def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        return reverse_string(str[1:]) + str[0]

string = "hello"
print(f"reversed string of {string} is {reverse_string(string)}")

# 3
def find_length(ls):
    if not ls:
        return 0
    else:
        return 1 + find_length(ls[1:])

ls1 = [1, 2, 3, 4, 5]
print(f"the length of list is {find_length(ls1)}")  

# 4
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

number = 12345
print(f"The sum of digits of {number} is: {sum_of_digits(number)}")

# 5
def sum_of_natural_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_of_natural_numbers(n-1)

n = 5
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")

# 6
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")

# 7
def print_characters(string, index=0):
    if index >= len(string):
        return
    print(string[index])
    print_characters(string, index + 1)

string = "Hello, World!"
print_characters(string)

# 8
def print_list_elements(ls):
    if not ls:
        return
    print(ls[0])
    print_list_elements(ls[1:])

lst = [1, 2, 3, 4, 5]
print_list_elements(lst)

# 9
def print_numbers(n):
    if n <= 5:
        print(n)
        print_numbers(n + 1)

print_numbers(1)

# 10
def print_numbers(n):
    if n == 0:
        return
    else:
        print(n)
        print_numbers(n - 1)

print_numbers(5)

# 11
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

s = "anna"
print(is_palindrome(s))
