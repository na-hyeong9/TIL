# 예제 07. [오류 해결] 평균 구하기

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# count가 for문 밖에 선언되어 있다.
# 줄 맞춤으로 for문 안에서 반복 가능하게 수정
# total과 count 사이에 //로 몫만 출력
# / 하나로 수정
# float 삽입 실수형으로 형변형

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(float(total / count))