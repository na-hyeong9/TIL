1	numbers = [0, 20, 100, 40]
2	max_number = numbers[0]
3	second_number = numbers[0]
4	# 혹은
5	# max_number = float("-inf")
6	# second_number = float("-inf")
7	
8	# 1. 전체 숫자를 반복
9	for n in numbers:
10	    # 만약에, n이 최대보다 크다면
11	    if max_number < n:
12	        # 최댓값이었던 것이 두 번째로 큰 수
13	        secound_number = max_number
14	        max_number = n  
15	    elif second_number < n <max_number: # 이 식이 지원 안되는 언어도 있음 !
16	    # elif second_number < n and n < max_number # 지원이 안되는 언어들은 이렇게 !
17	        second_number = n
18	print(second_number)