# [GSAP] CSS 애니메이션의 한계를 넘어: 웹 인터랙션의 표준

## 1. Intro
CSS의 `transition`과 `animation`만으로도 웬만한 효과는 낼 수 있다.
하지만 스크롤에 따라 움직이거나, 여러 요소가 순차적으로 재생되는 복잡한 **시퀀스(Sequence) 애니메이션**을 구현하기엔 한계가 명확하다.
현재 웹 인터랙션의 표준이라 불리는 **GSAP(GreenSock Animation Platform)**의 핵심 개념과 리액트 환경에서의 사용법을 정리한다.

## 2. 기본 메서드: to() vs from()

GSAP의 가장 기초적인 메서드 3가지다. 이 차이만 알아도 80%는 먹고 들어간다.

### 1) `gsap.to()` : ~로 간다 (Current -> End)
현재 상태에서 설정한 값으로 변화한다. 가장 직관적이다.
```javascript
// 박스가 현재 위치에서 오른쪽으로 100px 이동
gsap.to(".box", { x: 100, duration: 1 });
```



### 2) `gsap.from()` : ~에서 온다 (Start -> Current)

설정한 값에서 시작해 원래 상태로 돌아온다. **등장 애니메이션**에 가장 많이 쓰인다.

```javascript
// 투명하고(0) 아래(100px)에 있던 요소가 제자리로 스르륵 올라옴
gsap.from(".hero-text", { 
  opacity: 0, 
  y: 100, 
  duration: 1 
});
```



### 3) `gsap.fromTo()` : ~에서 ~로 (Start -> End)

시작과 끝을 모두 내가 지정한다. 초기 상태를 확실하게 제어해야 할 때 쓴다.

```javascript
gsap.fromTo(".circle", 
  { opacity: 0, x: -100 }, // 시작 상태
  { opacity: 1, x: 0, duration: 1 } // 끝 상태
);
```



## 3. 타임라인(Timeline): 순차적 실행의 마법

`setTimeout`이나 `delay` 계산 없이, 애니메이션을 기차처럼 연결할 수 있다. 스토리텔링형 웹사이트의 핵심이다.

```javascript
const tl = gsap.timeline();

tl.to(".box1", { x: 100, duration: 1 }) // 1. 박스1 이동
  .to(".box2", { y: 50, duration: 0.5 }) // 2. 끝나면 박스2 이동
  .to(".box3", { rotation: 360 }); // 3. 끝나면 박스3 회전
```



## 4. ScrollTrigger: 스크롤이 트리거가 된다

"스크롤을 내리면 애니메이션이 실행된다"는 로직을 아주 쉽게 구현해준다.

```javascript
gsap.to(".section-2", {
  scrollTrigger: {
    trigger: ".section-2", // 감시할 요소
    start: "top 80%", // 요소의 top이 뷰포트 80% 지점에 닿을 때 시작
    end: "bottom 20%",
    toggleActions: "play none none reverse", // 들어올 때 재생, 나갈 때 역재생
    // markers: true, // 개발 가이드선 표시 (디버깅용)
  },
  x: 500,
});
```



## 5. React 환경에서의 사용 (`useGSAP`)

리액트는 컴포넌트가 렌더링될 때마다 함수가 재실행되므로, 메모리 누수 방지(Cleanup)가 필수다.

과거엔 `useEffect` 안에서 복잡하게 처리했지만, 이제는 **`useGSAP` 훅**이 이를 자동으로 처리해준다.

JavaScript

```javascript
import { useRef } from 'react';
import gsap from 'gsap';
import { useGSAP } from '@gsap/react';

const MyComponent = () => {
  const container = useRef();

  useGSAP(() => {
    // scope를 지정하면 이 컴포넌트 내부의 '.box'만 선택됨 (클래스 충돌 방지)
    gsap.from(".box", { x: -100, opacity: 0 });
  }, { scope: container });

  return (
    <div ref={container}>
      <div className="box">Hello GSAP</div>
    </div>
  );
};
```



## 6. 결론 (Today I Learned)

단순히 요소를 움직이는 것이 아니라, **"사용자의 시선을 어떻게 유도할 것인가?"**를 고민하게 해주는 도구다.

특히 `stagger` 속성으로 리스트를 순차적으로 띄우거나, `ScrollTrigger`로 스크롤 경험을 제어하는 것은 CSS만으로는 구현하기 힘든 디테일이다.

포트폴리오 프로젝트에 적극 도입하여 동적인 사용자 경험을 만들어야겠다.