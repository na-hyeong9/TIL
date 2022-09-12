T = int(input())

for i in range(1,T+1):
    number = map(int, input().split())
    odd = 0
    for j in number:
        if not j % 2 == 0:
            odd += i
            
    print(f'#{j} {odd}')
