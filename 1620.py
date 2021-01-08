# 나는야 포켓몬 마스터 이다솜

import sys



M, N = map(int, sys.stdin.readline().rstrip().split(' '))
pokemonsById = [0 for i in range(M+1)]
pokemonsByStr = {}

for i in range(1, M+1):
    name = sys.stdin.readline().rstrip()
    pokemonsById[i] = name
    pokemonsByStr[name] = i

for i in range(N):
    ipt = sys.stdin.readline().rstrip()
    if ipt[0].isupper():
        print(pokemonsByStr[ipt])
    else:
        print(pokemonsById[int(ipt)])