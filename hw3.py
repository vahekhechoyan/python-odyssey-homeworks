# Write a program that asks the user to enter two numbers, x, and y, and computes x − y  /  x+y.
x = int(input("Enter an integer: ")) 
y = int(input("Enter an integer: ")) 
if(x + y == 0): 
    print("Division by zero error. |(x - y)| / (x + y) can't be evaluated.") 
else: 
    print("|(x - y)| / (x + y) = ", abs(x - y) / (x + y))

# Write a program that asks the user for weight in 
# kilograms and converts it to pounds. There are 2.2 pounds in a kilogram.

a=int(input("Enter your number"))
b=a*2.2
print(b)