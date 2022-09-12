# 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.

# (시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)


# [제약 사항]

# 시는 1 이상 12 이하의 정수이다. 분은 0 이상 59 이하의 정수이다.

# 3 
# 3 17 1 39
# 8 22 5 10
# 6 53 2 12  

T = int(input())
for tc in range(1, T + 1):
    hour_1, minute_1, hour_2, minute_2 = map(int, input().split())

    hour = hour_1 + hour_2
    minute = minute_1 + minute_2

    if hour >= 12:
        hour -= 12
    else:
        hour
    
    if minute > 59:
        hour += 1
        minute -= 60

print(f'#{tc} {hour} {minute}')
        
        
