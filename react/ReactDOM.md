# TIL | React DOM, 실제로 써보기

> 2025.04.08

---

## 계기

포트폴리오 사이트 만들면서 `createRoot` API 처음 써봤다. 예전에 `ReactDOM.render()` 방식이랑 뭐가 다른 건지 궁금해서 파고들어봤다. 겸사겸사 렌더링 방식 자체도 정리해보자.

---

## ReactDOM이 뭐하는 애인가

React는 UI를 **컴포넌트 트리**로 관리하는 라이브러리인데, 그 트리를 실제 브라우저 DOM에 붙이는 역할을 하는 게 `react-dom`이다. React 자체는 DOM을 모름. 그냥 "어떻게 생겼는지"만 알고 있음. DOM에 직접 밀어 넣는 건 `react-dom`이 한다.

---

## 기존 방식: `ReactDOM.render()`

```jsx
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

React 18 이전까지 쓰던 방식이다. 심플하고 직관적인데, **동기적으로 렌더링**이 이루어진다는 게 문제였음. 렌더링 도중 다른 작업이 끼어들 여지가 없었다.

---

## 모던 방식: `createRoot`

```jsx
import { createRoot } from 'react-dom/client';
import App from './App';

const root = createRoot(document.getElementById('root'));
root.render(<App />);
```

React 18부터 공식 방식이 됐다. 핵심 차이는 **Concurrent Mode 지원**이다.

### Concurrent Mode가 뭔데?

쉽게 말하면 렌더링을 **쪼개서 처리**할 수 있게 해준다는 거다. 급한 업데이트(예: 사용자 입력)를 먼저 처리하고, 덜 급한 업데이트(예: 데이터 패칭 후 화면 갱신)는 잠깐 미뤄둘 수 있다. 덕분에 UI가 끊기는 느낌이 줄어든다.

`useTransition`, `useDeferredValue` 같은 새 훅들이 전부 이 기반 위에서 동작한다. `createRoot` 안 쓰면 이 기능들 쓰지 못한다.

---

## 포털: `ReactDOM.createPortal()`

```jsx
import { createPortal } from 'react-dom';

function Modal({ children }) {
  return createPortal(
    <div className="modal">{children}</div>,
    document.getElementById('modal-root')
  );
}
```

모달이나 툴팁 같은 걸 만들 때 진짜 유용하다. 컴포넌트 트리 구조상으로는 안쪽에 있는데, 실제 DOM에는 `body` 바로 아래에 붙여버릴 수 있음. `z-index` 지옥에서 탈출하게 해주는 기능이다!

포트폴리오 모달 구현할 때 써봤는데 체감이 확실히 달랐음. 부모 컴포넌트의 `overflow: hidden`이나 스타일 간섭을 전혀 안 받으니까.

---

## 서버사이드 렌더링: `react-dom/server`

```jsx
import { renderToString } from 'react-dom/server';

const html = renderToString(<App />);
```

Next.js나 SSR 환경에서 쓰는 방식이다. 서버에서 HTML을 미리 만들어서 클라이언트에 내려보내는 것. SEO가 중요하거나 초기 로딩 속도가 핵심인 서비스라면 고려해볼 만하다.

근데 직접 구현하기엔 설정할 게 많음. 보통 Next.js 같은 프레임워크를 끼고 씀.

---

## 방식 비교 정리

| 방식                | 특징                           | 언제 쓰나                   |
| ------------------- | ------------------------------ | --------------------------- |
| `ReactDOM.render()` | 구식, 동기 렌더링              | 레거시 프로젝트 유지보수    |
| `createRoot`        | React 18 표준, Concurrent 지원 | 신규 프로젝트 무조건 이걸로 |
| `createPortal`      | DOM 위치 분리                  | 모달, 툴팁, 드롭다운        |
| `react-dom/server`  | 서버에서 HTML 생성             | SSR, SEO 중요한 서비스      |

---

## 오늘 후기

솔직히 예전엔 그냥 `ReactDOM.render()` 복붙하고 넘어갔는데, 이번에 `createRoot` 쓰면서 왜 바뀐 건지 이해하게 됐다. Concurrent Mode 개념 자체가 처음엔 좀 추상적으로 느껴졌는데, "급한 렌더링 먼저, 느긋한 건 나중에"라고 생각하니까 감이 조금은 잡힌다.

`createPortal`도 모달 구현할 때마다 스타일 충돌로 고생하던 게 있었는데 이게 해답이었다. 진작 알았으면 좋았을 텐데 싶다.

다음엔 Suspense랑 같이 동작하는 방식 파봐야겠다.
