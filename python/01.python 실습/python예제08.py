# # 예제 08. [오류 해결] 모음의 개수 찾기

# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# 조건문 or 입력 오류
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or  char == "u":
        count += 1

print(count)