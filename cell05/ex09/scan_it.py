import sys

if len(sys.argv) < 3:
    print("none")
    exit(0)

key, text = sys.argv[1], sys.argv[2]

count = text.count(key)
print(count)