# 딕셔너리

1. 해시테이블

   >Non - sequence & Key-Value (_Key는 immutable_)

   해시 함수 : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수

   해시: 해시 함수를 통해 얻어진 값 

   딕셔너리는 __Key__ 값을 이용해서 index와 같이 __Value__ 값을 찾아냄

   -> ```시간 복잡도 O(n)```

   

   - 딕셔너리는 언제 사용해야할까?

   > - 리스트를 사용하기 힘든 경우
   > - 데이터에 대한 빠른 접근 탐색이 필요한 경우
   > - 현실 세계의 대부분의 데이터를 다룰 경우

   

2. 딕셔너리 기본 문법

   - 기본적인 딕셔너리 사용법 (선언)

   - 기복적인 딕셔너리 사용범 (삽입/수정)

     ```python
     딕셔너리 [Key] = value
     
     # Counting
     scores = ["A", "A", "B", "C", "D", "A", "B"]
     
     # 키 자체가 데이터가 될 수 있다.
     counter = {
         "A": 0,
         "B": 0,
         "C": 0,
         "D": 0
     }
     
     for score in scores:
         counter[score] += 1
         
     print(counter)
     
     ========================================
     
     from collections import Counter
     easy_counter = Counter(scores)
     
     print(easy_counter)
     ```

     

   

   - 기본적인 딕셔너리 사용법 (삭제)

     - 딕셔너리.pop(key)

       > 내부에 존재하는 key에 대한 삭제 및 반환, 본재하지 않는 key에 대해서는 KeyEroor 발생

       ```python
       nana = {
           "name" : "nana"
           "role" : "ceo"
       }
       
       role = nana.pop("age") 
       
       print(role)
       
       # KeyError
       ```

     - 딕셔너리.pop(key, default)

       ```python
       nana = {
           "name" : "nana"
           "role" : "ceo"
       }
       
       role = nana.pop("age")
       
       print(role)
       ```

       

   - 기본적인 딕셔너리 사용법 (조회)

     - 딕셔너리.get(key, default)

     - 딕셔너리[key]

       ```python
       nana = {
           "name" : "nana"
           "role" : "ceo"
       }
       
       age = nana.get("age",25) # age가 없으면 25로 반환
       
       print(age)
       
       # None
       ```

       

3. 딕셔너리 메서드

   - .key()

     > keyㅇ

     ```python
     nana = {
         "name" : "nana"
         "role" : "ceo"
     }
     
     for elem in nana:
         print(elem) # name, role
         print(nana[elem]) # nana, ceo
     ```

   - .values()

     ```python
     nana = {
         "name" : "nana"
         "role" : "ceo"
     }
     
     print(nana.values())
     ```

   - .iteme()

     ```python
     nana = {
         "name" : "nana"
         "role" : "ceo"
     }
     
     print(nana.items())
     
     # dick_items([('name', 'nana'),('role', 'ceo')])
     
     for (key, value) in nana.items():
         print(key, value)
         # name nana
         # role ceo
     ```

     

