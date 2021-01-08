import sys

S = 0

M = int(sys.stdin.readline().rstrip())
for i in range(M):
    ipt = sys.stdin.readline().rstrip().split(' ')
    command = ipt[0]
    if len(ipt) == 2: 
        value = int(ipt[1])-1
    if command == 'add':
        S = S | 1 << value
    elif command == "check":
        print(S >> value & 1)
    elif command == "remove":
        S = S & ~(1 << value)
    elif command == "toggle":
        if S >> value & 1:
            S = S & ~(1 << value)
        else:
            S = S | 1 << value
    elif command == "all":
        S = 2**20-1
    elif command == "empty":
        S = 0


    

