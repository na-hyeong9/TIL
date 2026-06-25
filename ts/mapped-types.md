# [TypeScript] - 4 - 맵드 타입, 내 손으로 Partial을 만들어보자

> 2026.06.25

---

## 지난 편에서

유틸리티 타입을 정리하면서 `Partial`, `Readonly` 같은 헬퍼들이 전부 제네릭으로 만들어져 있다고 했다. 이번엔 그 내부를 열어본다. 핵심 문법은 **맵드 타입(Mapped Type)** — 기존 타입의 프로퍼티를 순회하면서 변환하는 방식이다.

---

## 기본 문법

```ts
type MyMapped<T> = {
  [K in keyof T]: T[K];
};
```

`keyof T`는 `T`의 모든 키를 유니온 타입으로 뽑아낸다. `[K in keyof T]`는 그 키들을 하나씩 순회한다. `T[K]`는 원래 값의 타입을 그대로 쓴다.

위 코드는 `T`를 그대로 복사하는 타입이다. 실용성은 없지만, 구조를 이해하는 출발점이 된다.

---

## Partial을 직접 만들어보면

유틸리티 타입 `Partial<T>`의 실제 구현은 이렇게 생겼다.

```ts
type MyPartial<T> = {
  [K in keyof T]?: T[K];
};
```

`?` 하나 추가했을 뿐인데, 모든 프로퍼티가 선택적으로 바뀐다. `Partial`이 마법이 아니라 단순한 문법 응용이라는 게 보인다.

같은 방식으로 `Readonly`도 만들 수 있다.

```ts
type MyReadonly<T> = {
  readonly [K in keyof T]: T[K];
};
```

---

## 값 타입을 바꾸고 싶을 때

맵드 타입은 키만 순회하는 게 아니라 값의 타입도 바꿀 수 있다.

```ts
type Stringify<T> = {
  [K in keyof T]: string;
};

type User = { id: number; name: string; active: boolean };
type StringUser = Stringify<User>;
// { id: string; name: string; active: string; }
```

모든 값을 `string`으로 바꿨다. 폼 데이터처럼 서버에서 모든 필드가 문자열로 넘어오는 경우에 실제로 쓰인다.

---

## as로 키 이름까지 바꾸기 (TS 4.1+)

```ts
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type UserGetters = Getters<User>;
// { getId: () => number; getName: () => string; getActive: () => boolean; }
```

`as` 절로 키 이름을 템플릿 리터럴 타입과 결합해 변환할 수 있다. 이 수준부터는 타입이 코드 생성에 가까워진다.

---

## 오늘 얻은 것

유틸리티 타입이 "미리 만들어둔 도구"라면, 맵드 타입은 그 도구를 만드는 공장이다. `keyof`로 키를 뽑고, `in`으로 순회하고, `?` 또는 `readonly`로 수식어를 달고, `T[K]`로 원래 값 타입을 쓴다. 직접 만들어보고 나니 유틸리티 타입이 훨씬 친숙하게 느껴진다.

다음엔 이 맵드 타입과 함께 자주 등장하는 **조건부 타입(Conditional Type)**을 정리할 예정이다.
