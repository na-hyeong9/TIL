import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{test} {a//b} {a%b}')
