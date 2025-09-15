inp = input("Enter a number less than 25\n")
inp = int(inp)

if (inp > 25):
    print("ERROR")
else:
    while (inp <= 25):
        print(f"Inside the loop, my variable is {inp}")
        inp += 1