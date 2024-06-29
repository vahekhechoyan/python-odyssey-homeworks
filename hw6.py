# 1
my_string = "find the letter z"

index = my_string.find('z')
if index != -1:
    print(f"The index of 'z' is: {index}")
else:
    print("Character not found")

# 2

word = "capitalize"


if len(word) > 0:
    first_char = word[0]
    if 'a' <= first_char <= 'z':  
        uppercase_first_char = chr(ord(first_char) - 32)
        transformed_word = uppercase_first_char + word[1:]
        print("Original:", word)
        print("Transformed:", transformed_word)
    else:
        print("First character is not a lowercase letter")
else:
    print("String is empty")

# 3

sentence = "hello, world! are you ready?"

words = sentence.split()

title_case_words = []
for word in words:
    if word:
    
        first_char = word[0]
        if 'a' <= first_char <= 'z':  
            uppercase_first_char = chr(ord(first_char) - 32)
            title_case_word = uppercase_first_char + word[1:]
            title_case_words.append(title_case_word)
        else:
            title_case_words.append(word)  
    else:
        title_case_words.append(word)  


title_case_sentence = ' '.join(title_case_words)


print("Original:", sentence)
print("Transformed:", title_case_sentence)

# 4

original_string = "reverse me"


reversed_string = original_string[::-1]


print("Original String:", original_string)
print("Reversed String:", reversed_string)

# 5

word = "radar"

if word == word[::-1]:
    print("Yes")
else:
    print("No")

# 6

str1 = "hello"
str2 = "world"

result = str1 + " " + str2


print("Concatenated String:", result)

# 7

original_string = "banana"


modified_string = original_string.replace('a', 'x')

print("Original String:", original_string)
print("Modified String:", modified_string)
