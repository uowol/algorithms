# 나는야 포켓몬 마스터 이다솜

import sys


class Node:
    def __init__(self, char):
        self.char = char
        self.values = []
        self.next = []
        self.end = -1
    def update(self, value):
        self.values.append(value)
    def __str__(self):
        return str(self.char)

class Tree:
    def __init__(self):
        self.roots = []
    def addRoot(self, node):
        self.roots.append(node)
    def selectRoot(self, character):
        for root in self.roots:
            if root.char == character:
                return(root)
        new_node = Node(character)
        self.addRoot(new_node)
        return new_node


def search(node, c):
    _next = node.next
    for next_node in _next:
        if next_node.char == c:
            return(next_node)
    new_node = Node(character)
    node.next.append(new_node)
    return(new_node)        


M, N = map(int, sys.stdin.readline().rstrip().split(' '))

arr_dict = [0 for i in range(M+1)]
tree = Tree()

# testcase = ['Pidgey', 'Pidgeotto', 'Pidgeot']
#(sys.stdin.readline().rstrip())
for i in range(1, M+1):
    arr_dict[i] = (sys.stdin.readline().rstrip())
    chars = list(arr_dict[i])
    first_char = chars[0]
    now = tree.selectRoot(first_char)
    now.update(i)
    for j in range(1, len(chars)):
        character = chars[j]
        next_node = search(now, character)
        now = next_node
        now.update(i)
    now.end = i

for i in range(N):
    _input = (sys.stdin.readline().rstrip())
    if _input[0].isupper():
        idx = 0
        char = _input[idx]
        now = tree.selectRoot(char)
        answer = None
        while len(now.next) != 0:
            # print(str(now))
            if len(now.values) == 1:
                answer = now.values[0]
                break
            if len(_input)-1 == idx:
                answer = now.end
                break
            idx += 1
            # char = _input[idx]
            now = search(now, _input[idx])
        if not answer: answer = now.values[0]
        print(answer)
    else:
        print(arr_dict[int(_input)])