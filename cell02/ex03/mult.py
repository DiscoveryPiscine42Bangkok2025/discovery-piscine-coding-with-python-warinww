f_num = input("Enter the first number:\n")
s_num = input("Enter the second number:\n")
result = int(f_num)*int(s_num)

print(f"{f_num} x {s_num} = {result}")

if (result > 0):
    print("This number is positive.")
elif (result < 0):
    print("This number is negative.")
else:
    print("This number is both positive and negative.")