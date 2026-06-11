# [TypeScript] - 2 - 제네릭(Generic), 타입도 인자처럼 넘길 수 있다

> 2026.06.11

---

## 지난 편에서

`type`과 `interface`의 차이를 정리하면서, 타입을 어떻게 정의하느냐에 따라 코드의 표현력이 달라진다는 걸 알게 됐다.

이번엔 그보다 한 단계 더 나아간 개념이다. **제네릭(Generic)** — 타입 자체를 변수처럼 다루는 것.

---

## 문제부터 보자

숫자 배열에서 첫 번째 요소를 반환하는 함수가 있다고 치자.

```ts
function first(arr: number[]): number {
  return arr[0];
}
```

잘 동작한다. 근데 문자열 배열에도 쓰고 싶어졌다. 어쩔 수 없이 복붙한다.

```ts
function firstString(arr: string[]): string {
  return arr[0];
}
```

이걸 반복하면 타입만 다르고 똑같은 함수가 계속 생긴다. `any`로 퉁치면 타입 안전성이 날아간다.

```ts
function first(arr: any[]): any {
  return arr[0];
}
```

이건 그냥 JS다. TS를 쓰는 의미가 없어진다.

---

## 제네릭이 이걸 해결한다

제네릭은 함수를 선언할 때 타입을 고정하지 않고, **호출할 때 타입을 넘겨받는** 방식이다.

```ts
function first<T>(arr: T[]): T {
  return arr[0];
}

first([1, 2, 3]);       // T = number로 추론됨, 반환 타입도 number
first(['a', 'b', 'c']); // T = string으로 추론됨, 반환 타입도 string
```

`<T>`는 타입 매개변수다. 함수 인자가 값을 받듯, 타입 인자는 타입을 받는다. 호출 시점에 TS가 넘긴 배열을 보고 `T`가 뭔지 알아서 추론해준다.

명시적으로 넘길 수도 있다.

```ts
first<number>([1, 2, 3]);
```

---

## 인터페이스에도 쓸 수 있다

API 응답 구조는 엔드포인트마다 다르지만 형태는 비슷한 경우가 많다.

```ts
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

// 사용자 정보를 담은 응답
type UserResponse = ApiResponse<User>;

// 게시글 목록을 담은 응답
type PostListResponse = ApiResponse<Post[]>;
```

`T` 자리에 원하는 타입을 끼워 넣으면 된다. 응답 구조 자체는 재사용하면서, 안에 담기는 데이터 타입만 바꿀 수 있다.

---

## 제약을 걸 수도 있다

`T`가 아무 타입이나 받아도 된다면 상관없지만, 특정 프로퍼티가 있어야 한다면 `extends`로 제약을 건다.

```ts
function getLength<T extends { length: number }>(value: T): number {
  return value.length;
}

getLength('hello');     // string은 length가 있다
getLength([1, 2, 3]);   // array도 length가 있다
getLength(42);          // 에러! number에는 length가 없다
```

`T extends { length: number }`는 "length 프로퍼티가 있는 타입만 받겠다"는 뜻이다. 무제한 유연성을 주되, 필요한 조건은 강제할 수 있다.

---

## React에서는 이렇게 쓰인다

`useState`의 타입 정의가 바로 제네릭이다.

```ts
const [count, setCount] = useState<number>(0);
const [user, setUser] = useState<User | null>(null);
```

상태에 담길 타입을 명시하면, `setCount`에 문자열을 넣으려 할 때 TS가 바로 잡아준다. 제네릭 덕분에 `useState` 하나로 어떤 타입의 상태든 다룰 수 있는 것이다.

---

## 오늘 얻은 것

제네릭은 처음에 `<T>` 문법이 낯설어서 미뤄뒀는데, 핵심은 단순하다. **타입을 나중에 결정하겠다는 약속이다.**

함수나 컴포넌트를 여러 타입에 재사용하고 싶을 때, `any` 없이 타입 안전성을 지키고 싶을 때, 제네릭이 답이다. `useState`, `Array`, `Promise` 같은 내장 타입도 전부 제네릭으로 만들어져 있다는 걸 알고 나니까 TS 표준 라이브러리가 다르게 읽히기 시작했다.
