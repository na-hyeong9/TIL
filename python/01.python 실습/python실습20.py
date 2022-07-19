# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

# a = list(map(int, input()))
# s = 0
# for i in a:
#     s += i
#     print(i)

a = int(input())
i = 0

while a > 0:
    i += a % 10
    a = a // 10
print(i)