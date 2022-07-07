# GIT

----

#### GIT 이란?

분산 버전 관리 시스템



## 1. 기본 명령어

- git init

  > 로컬 저장소 생성



- git add <file>

  >  특정 파일/ 폴더의 변경 사항 추가



- git commit-m <커밋메시지>

  > 커밋 (버전 기록)

  

- git log

  > 버전 확인

​		```log -1 '이전 커밋으로 돌아가라'```

- rm -rf <파일명>

  > 파일 삭제하기

  

- git status

  > 상태 확인

  
  
  ---
  
  ### ☑ 기본 흐름

| Working Directory | Staging Area                                | Repositorty                |
| ----------------- | ------------------------------------------- | -------------------------- |
| 파일의 변경사항   | 버전으로 기록하기 위한 파일 변경사항의 목록 | 커밋(버전)들이 기록되는 곳 |

​	*b.txt가 실제로 staging area(임시공간)에 옮겨진 것이 아님*

​	*end가 나왔을 때 q (quit*)

> 커밋 주의 사항
>
> 의미있는 저장 ```(sw->반드시 작동 가능한 상태)```



## 2. 원격저장소 기본 명령어



- git clone <url>

  > 원격 저장소 복제

  

- git remote add <원격 저장소 이름> <url>

  > 원격 저장소 추가 (일반적으로 origin)

  

- git remote -v

  > 원격 저장소 정보 확인

  

- git remote rm <원격 저장소>

  > 원격 저장소 삭제

  

- git push <원격저장소> <브랜치>

  > 원격 저장소에 로컬 저장소에 있는 data를 저장

  

- git pull <원격 저장소> <브랜치>

  > 로컬 저장소에 원격 저장소에 있는 data를 저장

  

###   ☑ 기본흐름



![depositphotos_196587212-stock-illustration-software-upload-user-data-cloud](C:\Users\HOME\Downloads\depositphotos_196587212-stock-illustration-software-upload-user-data-cloud.jpg)



> **원격 저장소**와 __로컬저장소__의 공유가 가능하다.
>
> ```git push``` 로컬 저장소 >>> 원격 저장소
>
> ```git pull``` 원격 저장소 >>> 로컬 저장소

