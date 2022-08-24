import sys
sys.stdin = open ("input.txt")

N = int(input())
M = int(input())
all = 0

for _ in range(M):
    money, cnt = map(int,input().split())
    all += money * cnt
if N == all:
    print('Yes')
else:
    print('No')