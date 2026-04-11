# [Refactoring] 리액트 프로젝트 마이그레이션: JSX에서 TSX로의 전환

## 1. Intro
기존 JavaScript(JSX) 기반의 포트폴리오 프로젝트를 진행하던 중, 컴포넌트 간의 데이터 흐름이 명확하지 않고 런타임 에러의 위험이 있다는 것을 느꼈다.
특히 GSAP과 같은 외부 라이브러리를 사용할 때, DOM 요소나 속성값의 타입이 보장되지 않아 발생할 수 있는 잠재적 이슈를 해결하기 위해 **TypeScript(TSX)로의 마이그레이션**을 진행했다.



## 2. 주요 변경 사항 (Key Changes)

### 1) useRef의 타입 명시
JS에서는 `useRef()`를 비워두어도 문제가 없었지만, TS에서는 해당 Ref가 어떤 HTML 요소를 참조하는지 명확히 알려줘야 했다.

```tsx
// [Before: JS]
const aboutRef = useRef();

// [After: TS]
// section 태그를 참조하므로 HTMLElement 타입 지정, 초기값 null 설정
const aboutRef = useRef<HTMLElement>(null);
```

### 2) 데이터 인터페이스(Interface) 정의

반복되는 데이터 구조(배열)에 타입을 정의하여, 잘못된 키값이나 자료형이 들어가는 것을 원천 차단했다.

```TypeScript
// 데이터 구조 정의
interface Skill {
  name: string;
  level: string;
}

// 타입 적용
const skills: Skill[] = [
  { name: "HTML5", level: "95%" },
  // ...
];
```



## 3. 트러블 슈팅: GSAP과 TypeScript의 충돌

마이그레이션 중 가장 애를 먹었던 부분은 **GSAP 애니메이션 설정에서의 타입 에러**였다.

### 🚨 문제 상황 (Error)

GSAP의 `width` 속성을 설정하는 콜백 함수에서 에러가 발생했다.

```TypeScript
// Error: Type 'string | undefined' is not assignable to type 'string | number ...'
width: (i, target) => target.dataset.level, 
```

- **원인:** TypeScript는 `target.dataset.level` 값이 존재하지 않을 수도 있다고(`undefined`) 판단하여, 확실한 값만 요구하는 GSAP 속성에 할당을 거부했다. JS였다면 그냥 넘어가서 나중에 화면이 깨졌을 것이다.

### ✅ 해결 (Solution)

값이 없을 경우를 대비한 **폴백(Fallback) 값**을 지정하여 타입을 보장했다.

```TypeScript
// target을 HTMLElement로 단언하고, 값이 없으면 "0%"를 반환하도록 수정
width: (_: number, target: HTMLElement) => target.dataset.level || "0%",
```

- `_`: 사용하지 않는 인자(`index`)는 언더바 처리하여 'unused variable' 경고 해결.
- `|| "0%"`: 데이터가 없을 경우 기본값을 할당하는 **방어적 코딩(Defensive Coding)** 적용.



## 4. 결론 (Today I Learned)

단순히 확장자를 `.jsx`에서 `.tsx`로 바꾸는 작업이 아니었다.

그 과정에서 **"이 변수가 정말 이 시점에 값이 있는가?"**를 끊임없이 고민하게 되었고, 결과적으로 코드가 훨씬 단단해졌다.

앞으로의 프로젝트는 초기 세팅부터 TypeScript를 도입하여, 개발 단계에서부터 에러를 제어하는 환경을 구축해야겠다.