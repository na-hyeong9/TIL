# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
# 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)

# ** 비트단위(bitwise) 연산자는,
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)
# 가 있다.

# 예를 들어 1이 입력되었을 때 저장되는 1을 32비트 2진수로 표현하면
#         00000000 00000000 00000000 00000001 이고,
# ~1은 11111111 11111111 11111111 11111110 가 되는데 이는 -2를 의미한다.

# 예시
# a = 1
# print(~a) #-2가 출력된다.

a = int(input())
print(~a)