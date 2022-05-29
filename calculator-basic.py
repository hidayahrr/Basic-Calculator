num1 = float(input("Enter number here: "))
operation = input("Enter operator here: ")
num2 = float(input("Enter number here: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "*":
    print(num1 * num2)
else:
    print("invalid operation")
