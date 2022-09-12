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

     

2. 입력 받기

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

   - 왼쪽으로 90도 회전하기

     ```python
     matrix =[
         [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]
     ]
     
     n = 3
     rotaed_matrix = [[0] * n for _ in range(n)]
     
     for i in range(n):
         for j in range(n):
             rotaed_matrix[j][i] = matrix[j][n-i-1]
     ```

   - 오른쪽으로 90도 회전하기

     ```python
     matrix =[
         [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]
     ]
     
     n = 3
     rotaed_matrix = [[0] * n for _ in range(n)]
     
     for i in range(n):
         for j in range(n):
             rotaed_matrix[i][j] = matrix[n-i-1][j]
     ```

   

6. 완전 탐색_verse.1 (Exhaustive Search)

   1.  무식하게 풀기 (Brute - force)

   2.  델타 탐색(Delta Search)

      > (0, 0) 에서 부터 이차원 리스트의 모든 우너소를 순회하며(완전 탐색)
      >
      > 각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동하는 방식이다.
      >
      > 이차원 리스트의 인덱스(좌표)의 조작을 통해서 상하좌우 탐색을 한다.
      >
      > 이때 행과 열의 변량인 -1, +1을 델타(delta)값이라 한다.

      ```python
      delta = [(-1, 0), (1, 0), (0, -1), (0, -1)]
      
      
      # x = 행 , y = 열
      dx = [-1, 1, 0, 0]
      dy = [0, 0, -1, 1]
      
      
      # 상 (x-1, y)
      nx = x +dx[0]
      ny = y +dy[0]
      
      # 하 (x+1, y)
      nx = x +dx[1]
      ny = y +dy[1]
      
      # 좌 (x, y-1)
      nx = x +dx[2]
      ny = y +dy[2]
      
      # 우 (x, y+1)
      nx = x +dx[3]
      ny = y +dy[3]
      
      # 상하좌우
      for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
      
      ```

   - 상하좌우로 이동 후 범위를 벗어나지 않는지 확인 및 갱신하기

     ```python
     # 델타값을 이용해 상하좌우 이동
     for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]
         
     # 범위를 벗어나지 않으면 갱신
     if 0 <= nx < 3 and 0 <=ny <3:
         x = nx
         y = ny
     ```

     

