# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

# 오류 발생
# SyntaxError: invalid syntax (<string>, line 2)
# a, b = map(int, input().split())
# if bool(a) == 'True' and bool(b) == 'True'
#     print(True)

a, b = input().split()
a= int(a)
b= int(b)
print(bool(a) and bool(b))