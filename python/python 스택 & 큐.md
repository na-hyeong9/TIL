# 스택 & 큐

1. 스택 (Stack)

   > Stack은 쌓는다는 의미로써, 마치 접시를 쌓고 빼듯이 데이터를 한쪽에서만 넣고 빼는 자료구조
   >
   > 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 LIFO(Last -in Firs-out,후입선출) 방식

   ```가장 맨 뒤에 데이터를 넣는 행위 ->append```

   ```가장 최신의 데이터를 빼는 행위 -> pop```

   ``` 왜 스택을 써야할까(Why)?```

   > 데이터가 반대로 정렬되어야 할 때

   - 뒤집기, 되돌리기, 되돌아가기

     ``` ctrl + z ``` 

   - 마무리 되지 않은 일을 임시 저장

     ```괄호매칭``` ```함수 호출``` ```백트래킹``` ```DFS(깊이 우선 탐색)```

     

2. 큐

   > Queue는 한 쪽 끝에서 데이터를 넣고, 다른 한쪽에서만 데이터를 뺄 수 있는 자료구소
   >
   > 가장 먼저들어온 데이터가 가장 먼저 나가는 선입 선출 구조 (FIFO : First - in First - out)

   ```큐의 맨 뒤에 데이터를 넣는 행위 -> enqueue```

   ```큐의 가장 오래된(맨 앞) 데이터를 빼는 행위 -> dequeue```

   ``` python
   from collections import deque
   
   numbers = [1, 2, 3, 4, 5]
   
   deque(numbers) #seq, iterable
   
   queue.append(6)
   queue.popleft()
   
   print(queue)
   
   
   #[2,3,4,5,6]
   ```

   