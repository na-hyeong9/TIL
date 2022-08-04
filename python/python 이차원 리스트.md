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

   

   -  반복문으로 작성 (n X m 행렬)

     ```python
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

     

   - 컴프리헨션으로 작성

     ```python
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

     

2.  입력 받기

   - 행렬의 크기가 미리 주어지는 경우

     ```python
     # 3x3 행렬 만들기
     
     1 2 3
     4 5 6
     7 8 9
     
     matrix1=[list(map(int, input().split())) for _ in range(3)]
     
     print(matrix1)
     ```

     

3. 순회

   1. ```이중 for문```을 이용한 행 우선 순회

      ```python
      matrix = [
          [1, 2, 3, 4]
          [5, 6, 7, 8]
          [9, 0, 1, 2]
      ]
      for i in range(3):
          for j in range(4):
              print(matrix[i][j], end=' ')
          print()
      
      >>> 1 2 3 4
      >>> 5 6 7 8
      >>> 9 0 1 2
          
      ```

   2. ```이중 for문```을 이용한 열 우선 순회

      ```python
      matrix = [
          [1, 2, 3, 4]
          [5, 6, 7, 8]
          [9, 0, 1, 2]
      ]
      for i in range(4):
          for j in range(3):
              print(matrix[j][i], end=' ')
          print()
      
      >>> 1 5 9
      >>> 2 6 0
      >>> 3 7 1
      >>> 4 8 2
      ```

      📌__참고__📌 __pythonic한 방법__으로 이차원 리스트 총합 구하기

      ```python
      matrix = [
          [1, 1, 1, 1]
          [1, 1, 1, 1]
          [1, 1, 1, 1]
      ]
      
      total = sum(map(sum, matrix))
      print(total)
      ```

      

4. 전치

   > 전치(transpose)란 행렬의 행과 열을 서로 맞바꾸는 것을 의미한다.

5. 회전

   > 문제에서 이차원 리스트를 왼쪽, 오른쪽으로 90도 회전하는 경우가 존재한다.