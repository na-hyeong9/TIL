import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    N, M = input().split()
    N = int(N)
    print(M[:N-1], M[N:], sep = '')
