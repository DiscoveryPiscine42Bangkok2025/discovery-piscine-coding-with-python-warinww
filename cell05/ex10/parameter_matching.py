import sys

if len(sys.argv) != 2:
    print("none")
    exit(0)

param = sys.argv[1]
inp = input("What was the parameter? ")

if inp == param:
    print("Good job!")
else:
    print("Nope, sorry...")
