<h1>JS - 클로저(Closure) — 함수가 스코프를 기억하는 방법 - 6</h1>

> 2026.05.25

---

지난 편에서 **렉시컬 스코프**를 정리하면서 이런 말을 남겼다.

> "함수가 정의될 때 스코프를 '기억'하고 있는 게 클로저다."

오늘은 그 클로저가 정확히 무엇인지, 실제로 어디서 쓰이는지를 흐름으로 정리한다.

---

## 클로저란

**클로저(Closure)** 는 함수가 정의된 시점의 렉시컬 환경을 기억하는 함수다. 쉽게 말하면, 함수가 자신이 태어난 곳의 변수들을 기억하고 — 외부에서 호출되더라도 — 그 변수에 접근할 수 있는 특성이다.

```js
function outer() {
  const name = "김나형";

  function inner() {
    console.log(name); // outer의 변수를 기억함
  }

  return inner;
}

const greet = outer(); // outer 실행 끝
greet(); // "김나형" — 근데 name에 접근된다!
```

`outer`는 실행이 끝났는데도 `inner`가 `name`을 여전히 알고 있다. 이게 클로저다.

보통이라면 `outer`가 끝나면 `name`이 메모리에서 사라져야 하는데, `inner`가 `name`을 참조하고 있기 때문에 GC(Garbage Collector)가 수거하지 못하고 살아있는 것이다.

---

## 실제로 어디에 쓰이나

### 1. 상태 은닉 + 카운터

```js
function makeCounter() {
  let count = 0;

  return {
    increment() { count++; },
    decrement() { count--; },
    getCount()  { return count; },
  };
}

const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.getCount()); // 2
console.log(counter.count);      // undefined — 외부에서 직접 접근 불가!
```

`count`는 `makeCounter` 내부에만 있는데, 반환된 메서드들이 클로저로 `count`를 계속 참조한다. 외부에서 직접 건드릴 수 없고 정해진 메서드로만 상태를 바꿀 수 있다. 이게 **캡슐화**다.

### 2. 루프에서의 변수 캡처 문제

```js
// 문제 상황
for (var i = 0; i < 3; i++) {
  setTimeout(function () {
    console.log(i); // 3, 3, 3 — 의도한 건 0, 1, 2인데!
  }, 0);
}
```

`var`는 함수 스코프라서 루프가 끝난 시점의 `i` 값(3)을 세 번 출력해버린다.

```js
// let으로 해결
for (let i = 0; i < 3; i++) {
  setTimeout(function () {
    console.log(i); // 0, 1, 2
  }, 0);
}
```

`let`은 블록 스코프라서 매 반복마다 새로운 `i`가 생긴다. 각 콜백이 서로 다른 `i`를 클로저로 참조하는 것. 클로저를 처음 배울 때 가장 자주 나오는 예시다.

---

## 주의할 점

클로저는 외부 변수를 기억하기 때문에 **메모리에서 해제되지 않고 남아있다.** 무분별하게 쓰면 메모리 누수로 이어질 수 있다. 더 이상 필요 없는 클로저는 참조를 끊어줘야 한다.

클로저가 중첩되면 스코프 체인이 길어져서 변수 탐색 비용이 생기기도 한다. 실무에서 대부분 문제없는 수준이지만, 깊이 중첩된 클로저는 피하는 게 맞다.

---

## React에서의 클로저

React Hooks가 클로저 기반이다.

```js
const [count, setCount] = useState(0);

useEffect(() => {
  console.log(count); // 렌더링 시점의 count를 클로저로 기억
}, []); // count가 의존성 배열에 없으면 오래된 값을 참조한다
```

`useEffect` 콜백이 클로저라서 의존성 배열을 빠뜨리면 오래된 값을 계속 참조하는 **stale closure** 문제가 생긴다. React를 쓰면서 겪는 버그 중 상당수가 클로저를 이해 못 해서 생기는 것들이다.

---

## 오늘 얻은 것

클로저는 뭔가 어렵고 거창한 개념처럼 들리는데, 결국 **렉시컬 스코프 + 함수가 외부 변수를 참조**하면 자동으로 생기는 특성이다. 특별히 만들려고 하는 게 아니라 JS의 스코프 동작 방식에서 자연스럽게 나오는 것이다.

상태를 안전하게 숨기거나, 루프에서 변수를 제대로 캡처하거나, React Hooks처럼 렌더링 시점의 값을 기억하거나 — 클로저를 이해하면 이 모든 게 "왜 이렇게 동작하지?"가 아니라 "아, 그렇구나"가 된다.

다음은 **프로토타입 체인과 상속** — JS가 클래스 없이 상속을 구현하던 방식을 파볼 예정이다.
