### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT *
FROM playlist_track  AS "A"
ORDER BY PlaylistID DESC
LIMIT 5;
```
```sql
PlaylistId  TrackId
----------  -------
18          597
17          3290
17          2096
17          2095
17          2094
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT *
FROM tracks AS "B"
ORDER BY TrackId
LIMIT 5;
``` 
```sql
TrackId  Name                                     AlbumId  MediaTypeId  GenreId  Composer                                                      Milliseconds  Bytes     UnitPrice  
-------  ---------------------------------------  -------  -----------  -------  ------------------------------------------------------------  ------------  --------  ---------  
1        For Those About To Rock (We Salute You)  1        1            1        Angus Young, Malcolm Young, Brian Johnson                     343719        11170334  0.99       

2        Balls to the Wall                        2        2            1                                                                      342562        5510424   0.99       

3        Fast As a Shark                          3        2            1        F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman           230619        3990994   0.99       

4        Restless and Wild                        3        2            1        F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider &   252051        4331779   0.99       
                                                                                 W. Hoffman

5        Princess of the Dawn                     3        2            1        Deaffy & R.A. Smith-Diesel                                    375418        6290521   0.99       
``` 
### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT PlaylistId, Name 
FROM playlist_track A 
INNER JOIN tracks B ON A.TrackId = B.TrackId
ORDER BY PlaylistId DESC
LIMIT 10;
```  

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT PlaylistId , Name
FROM playlist_track A
INNER JOIN tracks B ON A.TrackId  = B.TrackId
WHERE PlaylistId = 10
ORDER BY Name DESC
LIMIT 5;
```
```sql
PlaylistId  Name
----------  ------------------------
10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks A
INNER JOIN artists B ON A.Composer = B.Name;
```
```sql
COUNT(*)
--------
402
sqlite>
```
### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks A
LEFT JOIN artists B ON A.Composer = B.Name;
```
```sql
COUNT(*)
--------
3503
```
### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
INNER JOIN은 교집합, LEFT JOIN은 왼쪽 테이블을 중심으로 오른쪽의 테이블을 매치시킨다. 오른쪽 테이블에 없으면 NULL값으로 표현된다.
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId
LIMIT 5;
``` 
```sql
InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2
```
### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId
LIMIT 5;
``` 
```sql
InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23
```
### 10. 각 invoice_items에 해당하는 invoices 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.InvoiceLineId, B.InvoiceId FROM invoice_items A
INNER JOIN invoices B
ON A.InvoiceId = B.InvoiceId
ORDER BY B.InvoiceId DESC
LIMIT 5;
```
```sql
InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2226           411
2227           411
2228           411
2229           411
```

### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.InvoiceId, B.CustomerId
FROM invoices A
INNER JOIN customers B ON A.CustomerId = B.CustomerId
ORDER BY InvoiceId DESC
LIMIT 5;
```
```sql 
nvoiceId  CustomerId
---------  ----------
412        58
411        44
410        35
409        29
408        25
```
### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.InvoiceLineId, B.InvoiceId, C.CustomerId
FROM invoice_items A
INNER JOIN invoices B ON A.InvoiceId = B.InvoiceId
INNER JOIN customers C ON B.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;
```
```sql
InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        1
2240           412        3
2240           412        12
2240           412        15
2240           412        18
```
### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT C.CustomerId, COUNT(*)
FROM invoice_items A
INNER JOIN (SELECT * FROM invoices A INNER JOIN customers B ON A.CustomerId = B.CustomerId) C
ON A.InvoiceId = C.InvoiceId
GROUP BY C.CustomerId
ORDER BY C.CustomerId
LIMIT 5;
```
```sql
CustomerId  COUNT(*)
----------  --------
1           38
2           38
3           38
4           38
5           38
```
