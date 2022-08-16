import sys
sys.stdin = open("input.txt")

T = list(input())
word = 'CAMBRIDGE'

for i in range(len(word)):
    if word[i] in T:
        while word[i] in T: 
            T.remove(word[i])
print(''.join(T))
