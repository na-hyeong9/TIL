# Branch



- __작업/협업__하는 흐름 --> __branch__ 활용 (가지치기)

각자 개발을 진행하고 

_-> 각자 완료 branch 통합 

```asciiarmor
(master) $ git branch merge (exmanple)
```

이력(커밋)을 합치기 위해서는 일반적으로 _merge_ 명령어를 사용



---

### 1. 명령어

- git branch

  > 브랜치 조회

- git branch -b example

  > 브랜치 생성

- git checkout example

  > 해당 브랜치로 변경

- git branch -d <브랜치>

  > 브랜치 삭제



__(HEAD -> master)  뜻__

```master```의 가장 최근의 커밋 ```HEAD```

