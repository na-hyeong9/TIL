## 조건문

```python
num = -10

if num > 0:
    value = num
else vlaue = -num #선택적 직접 조회 불가

```



- 조건 표현식

```python
num = -10

if num > 0:
    value = 1️⃣num
else vlaue = 2️⃣-num

--
value = num if 1️⃣num >= 0 else 2️⃣-num #조건표현식
```



## 반복문

- while 문

  _반복이 해당하는 조건_

  ```python
  while expressin #참일 때 까지 실행
  	#참 -> 거짓
  while True : 
      print #무한히 실행
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

  - break

    ```
    반복문을 종료
    ```

  - continue

    ```
    continue 이후의 코드블록은 실행하지 않고, 다음 반복을 수행 #True일 때
    ```

  - for else

    ```
    break로 중단되었는지 여부에 따라 실행
    ```

    

    