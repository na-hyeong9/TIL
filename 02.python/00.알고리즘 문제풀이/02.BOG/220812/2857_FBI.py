from re import L
import sys
sys.stdin = open ("input.txt")

li = [] 
for i in range(1,6):
    N = input()
    if 'FBI' in N:
        li.append(i)
if len(li) > 0:
    print(*li)
else:
    print('HE GOT AWAY!')