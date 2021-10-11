print(f"A simple calculator!")
num1 = input("First number: ")

if num1.isnumeric() == False:
    print("Input is not a number")
    exit()
operator = input("Operator: ")
num2 = input("Second number: ")

if num2.isnumeric() == False:
    print("Input is not a number")
    exit()

num1 = int(num1)
num2 = int(num2)
if operator == "+":
    total = num1 + num2
    print(f"Sum is {total}")
elif operator == "-":
    total = num1 - num2
    print(f"Difference is {total}")
elif operator == "*":
    total = num1 * num2
    print(f"Product is {total}")
elif operator == "/":
    total = num1 / num2
    print(f"Quotient is {total}")
elif operator == "%":
    total = num1 % num2
    print(f"Modulus is {total}")
elif operator == "**":
    total = num1 ** num2
    print(f"Exponent is {total}")
else:
    print("Operation not recognized.")