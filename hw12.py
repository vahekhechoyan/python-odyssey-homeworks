# 1
def print_list_elements(ls):
    for element in ls:
        print(element)

ls = [1,2,3,4]
print_list_elements(ls)

# 2
def print_numbers(n):
    for i in range(n+1):
        print(i)

n = 5
print_numbers(n)

# 3
def print_numbers(n):
    for i in range(n, -1, -1):
        print(i)

n = 5
print_numbers(n)

# 4
def first_uppercase_letter(string):
    for char in string:
        if char.isupper():
            return char
    return None


string = "hello World"
print(first_uppercase_letter(string))

# 5
def get_minimum_element(ls):
    return min(ls)

def get_maximum_element(ls):
    return max(ls)

ls = [1,2,3,4]
print(get_minimum_element(ls))
print(get_maximum_element(ls))

# 6
def sum_of_digits(number):
    number_str = str(number)
    total = 0
    for digit in number_str:
        total += int(digit)
    return total

number = 123
print(sum_of_digits(number))

