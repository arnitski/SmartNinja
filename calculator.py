x = input("first number?")
y = input("second number?")
operation = input("what calculation do you want to make? (+,-,* or /) ")

if operation == "+":
    print(int(x) + int(y))
elif operation == "-":
    print(int(x) - int(y))
elif operation == "/":
    print(int(x) / int(y))
elif operation == "*":
    print(int(x) * int(y))
else:
    print("computer says NO")