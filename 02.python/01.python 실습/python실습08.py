numbers = [0, 20, 100]

# 변수를 각각 지정
first = numbers[0]
second = numbers[0]
for i in numbers:
   # first 보다 큰 수 -> True로 for문 실행
   if first <= i: 
      #비교했던 값을 미리 second에 저장
      second = first 
      # 리스트에 있는 값을 하나씩 비교
      # i[1] = 20 -> 20을 first 값에 대입 fot문에서 반복 실행
      first = i 
   
print(second)
