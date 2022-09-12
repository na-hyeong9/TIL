# 예제 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기

# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# 튜플은 appned 함수 사용 불가
# list로 변형
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)