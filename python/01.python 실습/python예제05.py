# 예제 05. [오류 해결] 숫자의 길이 구하기

# number = 22020718
# print(len(number))

# int는 len을 출력하지 못한다.
# str으로 형변환

number = str(22020718)
print(len(number))