# [오류 해결] 입력 받기 - 2

# words = list(map(int, input().split()))
# print(words)


# 타입 오류 int -> str 으로 형변환
words = list(map(str, input().split()))
print(words)