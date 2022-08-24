import sys
sys.stdin = open ("input.txt")


t = input()

left, right = t.split("(")
print(left.count("@"), right.count("@"), end=" ")








