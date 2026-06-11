# [TypeScript] - 3 - 유틸리티 타입, TS가 미리 만들어둔 도구들

> 2026.06.12

---

## 지난 편에서

제네릭을 정리하면서 `useState`, `Array`, `Promise` 같은 내장 타입들이 전부 제네릭으로 만들어져 있다는 걸 알게 됐다.

이번엔 그 제네릭을 활용해 TS가 미리 만들어둔 **유틸리티 타입**들을 살펴본다. `Partial`, `Required`, `Pick`, `Omit`, `Readonly` — 이름은 들어봤어도 직접 써본 적이 없다면, 이 글이 시작점이 될 것 같다.

---

## 왜 필요한가

이런 상황을 생각해보자.

```ts
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}
```

회원가입 폼에서는 이 필드를 다 채워야 하지만, 회원 정보 수정 폼에서는 일부만 바꿀 수 있다. 그러면 수정용 타입이 따로 필요하다.

```ts
interface UpdateUser {
  id?: number;
  name?: string;
  email?: string;
  password?: string;
}
```

`User`에서 모든 필드에 `?`만 붙인 걸 또 썼다. `User`가 바뀌면 `UpdateUser`도 따로 고쳐야 한다. 여기서 유틸리티 타입이 등장한다.

---

## Partial — 모든 필드를 선택적으로

```ts
type UpdateUser = Partial<User>;
// { id?: number; name?: string; email?: string; password?: string; }
```

`Partial<T>`은 `T`의 모든 프로퍼티를 옵셔널(`?`)로 바꿔준다. `User`가 바뀌면 `UpdateUser`도 자동으로 따라간다.

---

## Required — 모든 필드를 필수로

`Partial`의 반대다. 선택적인 필드를 전부 필수로 만든다.

```ts
interface Config {
  host?: string;
  port?: number;
}

type StrictConfig = Required<Config>;
// { host: string; port: number; }
```

환경 검증 로직에서 "이 시점부터는 모든 설정이 채워져 있어야 한다"고 명시할 때 쓸 수 있다.

---

## Pick과 Omit — 일부만 고르거나 빼거나

`Pick<T, K>`는 `T`에서 `K`에 해당하는 프로퍼티만 뽑아온다.

```ts
type UserPreview = Pick<User, 'id' | 'name'>;
// { id: number; name: string; }
```

`Omit<T, K>`는 반대로 `K`를 제거하고 나머지를 가져온다.

```ts
type PublicUser = Omit<User, 'password'>;
// { id: number; name: string; email: string; }
```

API 응답에서 민감한 필드를 제거하거나, 컴포넌트 props를 원본 타입에서 일부만 떼어낼 때 자주 쓴다.

---

## Readonly — 변경 불가

```ts
type ImmutableUser = Readonly<User>;

const user: ImmutableUser = { id: 1, name: '홍길동', email: 'a@b.com', password: '1234' };
user.name = '김철수'; // 에러! 읽기 전용
```

`Readonly<T>`는 모든 프로퍼티를 읽기 전용으로 만든다. 상태 관리에서 불변성을 타입 수준으로 강제하고 싶을 때 유용하다.

---

## 오늘 얻은 것

유틸리티 타입은 결국 제네릭으로 만들어진 헬퍼들이다. `Partial<T>` 내부를 들여다보면 맵드 타입(Mapped Type)이 쓰인다 — 그건 다음에 정리할 예정이다.

오늘 핵심은 **기존 타입에서 새 타입을 파생시키는 패턴**을 익히는 것이다. 타입을 매번 새로 쓰는 게 아니라, 하나의 원천 타입에서 용도에 맞게 변형해 쓰면 유지보수가 훨씬 편해진다.
