# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.

# a = int(input())
# b = bool(a)
# if b != 'False':
#     print(b)
# else:
#     print(True)

a = bool(int(input()))
print(not a)