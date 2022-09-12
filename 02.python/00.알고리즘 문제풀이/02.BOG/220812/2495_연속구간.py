from re import L
import sys
sys.stdin = open ("input.txt")

for _ in range(3):
    s = str(input())
    max_num = 1
    cnt = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cnt+=1
        else:
            max_num = max(cnt,max_num)
            cnt=1
    max_num = max(cnt, max_num)
    print(max_num)