inp = input("Please tell me your age: ")
inp = int(inp)
ls = [10, 20, 30]

print(f"You are currently {inp} years old.")
for i in ls:
    age = i+inp
    print(f"In {i} years, you'll be {age} years old.")