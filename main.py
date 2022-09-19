import math


number1 = input("Add the first number:")

if number1.isalpha() or number1.isspace():
    print("Enter true value!")

print("____________________")
print("1. + \n2.- \n3.* \n4./ \n5.^ \n6.% ")

operation = input(" inter the opertion you need :")

number2 = input("Add the second number:")

if operation == "1" or operation == "+":
    result1 = float(number1) + float(number2)
    print(f"the result is {result1}")

elif operation == "2" or operation == "-":
    result1 = float(number1) - float(number2)
    print(f"the result is {result1}")

elif operation == "3" or operation == "*":
    result1 = float(number1) * float(number2)
    print(f"the result is {result1}")

elif operation == "4" or operation == "/":
    result1 = float(number1) / float(number2)
    print(f"the result is {result1}")

elif operation == "5" or operation == "^":
    result1 = float(number1) ^ float(number2)
    print(f"the result is {result1}")


elif operation == "6" or operation == "%":
    result1 = float(number1) % float(number2)
    print(f"the result is {result1}")

print("_________________")
operation2 = input("1.round \n2.floor \n3.ceil \n4.Integer \n5.exit \n.Enter the operation for result:")

if operation2 == "1":
    result = round(result1)
    print(f"the final result is {result}")

elif operation2 == "2":
    result = math.floor(result1)
    print(f"the final result is {result}")

elif operation2 == "3":
    result = math.ceil(result1)
    print(f"the final result is {result}")

elif operation2 == "4":
    result = int(result1)
    print(f"the final result is {result}")


elif operation2 == "5":
    print(f"the final result is {result1}")
    exit()




