import sys

if len(sys.argv) < 2:
    print("none")
    exit(0)
    
ans = []
    
inp = sys.argv[1:]
for i in inp:
    if "ism" not in i:
        print(f"{i}ism")