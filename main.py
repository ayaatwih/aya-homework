list1 = []

for x in range(5):
    number1= input("enter the number:\n")
    list1.append(float(number1))

min = list1[0]
max = 0

for item in list1:
    if item < min:
        min = item
    elif item > max :
        max = item

print(max)
print(min)