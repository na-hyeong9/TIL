import sys
sys.stdin = open ("input.txt")

N = int(input())
n = N
cnt = 0
while True:
    a = n // 10 # 10의 자리에 있는 수 6
    b = n % 10  # 1의 자리에 있는 수 8
    c = (a + b) % 10 # 각 자리에 있는 수를 더하고 1의 자리 수만 남김 14 -> 4
    n = (b * 10) + c
    cnt += 1 #사이클 횟수
    if n == N: # n 과 N이 같은 수가 될 때까지 while문 반복
        break
print(cnt)
