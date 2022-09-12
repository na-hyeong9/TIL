# [오류 해결] 입력 받기

# numbers = input().split()
# print(sum(numbers))

# 타입 오류 map을 사용하여 str -> int로 형변환
numbers = map(int, input().split())
print(sum(numbers))