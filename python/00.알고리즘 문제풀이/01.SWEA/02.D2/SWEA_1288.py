# 민석이는 불면증에 걸렸다. 그래서 잠이 안 올 때의 민간요법 중 하나인 양 세기를 하려고 한다.

# 민석이는 1번 양부터 순서대로 세는 것이 재미없을 것 같아서 N의 배수 번호인 양을 세기로 하였다.

# 즉, 첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다.

# 이렇게 숫자를 세던 민석이에게 잠은 더 오지 않고 다음과 같은 궁금증이 생겼다.

# 이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?

# 예를 들어 N = 1295이라고 하자.

# 첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9이다.

# 두 번째로 2N = 2590번 양을 센다. 현재 본 숫자는 0, 2, 5, 9이다.

# 현재까지 본 숫자는 0, 1, 2, 5, 9이다.

# 세 번째로 3N = 3885번 양을 센다. 현재 본 숫자는 3, 5, 8이다.

# 현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.

# 네 번째로 4N = 5180번 양을 센다. 현재 본 숫자는 0, 1, 5, 8이다.

# 현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.

# 다섯 번째로 5N = 6475번 양을 센다. 현재 본 숫자는 4, 5, 6, 7이다.

# 현재까지 본 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9이다.

# 5N번 양을 세면 0에서 9까지 모든 숫자를 보게 되므로 민석이는 양 세기를 멈춘다.


# 강사님 풀이 과정

# T = int(input())
# for test_case in range(1, T + 1):
#     # Input 가져오기 (첫번째 값 -> 1)
#     N = int(input())
#     N1 = N
#     # Set에 계속 추가 예정
#     numbers = set()
#     # while 반복 => set 길이가 10이 될 때까지
#     while True:
#         # for 반복 : 숫자를 문자로
#         for n in str(N):
#         # numbers set에 추가 
#             numbers.add(n)
#         if len(numbers) == 10:
#             break
#         # print(n, numbers)
#         N += N1
#     print(f'#{test_case} {N}')


import sys
sys.stdin = open("1288_input.txt", "r")


T = int(input()) 
for tc in range(1, T + 1):

    N = int(input()) # 숫자로 input
    number = set() # 중복값 없는 튜플
    cnt = 1
    while True: #  조건식이 false가 될때 까지 무한 실행

         # 숫자를 문자로 형 변환 len을 통하여 '0'부터 '9'까지의 문자 길이를 반환
         # 형변환 하는 이유
         # len(2) # TypeError: object of type 'int' has no len()
         # len(2.4) # TypeError: object of type 'float' has no len()
         # 정수나 실수는 len()을 지원하지 않음
        for num in list(str(N)): 
            number.add(num)
        # 문자열의 길이가 10이면
        if len(number) == 10:
            # 멈춤
            break
        # 곱한 값을 cnt += 실행 되기 전에 값으로 나누어 기존 N의 값으로 전환    
        N //= cnt
        cnt += 1
        # 곧 1* 2* 3*로 보이는 곱은 기존 N을 더한다고 볼 수 있다.
        N *= cnt
   
        print(f'#{tc} {cnt}')
                
                
                
                    
