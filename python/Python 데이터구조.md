# 데이터 구조



__시작하기 앞서 정리__

```python

# 타입.메서드()
# 누가.output(input)
input(). split()

=======================================

# 리스트 메서드 사용
a= [10, 1, 100]
new_a = a.sort()
print(a, new_a)

# [10, 1, 100] none

#리스트에 sorted 함수를 활용
b= [10, 1, 100]
new_b = sorted(b)
print(b, new_b)

# [10, 1, 100] [1, 10, 100]
# sorted 함수를 활용하면, 원본을 변경하지 않음
# return되는 것은 정렬된 리스트

# 실제 활용 코드
a= [10, 1, 100]
a.sort()

b= [10, 1, 100]
b = sorted(b)
```





## 시퀀스

> 순서가 있는 데이터 구조



### 문자열(string) 

변경 불가능

- 문자열 탐색/검증

  - .fine(x)

    > x 위치를 반환, 없으면 '-1'을 반환함

  - .index(x)

    >  x 위치를 반환, 없으면  오류 발생

    

- 문자열 관련 검증 메소드

  ```python
  'abc'. isalpha
  # True
  
  추가 필요 (수정중)
  ```

  

- 문자열 변경

  - .replace(old, new, [count])

    > 바꿀 대상 글자를 새로운 글자로 변경

  - .strip([chars])

    > 특정한 문자들을 지정하면 양쪽(strip),왼쪽(lstrip),오른쪽을 제거(rstrip)문자열을 지정하지 않으면 공백을 제거

  - .split(sep=None, maxsplit=-1)

    > 문자열을 특정한 단위로 나눠 리스트로 반환

  - 'separator'.join([iterable])

    > 반복가능한(interable  : 문자, 튜플, ??) 컨테이너 요소들을 구분자(separator)로 합쳐 문자열을 반환

    ```python
    names = ','.join(['홍길동','김철수'])
    print(names)
    
    #홍길동,김철수
    
    numbers = ','.join([1, 2, 3])
    print(names)
    # 오류
    # why? 문자열이 아니라 숫자라서 오류 발생
    # join(map(int, [1, 2, 3])) 으로 표현
    ```

    

  

### 리스트(list)

> 변경 가능

- 값 추가 및 삭제

  - .append(x)

  - .extend(iterable)

    > 리스트에 interable의 항목을 추가함

    ```python
    
    a = ['apple']
    a.extend('banana','mango')
    print(a)
    
    # 문자를 하나씩
    a.extend('banana')
    print(a)
    ```

    

  - .insert(i, x)

    >정해진 위치 i에 값(x)를 삽입

  - remove(x)

    >  리스트에서 값이 x인 것 삭제

  - pop(i)

    > 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함

  - .clear()

    > 모든 항목을 삭제

    

- 탐색 및 정렬

  - count(x)

    > 원하는 값의 개수를 반환함
    >
    > 리스트를 순회(for)

  - sort()

    > 원본 리스트를 정렬함  None 반환
    >
    > sorted와 비교

  - .reverse()

    > 순서를 반대로 뒤집음

  

  ---

  

  ```python
  # 리스트는 mutable
  a = [1, 2, 3]
  a[0] = 100
  print(a)
  
  #문자열은 immutable
  a = ['hi']
  a[0] = 'c'
  print(a)
  ```

  

## 컬렉션

세트(set)

### 딕셔너리(dictinary)

> 키 - 값 으로 접근 index 개념이 없음

- 조회

  - .get(key[,default])

    > key를 통해 value를 가져옴
    >
    > KeyError가 발생하지 않으며, default 값을 설정할 수 있음 (기본 : None)

- 추가 및 삭제

  - .pop(key[,default])

    > key가 딕셔너리에 있으면 제거하고 해당 값을 반환

  - .update([other])

    > 값을 제공하는 key, value로 덮어씀

    

---



```python
my_dict = {'apple' : '사과', 'banana' : '바나나'}

for word in my_dict:
    # 키 반환
    print(word)
    # 키 값 반환
    print(word, my_dict[word])
 
print(my_dict['apple']) #사과 (apple의 값인 사과 출력)
# word에 키 값이 순차적으로 입력되므로 위와 같이 값인 사과 출력 
print(my_dict[word])

```

