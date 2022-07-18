# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

month = int(input())
if month in (12, 1, 2):
    print('winter')
elif month in (3, 4, 5):
    print('spring')
elif month in (6, 7, 8):
    print('summer')
elif month in (9, 10, 11):
    print('fall')


# 모범 답안
#     a=int(input())
# if a//3==1:
#     print("spring")
# elif a//3==2:
#     print("summer")
# elif a//3==3:
#     print("fall")
# else:
#     print("winter")
