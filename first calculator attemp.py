a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
user_input = str(input("What do you want to do? Add, Subtract, Multiply or Divide? "))
if user_input.lower() == "add":
    print(f"{a} + {b} = {a+b}")
elif user_input.lower() == "subtract":
    print(f"{a} - {b} = {a-b}")
elif user_input.lower() == "multiply":
    print(f"{a} * {b} = {a*b}")
elif user_input.lower() == "divide":
    print(f"{a} / {b} = {a/b}")

