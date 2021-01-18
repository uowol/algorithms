import sys
input = sys.stdin.readline

exp = input().rstrip()

num = []
operator = []

def isNaN(num):
    return num != num

def operate(num, operator):
    res = num[0]
    for i in range(len(operator)):
        if operator[i] == '-':
            res = res - num[i+1]
        else:
            res = res + num[i+1]
    return(res)

_num = ''
for n in exp:
    try:
        int(n)
        _num = _num + n
    except:
        operator.append(n)
        num.append(int(_num))
        _num = ''
num.append(int(_num))

_min = operate(num, operator)
next_num = num
next_operator = operator

while len(operator)>1:
    for i in range(len(operator)):
        b_num = num[:i]
        b_operator = operator[:i]
        a_num = num[i+2:]
        a_operator = operator[i+1:]
        if operator[i] == '-':
            _num = b_num + [num[i]-num[i+1]] + a_num
            _operator = b_operator + a_operator
        else:
            _num = b_num + [num[i]+num[i+1]] + a_num
            _operator = b_operator + a_operator
        res = operate(_num, _operator)
        if _min >= res:
            next_num = _num
            next_operator = _operator
            _min = res
    num = next_num
    operator = next_operator

print(operate(num, operator))
