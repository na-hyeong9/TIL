import sys
sys.stdin = open ("input.txt")
N = int(input())
ind = [0] * N
for _ in range(N):
    x, y = map(int, input().split())
        
    if x > 0 and y > 0:
        ind[0] += 1
    if x < 0 and y > 0:
        ind[1] += 1    
    if x < 0 and y < 0:
        ind[2] += 1    
    if x > 0 and y < 0:
        ind[3] += 1    
    if x == 0 or y == 0:
        ind[4] += 1 
for i in range(len(ind)):
    if i == 4:
        print(f'AXIS: {ind[i]}')
        break
    print(f'Q{i+1}: {ind[i]}')   