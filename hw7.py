# 1
def insert_at_index(lst, index, value):
    
    if index < 0 or index > len(lst):
        raise IndexError("Index out of range")

  
    new_lst = lst[:index] + [value] + lst[index:]

    return new_lst


my_list = [1, 2, 4, 5]
index_to_insert = 1
value_to_insert = 3

result = insert_at_index(my_list, index_to_insert, value_to_insert)
print("Original List:", my_list)
print(f"List after inserting {value_to_insert} at index {index_to_insert}:", result)

# 2
def remove_first_occurrence(lst, value):
  
    if value in lst:
        
        index = lst.index(value)
        
        
        new_lst = lst[:index] + lst[index+1:]
        
        return new_lst
    else:
        print(f"{value} not found in the list.")
        return lst


my_list = [1, 2, 3, 2, 4]
element_to_remove = 2

result = remove_first_occurrence(my_list, element_to_remove)
print(f"List after removing {element_to_remove}: {result}")

# 3
def remove_last_element(lst):
    
    if not lst:
        return "List is empty"
    
   
    last_element = lst[-1]
    new_lst = lst[:-1]
    
    return last_element, new_lst


my_list = [1, 2, 3]

result, modified_list = remove_last_element(my_list)
print(f"Removed element: {result}")
print(f"Modified List: {modified_list}")

# 4
def clear_list(lst):
    
    while lst:
        lst.pop()


my_list = [1, 2, 3]

print("Original List:", my_list)
clear_list(my_list)
print("List after clearing:", my_list)

# 5

squares = [i ** 2 for i in range(1, 11)]

print(squares)

# 6

even_numbers = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 == 0]


print(even_numbers)
