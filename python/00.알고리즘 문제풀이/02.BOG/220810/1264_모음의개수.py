import sys
sys.stdin = open ("input.txt")
T = 4

collection = ['a', 'e', 'i', 'o', 'u']
while True:
    sen = input().lower()
    cnt = 0
    if sen == '#':
        break
    for _ in collection:
        cnt += sen.count(_)
    print(cnt) 
    
        