# 이차원 리스트

1. 이차원리스트

   > 이차원 리스트는 리스트를 원소로 가지는 리스트일 뿐이다.
   >
   > 이차원 리스트는 행렬(matrix이다.)

   ```python
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   
   
   matrix = [
      0 [1, 2, 3] # 00 01 02
      1 [4, 5, 6] # 10 11 12
      2 [7, 8, 9] # 20 21 22
   ]	  0  1  2	
   
   print(matrix[0][0])
   >>> 1
   ```

2.  반복문으로 작성 (n X m 행렬)

   ``` python
   n = 4 # 행
   m = 3 # 열
   # n x m
   # n : 행의 개수
   # m : 열의 개수
   matrix = []
   
   for _ in range(n):
       matrix.append([0]*m)
       
   print(matrix)
   >>>[[0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0]]
   ```

3.  컴프리헨션으로 작성

   ```pyrthon
   n = 4 # 행
   m = 3 # 열
   matrix = [앞, 조건]
   matrix = [[0] * m for _ in range(n)]
   
       
   print(matrix)
   >>>[[0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0]]
   ```

   

   📌__주의__📌 ```리스트 컴프리헨션 ```vs ```리스트 곱셈 연산```

   ```python
   n = 2
   m = 2
   
   matrix1 = [[0] * m for _ in range(n)]
   
   matrix[0][0] = 1
   
   print(matrix)
   >>>[[1, 0][0, 0]]
   
   
   matrix2 = [[0] * m] * n
   matrix2[0][0] = 1
   
   print(matrix2)
   >>>[[1, 0][1, 0]]
   ```

   