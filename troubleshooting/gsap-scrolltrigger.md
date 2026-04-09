# [React] GSAP ScrollTrigger 다중 요소 렌더링 꼬임(겹침) 현상 해결



## 1. Intro (The Problem)

React로 구축 중인 개인 포트폴리오의 `Project History` 섹션에서, 사용자가 스크롤을 내릴 때마다 프로젝트 카드(`.project-card`)들이 순차적으로 아래에서 위로 나타나는(Fade-up) 애니메이션을 구현하고자 했다.

이를 위해 `@gsap/react`의 `useGSAP`과 `ScrollTrigger` 플러그인을 사용했는데, **첫 번째 카드를 제외한 나머지 카드들이 화면에 나타나지 않거나 특정 위치에서 겹쳐버리는 렌더링 이슈**가 발생했다.

DOM 상태를 확인해 보니, 화면 아래쪽에 있어야 할 카드들이 애니메이션 초기 상태(`opacity: 0`, `y: 50`)에서 진행되지 않고 멈춰있는 현상을 발견할 수 있었다.



## 2. 원인 분석: Trigger 시점과 위치 계산의 오류

초기 구현 당시, 전체 카드를 감싸는 부모 컨테이너(`.grid-container`)를 기준으로 애니메이션을 일괄 실행하려고 시도했었다.

**[AS-IS: 문제가 발생했던 초기 접근 방식]**

JavaScript

```
useGSAP(
  () => {
    // ❌ 문제의 원인: 부모 컨테이너 전체를 트리거로 잡고 일괄 실행 시도
    gsap.from(".project-card", {
      scrollTrigger: {
        trigger: ".grid-container", 
        start: "top 85%",
        toggleActions: "play none none reverse",
      },
      y: 100,
      opacity: 0,
      duration: 1.5,
      stagger: 0.2, // 시간차를 주면 해결될 것이라 생각함
      ease: "power3.out",
    });
  },
  { scope: projectWrapRef }
);
```



**[문제의 핵심]**

부모 컨테이너(`.grid-container`) 전체를 트리거 영역으로 설정하면, 컨테이너의 상단이 뷰포트에 닿는 순간 **내부에 포함된 모든 카드의 애니메이션 시작점과 도착점이 동시에 계산**된다.

하지만 두 번째, 세 번째 카드 등 화면 아래쪽에 위치한 요소들은 아직 뷰포트에 렌더링되지 않았거나 위치가 온전히 확정되지 않은 상태일 수 있다. 이로 인해 GSAP이 요소들의 좌표를 잘못 계산하게 되고, 결과적으로 스크롤을 내려도 애니메이션이 멈춰버리거나 카드들이 한 곳에 겹쳐서 나타나는 현상이 발생한 것이다.



## 3. 해결 과정: 개별 요소 트리거 제어 (gsap.utils.toArray)

부모 컨테이너 기준의 일괄 실행 방식에서 벗어나, **"카드 하나하나가 뷰포트에 나타날 때마다 개별적으로 위치를 계산하고 애니메이션을 실행"**하도록 로직을 수정했다.

### 핵심 로직 구현

1. `gsap.utils.toArray`를 활용해 `.project-card` 클래스를 가진 모든 요소를 배열 형태로 추출한다.
2. `forEach` 반복문을 통해 배열을 순회하며, **각 카드 요소 자체를 `ScrollTrigger`의 `trigger` 타겟으로 개별 할당**한다.

**[TO-BE: 안정화된 현재 코드]**

```TypeScript
useGSAP(
  () => {
    // ... (헤더 애니메이션 코드 생략)

    // 1. 모든 카드 요소를 배열 형태로 수집
    const cards = gsap.utils.toArray(".project-card");
    
    // 2. 각 카드마다 개별적인 ScrollTrigger 생성 및 감지
    cards.forEach((card: any) => {
      gsap.from(card, {
        scrollTrigger: {
          trigger: card, // ✅ 부모가 아닌, 각 카드가 뷰포트에 들어올 때를 개별 감지
          start: "top 90%", // 카드가 화면 아래 90% 지점에 보일 때 시작
          end: "bottom 20%",
          toggleActions: "play none none reverse",
        },
        y: 50, // 이동 거리를 100에서 50으로 줄여 렌더링 최적화
        opacity: 0,
        duration: 0.8,
        ease: "power3.out",
      });
    });
  },
  { scope: projectWrapRef }
);
```

### 💡 왜 `gsap.utils.toArray`를 사용했는가?

React 환경은 가상 DOM(Virtual DOM)을 다루기 때문에, 바닐라 JS처럼 `document.querySelectorAll`을 사용해 DOM에 직접 접근하면 컨텍스트 충돌이나 타이밍 이슈가 발생할 수 있다.

GSAP에서 제공하는 `gsap.utils.toArray`를 사용하면 선언한 `scope`(`projectWrapRef`) 내에서 안전하게 요소를 탐색하고 배열로 반환받아 안정적인 개별 제어가 가능해진다.



## 4. 추가 대응: UX를 고려한 `start` 옵션 최적화

개별 트리거 방식으로 변경한 후 카드 겹침 이슈는 해결되었으나, 기본 설정대로라면 카드가 화면에 충분히 올라와야만 애니메이션이 시작되어 다소 답답한 느낌을 줄 수 있었다.

이를 개선하기 위해 `start: "top 90%"` 옵션을 부여했다.

이 설정을 통해 **카드의 최상단(top)이 화면의 아래쪽 90% 지점(사용자 눈에 막 보이기 시작하는 위치)에 도달하면 즉각적으로 애니메이션이 시작**되도록 반응성을 높였다. 결과적으로 스크롤 시 화면이 비어 보이는 시간을 줄이고, 요소가 부드럽게 나타나는 쾌적한 사용자 경험(UX)을 구축할 수 있었다.



## 5. 결론 (Today I Learned)

리스트 형태로 나열된 다중 요소에 스크롤 애니메이션을 적용할 때, 전체를 부모 요소에 묶어서(`stagger` 등) 일괄 처리하는 것이 항상 효율적인 것은 아니라는 점을 배웠다.

동적이고 레이아웃 변화가 있는 리스트일수록, **요소별로 각각 트리거를 걸어 독립적으로 좌표를 계산하게 만드는 방어적(Defensive) 코딩**이 예상치 못한 렌더링 이슈를 막는 가장 안전하고 확실한 방법임을 경험했다. React의 렌더링 방식과 GSAP의 라이프사이클을 함께 고민해 볼 수 있는 유의미한 트러블슈팅이었다.