inp = input("Give me a number: ")
inp = float(inp)

if (inp.is_integer()):
    print("This number is an integer.")
else:
    print("This number is a decimal.")