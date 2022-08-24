from re import L
import sys


import sys
sys.stdin = open("input.txt")

N = int(input())

for _ in range(N):
    A, B = map(str, input().split())
    
    a = sorted(list(A))
    b = sorted(list(B))

    if a == b:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')
