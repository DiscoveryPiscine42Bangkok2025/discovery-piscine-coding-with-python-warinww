import sys

if len(sys.argv) < 2:
    print("none")
    exit(0)
    
param = sys.argv[1:]
print(f"parameters: {len(param)}")
for i in param:
    print(f"{param[0]}: {len(param[0])}")
    param = param[1:]