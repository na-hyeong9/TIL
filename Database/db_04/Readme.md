### 1. 모든 테이블의 이름을 출력하세요.
```sql
.table
```

### 2. 모든 테이블의 데이터를 확인해보세요.
| 공백은 있는지 NULL은 있는지 데이터 타입은 어떤지 등등 데이터를 직접 확인해보세요.

```sql
.schema
```




### 3. 앨범(albums) 테이블의 데이터를 출력하세요.
| 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.

```sql
SELECT *
FROM albums
ORDER BY Title DESC
LIMIT 5
;
```

```sql
AlbumId  Title                         ArtistId
-------  ----------------------------  --------
208      [1997] Black Light Syndrome   136
240      Zooropa                       150
267      Worlds                        202
334      Weill: The Seven Deadly Sins  264
8        Warner 25 Anos                6
```



### 4. 고객(customers) 테이블의 행 개수를 출력하세요.

| 단, 컬럼명을 `고객 수`로 출력하세요.

```sql
SELECT COUNT(*) AS '고객 수' FROM customers;
```

```sql
고객 수
-----
59
sqlite>
```

### 5. 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력하세요.

| 단, 각각의 컬럼명을 `이름`, `성`으로 출력하고, `이름`을 기준으로 내림차순으로 5개까지 출력하세요.

```sql
SELECT FirstName, LastName  FROM customers WHERE Country = 'USA';
```

```sql
FirstName  LastName
---------  ----------
Frank      Harris
Jack       Smith
Michelle   Brooks
Tim        Goyer
Dan        Miller
Kathy      Chase
Heather    Leacock
John       Gordon
Frank      Ralston
Victor     Stevens
Richard    Cunningham
Patrick    Gray
Julia      Barnett
```



### 6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.

| 단, 컬렴명을 `송장수`로 출력하세요.
```sql
SELECT COUNT(*) FROM invoices WHERE BillingPostalCode IS NOT NULL;
```

```sql
COUNT(*)
--------
384
```



### 7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.

| 단, `InvoiceDate`를 기준으로 내림차순으로 5개까지 출력하세요.
```sql
SELECT COUNT(*) FROM invoices WHERE BillingPostalCode IS NULL ORDER BY InvoiceDate DESC LIMIT 5;
```

```sql
COUNT(*)
--------
28
```



### 8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.

| `strftime`를 검색해서 활용해보세요.

```sql
select count(*) from invoices where strftime('%Y',InvoiceDate) = '2013';
```

```sql
count(*)
--------
80
```

### 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.

| 단, 각각의 컬럼명을 `고객ID`, `이름`,`성`으로 출력하고, `고객ID`을 기준으로 오름차순으로 출력하세요.

```sql
SELECT CustomerId, FirstName, LastName FROM customers WHERE FirstName LIKE 'L%';
```

```sql
CustomerId  FirstName  LastName
----------  ---------  ---------
1           Luis       Goncalves
2           Leonie     Kohler
45          Ladislav   Kovacs
47          Lucas      Mancini
57          Luis       Rojas
```

### 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.
| 단, 각각의 컬렴명을 `고객 수`,`나라`로 출력하고, 고객 수 상위 5개의 나라만 출력하세요.
```sql
SELECT Country AS '나라', COUNT(*) AS '고객 수' FROM customers GROUP BY Country 
ORDER BY COUNT(country) DESC LIMIT 5;
```

```sql
나라       고객 수
-------  ----
USA      13
Canada   8
France   5
Brazil   5
Germany  4
```



### 11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.

```sql
SELECT ArtistID, COUNT(*) FROM albums GROUP BY ArtistID ORDER BY COUNT(*) DESC LIMIT 1;
```

```sql
ArtistId  COUNT(*)
--------  --------
90        21
```

### 12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요

| 단, 앨범 수를 기준으로 내림차순으로 출력하세요.
```sql 
SELECT ArtistID, COUNT(*) FROM albums GROUP BY ArtistID HAVING COUNT(*) >= 10;
```

```sql
ArtistId  COUNT(*)
--------  --------
22        14
50        10
58        11
90        21
150       10
```

### 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.

| 단, `고객 수`, `Country` 순서 기준으로 내림차순으로 5개까지 출력하세요.

```sql 
SELECT COUNT(*) AS '고객 수', Country, State FROM customers WHERE State NOT NULL GROUP BY Country, State ORDER BY COUNT(*) DESC, Country DESC LIMIT 5;
```

```sql
고객 수  Country  State
----  -------  -----
3     USA      CA
3     Brazil   SP
2     Canada   ON
1     USA      WI
1     USA      WA
```

### 14.  고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.

| 단, `CustomerId`와 `Fax 유/무` 컬럼만 출력하고, `CustomerId` 기준으로 오름차순으로 5개까지 출력하세요. 
```sql 
SELECT CustomerID, CASE WHEN Fax IS NULL THEN 'X' ELSE 'O' END AS 'Fax 유/무' FROM customers ORDER BY CustomerID LIMIT 5;
```

```sql
CustomerId  Fax 유/무
----------  -------
1           O
2           X
3           X
4           X
5           O
4           X                                         '
5           O  
```

### 15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.

| 단, 점원의 `LastName`, `FirstName`, `나이` 컬럼만 출력하고, `EmployeeId`를 기준으로 오름차순으로 출력하세요.

| cast(), strftime(), 오늘 날짜를 구하는 함수를 검색하고, 활용해보세요.

```sql 
SELECT LastName, FirstName, CAST(STRFTIME('%Y', 'now') AS INT) -  CAST(STRFTIME('%Y', BirthDate) AS INT) + 1 AS '나이' FROM employees ORDER BY EmployeeID;
```

### 16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.
| artists 테이블과 albums 테이블의 `ArtistId` 활용하세요.

```sql
SELECT Name FROM artists WHERE ArtistID = (SELECT ArtistID FROM albums 
GROUP BY ArtistID ORDER BY COUNT(ArtistID) DESC LIMIT 1);
```

```sql 
Name
-----------
Iron Maiden
```

### 17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.
| genres 테이블과 tracks 테이블의 `GenreId` 활용하세요.
```sql 
SELECT Name FROM genres WHERE GenreID = (SELECT GenreID FROM tracks GROUP BY GenreID ORDER BY COUNT(GenreID) ASC LIMIT 1);
```

```sql
Name
-----
Opera
```

### 자유롭게 문제를 만들어 보시고, 디스코드 채널에 공유해보세요!
