import sys

def shrink(x):
    print(x[0:8])
    
def enlarge(x):
    while len(x) < 8:
        x += "z"
    print(x)
    
if len(sys.argv) < 2:
    print("none")
    exit(0)
    
for i in sys.argv[1:]:
    if len(i) > 8:
        shrink(i)
    elif len(i) < 8:
        enlarge(i)
    else:
        print(i)
        