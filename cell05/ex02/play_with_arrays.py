inp = [2, 8, 9, 48, 8, 22, -12, 2]
print(inp)

new_array = []
i = 0

while i < len(inp):
    if inp[i] > 5:
        new_array.append(inp[i] + 2)
    i += 1

print(new_array)
