# 라이브러리

### ✅itertools

```python
from itertools import *
```

- 순열 (Permutation)

  > permutation(itertable, r) : itertable에서 원소 개수가 r개인 순열 뽑기 
  >
  > 순서O 중복X

  ```python
  dataset = ['A', 'B', 'C']
  
  printList = list(permutations(dataset, 2))
  print(printList)
      
  # 결과값
  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
  ```

  - r을 지정하지 않거나 r=None으로 하면 최대 길이의 순열이 리턴

  

- 중복 순열 (Permutation with repetition)

  >product(*iterables, repeat=1) : 여러 iterable의 데카르트곱 리턴
  >
  >순서O 반복O

  ```python
  dataset = ['A', 'B', 'C']
  
  printList = list(product(dataset, repeat = 2))
  print(printList)
  
  # 결과값
  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
  
  =====================================
  
  l1 = ['A', 'B']
  l2 = ['1', '2']
  
  for i in product(l1,repeat=3): #product(l1,l1,l1,repeat=1)과 동일한 출력
  	print(i)
      
  # 결과값
  ('A', 'A', 'A')
  ('A', 'A', 'B')
  ('A', 'B', 'A')
  ('A', 'B', 'B')
  ('B', 'A', 'A')
  ('B', 'A', 'B')
  ('B', 'B', 'A')
  ('B', 'B', 'B')
  ```

  

- 조합 (Combination)

  >combinations(itertable, r) : itertable에서 원소 개수가 r개인 조합 뽑기
  >
  >순서X 반복X

  ```py
  dataset = ['A', 'B', 'C']
  
  printList = list(combinations(dataset, 2))
  print(printList)
      
  # 결과값
  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
  ```

  

- 중복 조합 (Combination with repetition)

  >combinations_with_replacement(iterable,r) : iterable에서 원소 개수가 r개인 중복 조합 뽑기
  >
  >순서X 반복O

  ```python
  dataset = ['A', 'B', 'C']
  
  printList = list(combinations_with_replacement(dataset, 2))
  print(printList)
  
  
  # 결과값
  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
  ```




### ✅math

수학 함수와 상수를 제공

```python
import math
```



- math.ceil(x)

  > x보다 크거나 같은 최소 정수를 반환하는 함수입니다.

  ```python
  import math
  
  x = 2.1
  result = math.ceil(x)
  print(result) # 출력 결과: 3
  ```

- math.pow(x, y)

  >  x의 y 제곱을 계산하여 반환하는 함수

  ```python
  import math
  
  x = 2
  y = 3
  result = math.pow(x, y)
  print(result) # 출력 결과: 8.0
  ```

  
