name = input("Add your name:")

if name.isalpha():
    name = str(name)
else:
    print("enter true information!")
    exit()

age = input("add your age:")
if age.isdigit():
    age = int(age)
else:
    print("inter true value!")
    exit()

address = input("add your address:")

if type(name) is str and type(age) is int :
    print(f"Hello Mr/Ms {name} age {age} located in {address} thanks for being one of our community , Enjoy ")