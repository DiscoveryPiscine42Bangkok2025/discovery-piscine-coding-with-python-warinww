import sys

if len(sys.argv) != 3:
    print("none")
    exit(0)

start = int(sys.argv[1])
end = int(sys.argv[2])
ans = []

while start <= end:
    ans.append(start)
    start += 1

print(ans)
