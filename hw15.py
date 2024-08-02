# 1
def multiplier(factor):
    return lambda x: x * factor

double = multiplier(2)
triple = multiplier(3)

print(double(5))  
print(triple(5))  

# 2
def make_adder(n):
    return lambda x: x + n

add_five = make_adder(5)
add_ten = make_adder(10)

print(add_five(3))  
print(add_ten(3))   

# 3
def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x

result = apply_twice(square, 3)
print(result)  

# 4
def compose(f, g):
    return lambda x: f(g(x))

def add_one(x):
    return x + 1

def square(x):
    return x * x

add_one_then_square = compose(square, add_one)

result = add_one_then_square(3)
print(result)  

# 5
def power_factory(n):
    return lambda x: x ** n

square = power_factory(2)
cube = power_factory(3)

print(square(4))  
print(cube(2))    

# 6
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)

# 7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)  

# 8
def make_greeting(greeting):
    def greet(name):
        print(f"{greeting}, {name}!")
    return greet

hello_greeting = make_greeting("Hello")
good_morning_greeting = make_greeting("Good morning")

hello_greeting("Alice")        
good_morning_greeting("Bob")   

# 9
def make_accumulator(start=0):
    total = start
    def accumulator(value):
        nonlocal total
        total += value
        return total
    return accumulator

acc = make_accumulator(10)
print(acc(5))   
print(acc(3))   
print(acc(-2))  

acc2 = make_accumulator()
print(acc2(1))  
print(acc2(4))  

# 10
def make_config(key, value):
    def config():
        return {key: value}
    return config

config1 = make_config("username", "alice")
config2 = make_config("timeout", 30)

print(config1())  
print(config2())

# 11
def make_logger(level):
    def logger(message):
        print(f"[{level}] {message}")
    return logger

info_logger = make_logger("INFO")
error_logger = make_logger("ERROR")

info_logger("This is an informational message.")  
error_logger("This is an error message.")          

# 12
def make_memoize(f):
    cache = {}
    def memoized_function(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    return memoized_function


def slow_add(x, y):
    print("Computing...")
    return x + y


memoized_add = make_memoize(slow_add)

print(memoized_add(1, 2))  
print(memoized_add(1, 2))  
print(memoized_add(2, 3))  

# 13
def bar(n):
    functions = []
    for i in range(n):
        def multiplier(x, i=i):  
            return x * i
        functions.append(multiplier)
    return functions


funcs = bar(5)


for i, func in enumerate(funcs):
    print(f"Function {i}:")
    print(f"  Result of func(10): {func(10)}")  
    print(f"  Closure: {func.__closure__}")    
    print(f"  Free variables: {func.__closure__[0].cell_contents}")  
    print()


# 14
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculate(operand1, operand2, operator):
    if operator not in operations:
        raise ValueError(f"Operator {operator} not supported.")
    return operations[operator](operand1, operand2)


print(calculate(10, 5, '+'))  
print(calculate(10, 5, '-'))  
print(calculate(10, 5, '*'))  
print(calculate(10, 5, '/'))  

# 15

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def to_title_case(s):
    return s.title()

def reverse_string(s):
    return s[::-1]


string_operations = {
    'uppercase': to_uppercase,
    'lowercase': to_lowercase,
    'title': to_title_case,
    'reverse': reverse_string
}

def manipulate_string(s, operation):
    if operation not in string_operations:
        raise ValueError(f"Operation '{operation}' not supported.")
    return string_operations[operation](s)


print(manipulate_string("hello world", "uppercase"))  
print(manipulate_string("HELLO WORLD", "lowercase"))  
print(manipulate_string("hello world", "title"))       
print(manipulate_string("hello world", "reverse"))     

# 16
import math


def area_circle(radius):
    return math.pi * radius ** 2

def area_square(side):
    return side ** 2

def area_rectangle(width, height):
    return width * height

def area_triangle(base, height):
    return 0.5 * base * height


area_calculators = {
    'circle': area_circle,
    'square': area_square,
    'rectangle': area_rectangle,
    'triangle': area_triangle
}

def calculate_area(shape, **kwargs):
    if shape not in area_calculators:
        raise ValueError(f"Shape '{shape}' not supported.")
    return area_calculators[shape](**kwargs)


print(calculate_area('circle', radius=5))          
print(calculate_area('square', side=4))             
print(calculate_area('rectangle', width=4, height=5))  
print(calculate_area('triangle', base=4, height=3))  


# 17


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


temperature_conversions = {
    ('Celsius', 'Fahrenheit'): celsius_to_fahrenheit,
    ('Celsius', 'Kelvin'): celsius_to_kelvin,
    ('Fahrenheit', 'Celsius'): fahrenheit_to_celsius,
    ('Fahrenheit', 'Kelvin'): fahrenheit_to_kelvin,
    ('Kelvin', 'Celsius'): kelvin_to_celsius,
    
}

# 18
import math

# Define financial calculation functions
def compound_interest(principal, rate, time, n):
    """Calculate compound interest."""
    return principal * (1 + rate / n) ** (n * time)

def loan_payment(principal, annual_rate, months):
    """Calculate monthly loan payment."""
    monthly_rate = annual_rate / 12 / 100
    return (principal * monthly_rate) / (1 - math.pow(1 + monthly_rate, -months))

def investment_return(principal, rate, time):
    """Calculate future value of an investment."""
    return principal * (1 + rate) ** time


financial_operations = {
    'compound_interest': compound_interest,
    'loan_payment': loan_payment,
    'investment_return': investment_return
}

def financial_calculator(operation, **kwargs):
    if operation not in financial_operations:
        raise ValueError(f"Operation '{operation}' not supported.")
    return financial_operations[operation](**kwargs)


print(financial_calculator('compound_interest', principal=1000, rate=0.05, time=5, n=4))


print(financial_calculator('loan_payment', principal=30000, annual_rate=5, months=60))


print(financial_calculator('investment_return', principal=1000, rate=0.07, time=10))

# 19
import statistics

def mean(data):
    return statistics.mean(data)

def median(data):
    return statistics.median(data)

def mode(data):
    try:
        return statistics.mode(data)
    except statistics.StatisticsError:
        return "No unique mode"

def standard_deviation(data):
    return statistics.stdev(data)


data_operations = {
    'mean': mean,
    'median': median,
    'mode': mode,
    'standard_deviation': standard_deviation
}

def analyze_data(data, operation):
    if operation not in data_operations:
        raise ValueError(f"Operation '{operation}' not supported.")
    return data_operations[operation](data)


data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

print(analyze_data(data, 'mean'))                 
print(analyze_data(data, 'median'))               
print(analyze_data(data, 'mode'))                 
print(analyze_data(data, 'standard_deviation'))   


# 20
import os


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def append_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)

def delete_file(file_name):
    os.remove(file_name)


file_operations = {
    'read': read_file,
    'write': write_file,
    'append': append_file,
    'delete': delete_file
}

def file_manager(file_name, operation, content=None):
    if operation not in file_operations:
        raise ValueError(f"Operation '{operation}' not supported.")
    if operation in ['write', 'append'] and content is None:
        raise ValueError("Content must be provided for 'write' and 'append' operations.")
    return file_operations[operation](file_name) if operation == 'read' or operation == 'delete' else file_operations[operation](file_name, content)


file_manager('example.txt', 'write', 'Hello, world!\n')

file_manager('example.txt', 'append', 'Appending some text.\n')


print(file_manager('example.txt', 'read'))  


file_manager('example.txt', 'delete')

# 21
def sort_list(lst):
    return sorted(lst)

def reverse_list(lst):
    return lst[::-1]

def filter_list(lst, predicate):
    return list(filter(predicate, lst))

def map_list(lst, func):
    return list(map(func, lst))


list_operations = {
    'sort': sort_list,
    'reverse': reverse_list,
    'filter': filter_list,
    'map': map_list
}

def transform_list(lst, operation, func=None):
    if operation not in list_operations:
        raise ValueError(f"Operation '{operation}' not supported.")
    if operation in ['filter', 'map'] and func is None:
        raise ValueError(f"A function must be provided for '{operation}' operation.")
    if operation == 'filter' or operation == 'map':
        return list_operations[operation](lst, func)
    else:
        return list_operations[operation](lst)

numbers = [1, 2, 3, 4, 5]

print(transform_list(numbers, 'sort'))             
print(transform_list(numbers, 'reverse'))          
print(transform_list(numbers, 'filter', lambda x: x % 2 == 0))  
print(transform_list(numbers, 'map', lambda x: x ** 2))          

# 22

import math


def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def square_root(n):
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(n)

def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute the factorial of a negative number.")
    return math.factorial(n)


math_functions = {
    'square': square,
    'cube': cube,
    'square_root': square_root,
    'factorial': factorial
}

def math_operations(number, operation):
    if operation not in math_functions:
        raise ValueError(f"Operation '{operation}' not supported.")
    if operation == 'factorial' and (number < 0 or not number.is_integer()):
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math_functions[operation](number)


print(math_operations(4, 'square'))         
print(math_operations(3, 'cube'))           
print(math_operations(9, 'square_root'))    
print(math_operations(5, 'factorial'))     


# 23
def word_count(text):
    return len(text.split())

def character_count(text):
    return len(text)

def find_word(text, word):
    words = text.split()
    return [i for i, w in enumerate(words) if w == word]

def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)


text_operations = {
    'word_count': word_count,
    'character_count': character_count,
    'find_word': find_word,
    'replace_word': replace_word
}

def process_text(text, operation, **kwargs):
    if operation not in text_operations:
        raise ValueError(f"Operation '{operation}' not supported.")
    if operation == 'find_word' and 'word' not in kwargs:
        raise ValueError("The 'find_word' operation requires a 'word' argument.")
    if operation == 'replace_word' and ('old_word' not in kwargs or 'new_word' not in kwargs):
        raise ValueError("The 'replace_word' operation requires 'old_word' and 'new_word' arguments.")
    return text_operations[operation](text, **kwargs)


text = "hello world hello universe"

print(process_text(text, 'word_count'))                
print(process_text(text, 'character_count'))           
print(process_text(text, 'find_word', word='hello'))   
print(process_text(text, 'replace_word', old_word='hello', new_word='hi'))  
