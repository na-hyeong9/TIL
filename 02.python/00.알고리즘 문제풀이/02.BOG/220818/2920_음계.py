from re import L
import sys
sys.stdin = open("input.txt")

ascending = [1, 2, 3, 4, 5, 6, 7, 8]

m = list(map(int, input().split()))

if m == ascending:
    print('ascending')
elif m == sorted(ascending, reverse = True):
    print('descending')
else:
    print('mixed')


            
