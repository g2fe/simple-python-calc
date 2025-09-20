number1 = input("Enter Your First Number: ") # /// takes user input for the first number
number2 = input("Enter Your Second Number: ") # // takes user input for the second number
operation = input("Choose operation (+, -, *, /): ")   # /// takes user input for numbers and operation
if operation == "+":
 summary = float(number1) + float(number2)  # /// handles the addition operation    
elif operation == "-":
    summary = float(number1) - float(number2) # /// handles the subtraction operation
elif operation == "*":
    summary = float(number1) * float(number2) # /// handles the multiplication operation
elif operation == "/":
    summary = float(number1) / float(number2) # /// handles the division operation
else :
    summary = "Invalid Operation"  # /// handles the invalid operation

# /// prints the restult
print("The Result is: " , (summary))
