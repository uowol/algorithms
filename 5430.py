import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    command = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1]
    if len(arr) > 0:
        arr = list(map(int, arr.split(',')))

    left = 0
    right = n
    r = 1

    for i in range(len(command)):
        if command[i] == 'R':
            r *= -1
        else:
            if r == 1:
                left += 1
                if left > right:
                    print('error')
                    r = 0
                    break
            elif r == -1:
                right -= 1
                if left > right:
                    print('error')
                    r = 0
                    break

    if r == 0: continue

    if left == right: 
        print('[]')
        continue
    
    res = '['
    if r == 1:
        while left < right:
            res = res + str(arr[left]) + ','
            left+=1
    elif r == -1:
        while left < right:
            res = res + str(arr[right-1]) + ','
            right-=1
    res = res[0:-1] + ']'
    print(res)




    # list(map(int, 