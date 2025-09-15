import sys

if len(sys.argv) < 2:
    print("none")
    exit(0)

ans = sys.argv[1:]
ans.reverse()

print("\n".join(ans))