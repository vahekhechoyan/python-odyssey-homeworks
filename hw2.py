# Գրել ծրագիր, որը կտպի 1-ից 10 թվերի քառակուսիները:
    
for i in range(1, 11):
	sq = i * i
	print(sq, end=" ")


# Գրել ծրագիր, որը տրված թվերի ցուցակից կընտրի միայն դրական թվերը և կտպի դրանք:

numbers = [-5, 3, -1, 101, -33, 44, 0, 7]

for number in numbers:

    if number > 0:
        
        print(number)


# Գրել ծրագիր, որը կտպի 1-ից 20 միջակայքում գտնվող այն թիվերը, որոնք բազմապատիկ են 3-ի:
for number in range(1,21):
     if number % 3 == 0:
         
          print(number)       	  


# Գրել ծրագիր, որը կտպի տրված բառի յուրաքանչյուր տառը և իր ինդեքսը՝
word="Python"

for index , letter in enumerate(word):
     
     print(f'"{letter}" {index}')
     

# Պարզ հաշվիչի ստեղծում. 
def calculator():
  
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

   
    if operation in ['1', '2', '3', '4']:
  
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '1':
            result = num1 + num2
            operation_symbol = '+'
        elif operation == '2':
            result = num1 - num2
            operation_symbol = '-'
        elif operation == '3':
            result = num1 * num2
            operation_symbol = '*'
        elif operation == '4':
            
            if num2 != 0:
                result = num1 / num2
                operation_symbol = '/'
            else:
                print("Error: Division by zero is not allowed.")
                return

        
        print(f"The result of {num1} {operation_symbol} {num2} is: {result}")
    else:
        print("Invalid input. Please select a valid operation.")


calculator()
