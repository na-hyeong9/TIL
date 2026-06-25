# [TypeScript] - 5 - 조건부 타입, 타입 세계의 if문

> 2026.06.25

---

## 지난 편에서

맵드 타입으로 `Partial`, `Readonly` 같은 유틸리티 타입의 내부를 직접 뜯어봤다. 이번엔 그와 함께 자주 등장하는 **조건부 타입(Conditional Type)**을 살펴본다. 타입 수준에서 조건 분기를 쓰는 방법이다.

---

## 기본 문법

```ts
T extends U ? X : Y
```

"T가 U에 할당 가능하면 X, 아니면 Y" — 자바스크립트의 삼항 연산자와 구조가 같다. 차이는 값이 아니라 **타입**이 결과로 나온다는 점이다.

```ts
type IsString<T> = T extends string ? true : false;

type A = IsString<string>; // true
type B = IsString<number>; // false
```

복잡해 보이지만 읽는 법만 익히면 직관적이다.

---

## 실용 예시: NonNullable

TS 내장 유틸리티 `NonNullable<T>`의 실제 구현이다.

```ts
type NonNullable<T> = T extends null | undefined ? never : T;
```

`null`이거나 `undefined`면 `never`를, 아니면 `T`를 그대로 돌려준다. `never`는 타입 집합에서 공집합과 같다 — 이 자리에 실제 값이 올 수 없다는 의미다.

```ts
type A = NonNullable<string | null>;      // string
type B = NonNullable<number | undefined>; // number
```

---

## 분산 조건부 타입

유니온 타입을 넣으면 각 멤버에 조건이 따로 적용된다.

```ts
type ToArray<T> = T extends any ? T[] : never;

type Result = ToArray<string | number>;
// string[] | number[]
```

`string | number` 전체에 조건을 건 게 아니라, `string`과 `number` 각각에 적용한 결과가 합쳐진다. 이를 **분산(Distribution)**이라고 한다.

분산을 막고 싶으면 튜플로 감싸면 된다.

```ts
type ToArrayNoDistribute<T> = [T] extends [any] ? T[] : never;

type Result = ToArrayNoDistribute<string | number>;
// (string | number)[]
```

---

## infer — 타입을 추론해서 꺼내기

조건부 타입에서 가장 강력한 기능이다. `extends` 절 안에서 타입의 일부를 변수로 캡처할 수 있다.

```ts
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

function greet(): string {
  return 'hello';
}

type Result = ReturnType<typeof greet>; // string
```

`infer R`이 함수의 반환 타입을 잡아낸다. 이게 TS 내장 `ReturnType<T>`의 실제 구현이다. 직접 쓸 일은 많지 않지만, 라이브러리 타입 정의를 읽다 보면 자주 마주친다.

---

## 오늘 얻은 것

조건부 타입은 타입 수준의 `if`다. `T extends U ? X : Y` 문법 하나로 런타임 로직 없이 타입을 분기할 수 있다. 유니온에 적용되면 각 멤버마다 자동으로 분산되고, `infer`로 내부 타입을 변수처럼 꺼낼 수 있다. `NonNullable`, `ReturnType` 같은 내장 유틸리티가 전부 이 패턴으로 만들어져 있다.

다음엔 지금까지 정리한 제네릭, 유틸리티 타입, 맵드 타입, 조건부 타입이 실제 React 컴포넌트 props에서 어떻게 조합되는지 살펴볼 예정이다.
