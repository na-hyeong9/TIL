# [Git] 협업의 정석: 브랜치 전략(Git Flow)과 충돌(Conflict) 해결

## 1. Intro
혼자 개발할 때는 `main` 브랜치 하나에서 `add`, `commit`, `push`만 해도 문제가 없었다.
하지만 여러 명이 동시에 작업하는 실무 환경에서는 서로의 코드를 덮어쓰지 않기 위한 **규칙(Strategy)**이 생명이다.
SI 프로젝트에서 형상 관리 체계를 구축하며 적용했던 **브랜치 전략**과 **충돌 해결 노하우**를 정리한다.



## 2. 브랜치 전략 (Git Flow Light)

복잡한 오리지널 Git Flow를 실무 상황(SI/퍼블리싱)에 맞게 경량화하여 사용했다.

### 1) 브랜치 구조
* **`main` (Master)**: 언제든 배포 가능한 **최종본**. (건드리지 않음)
* **`develop`**: 개발자들의 코드가 합쳐지는 **통합 브랜치**. 여기서 테스트가 이루어진다.
* **`feature/*`**: 각자 맡은 기능을 개발하는 **작업 브랜치**.
    * 예: `feature/login-ui`, `feature/main-slide`

### 2) 작업 프로세스
1. `develop`에서 내 전용 브랜치(`feature/sub-page`)를 딴다(Create).
2. 작업을 마치고 `commit`, `push` 한다.
3. `feature` -> `develop` 브랜치로 **PR(Pull Request)**을 날리거나 병합(Merge)한다.
4. 동료들과 코드가 합쳐진 `develop`이 완성된다.

```bash
# 명령어 예시
$ git checkout develop        # develop으로 이동
$ git pull origin develop     # 최신 코드 받아오기 (필수!)
$ git checkout -b feature/ui-renewal  # 작업 브랜치 생성 및 이동
```



## 3. 공포의 충돌(Conflict) 해결하기

협업 중 가장 당황스러운 순간은 `Merge` 시 발생하는 **Conflict**다.

하지만 이는 "사고"가 아니라, 같은 파일을 수정했을 때 컴퓨터가 "누구 껄 쓸지 몰라서 물어보는" 자연스러운 과정이다.

### 1) 충돌 상황 발생

```bash
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

### 2) 코드 확인 및 수정

VS Code 같은 에디터에서 충돌 파일을 열면 다음과 같이 보인다.

```HTML
<<<<<<< HEAD (현재 내 코드)
    <button class="btn-blue">로그인</button>
=======
    <button class="btn-red">Login</button>
>>>>>>> develop (들어오는 코드)
```

- **해결 방법:**
  1. `<<<<`, `====`, `>>>>` 기호를 모두 지운다.
  2. 팀원과 상의하여 둘 중 하나를 선택하거나, 두 코드를 적절히 섞는다.
  3. 저장 후 다시 커밋한다.



```Bash
$git add index.html
$ git commit -m "fix: 로그인 버튼 스타일 충돌 해결"
```



## 4. 커밋 메시지 컨벤션 (협업의 매너)

"수정", "aaa", "작업끝" 같은 메시지는 협업의 적이다.

동료가 히스토리만 보고도 내용을 알 수 있도록 **머리말(Prefix)**을 붙이는 습관을 들였다.

- **`feat:`** : 새로운 기능 추가 (예: `feat: 메인 슬라이드 마크업 추가`)
- **`fix:`** : 버그 수정 (예: `fix: GNB 메뉴 줄바꿈 현상 수정`)
- **`docs:`** : 문서 수정 (예: `docs: README.md 가이드 업데이트`)
- **`style:`** : 코드 포맷팅, 세미콜론 누락 (로직 변경 없음)
- **`refactor:`** : 코드 리팩토링 (결과물은 같으나 내부 구조 개선)



## 5. 결론 (Today I Learned)

Git은 단순한 저장소가 아니라 **'소통 도구'**다.

브랜치를 따고, 충돌을 해결하고, 메시지를 남기는 모든 과정이 결국 동료를 배려하는 행위임을 깨달았다.

앞으로도 "나중에 내가 봐도, 남이 봐도 알 수 있는" 깔끔한 히스토리를 관리하는 습관을 유지해야겠다.