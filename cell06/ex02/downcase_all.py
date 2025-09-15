import sys

def downcase_it(x):
    return x.lower()

if len(sys.argv) < 2:
    print("none")
    exit(0)
    
for i in sys.argv[1:]:
    print(downcase_it(i))