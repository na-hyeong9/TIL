# Python 제어문



```
특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함.
```

## 조건문

- 기본형식

  __참/거짓__에 대한 조건식

  ```python
  num = -10
  
  if num > 0:
      value = num
  else:
      # else는 선택적 직접 조회 불가 (if 조건을 제외한 모든 값을 호출)
      vlaue = -num 
  print(value)
  
  #출력값
  -10 
  ```

  

- 복수 조건문

  ```python
  dust = 80
  
  # dust가 150보다 크면, 매우 나쁨
  if dust > 150:
      print('매우 나쁨')
  # 80보다 크면, 나쁨
  elif dust > 80:
      print('나쁨')
  # 30보다 크면, 보통
  elif dust > 30:
      print('보통')
  # 좋음
  # else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능
  # 조건문에서 else는 생략이 가능하다
  else:
      print('좋음')
      
  #출력
  보통
  ```

  

- 조건 표현식

  ```python
  num = -10
  
  if num > 0:
      value = 1️⃣num
  else vlaue = 2️⃣-num
  
  value = num if 1️⃣num >= 0 else 2️⃣-num 
  ```

  

## 반복문

- while 문

  _반복이 해당하는 조건_

  ```python
  while expressin #참일 때 까지 실행
  	#참 -> 거짓
  while True : 
      print #무한히 실행
      
      
  ex)
  # a 초깃값 0
  a = 0
  # 0 < 5 -> True a = 4까지 while문 반복
  while a < 5:
      # 0 + 1 = 0 -> a = 1
  	a += 1
  print('끝')
  ```

  

- for 문 

  _값을 받아서 쓸 변수의 이름을 정의_

  ```
  for 변수이름 in 반복가능한 아이를 처음부터 끝까지 꺼내준다.
  for문은 시퀀스(string, tuble, list, range)
  ```

  - 문자열(String)순회

  - 딕셔너리 순회

    키가 있을 때 값을 가져올 수 있지만 값만 있을 때 키를 가져올 수 없다.

- 반복문 제어

  break

  ```
  반복문을 종료
  ```

  continue

  ```
  continue 이후의 코드블록은 실행하지 않고, 다음 반복을 수행 #True일 때
  ```

  for else

  ```
  break로 중단되었는지 여부에 따라 실행
  ```

  

  