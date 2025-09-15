import sys

if len(sys.argv) < 2:
    print("none")
    exit(0)
    
ans = []
    
inp = sys.argv[1]
for i in inp:
    if (i == 'z'):
        ans.append("z")
print("".join(ans))
        
if len(ans) == 0:
    print("none")