# [TypeScript] - 1 - type과 interface, 뭐가 다르고 언제 쓸까

> 2026.06.11

---

## 지난 편에서

TypeScript를 쓰는 이유를 정리하면서 마지막에 이런 말을 했다.

> "다음은 타입 vs 인터페이스 차이를 정리해볼 예정이다."

실제로 써보면 금방 이런 갈림길이 생긴다.

```ts
type User = {
  name: string;
  age: number;
};

interface User {
  name: string;
  age: number;
}
```

둘 다 같은 모양이다. 뭐가 다른 거지?

---

## 생김새는 같아도 성격이 다르다

`type`과 `interface`는 객체 구조를 정의하는 용도로는 거의 동일하게 동작한다. 하지만 다룰 수 있는 범위와 할 수 있는 것들이 다르다.

### type이 할 수 있는 것들

`type`은 **타입 별칭(Type Alias)** 이다. 타입에 이름을 붙이는 것인데, 객체뿐 아니라 원시 타입, 유니온, 튜플 등 무엇이든 이름을 붙일 수 있다.

```ts
// 원시 타입에 별칭
type ID = string;
type Count = number;

// 유니온 타입 (여러 타입 중 하나)
type Status = "pending" | "fulfilled" | "rejected";

// 튜플 (고정 길이 배열)
type Coordinate = [number, number];

// 함수 타입
type Callback = (data: string) => void;
```

이런 건 `interface`로는 할 수 없다. `interface`는 **객체 구조**만 정의할 수 있다.

---

### interface가 할 수 있는 것들

`interface`는 **확장(Extension)** 에 강하다.

```ts
interface Animal {
  name: string;
}

interface Dog extends Animal {
  breed: string;
}

const dog: Dog = {
  name: "초코",
  breed: "포메라니안",
};
```

`extends`로 기존 인터페이스를 이어받아 확장할 수 있다. `type`도 `&`(인터섹션)로 비슷하게 할 수 있지만, 쓰는 방식이 다르다.

```ts
type Animal = { name: string };
type Dog = Animal & { breed: string };
```

결과는 같지만 `interface extends`가 더 선언적으로 읽히는 편이다.

---

### interface만 가능한 것: 선언 병합(Declaration Merging)

`interface`에는 독특한 특성이 하나 있다. **같은 이름으로 여러 번 선언하면 자동으로 합쳐진다.**

```ts
interface Config {
  host: string;
}

interface Config {
  port: number;
}

// 둘이 자동으로 합쳐짐
const config: Config = {
  host: "localhost",
  port: 3000,
};
```

라이브러리 타입을 외부에서 확장할 때 이걸 쓴다. 예를 들어 `window` 객체에 커스텀 프로퍼티를 추가해야 할 때가 있다.

```ts
declare global {
  interface Window {
    analytics: Analytics;
  }
}
```

`type`은 같은 이름으로 두 번 선언하면 에러가 난다. 이 차이는 라이브러리 타입을 다룰 때 생각보다 자주 마주치게 된다.

---

## 그래서 뭘 써야 하나

결론은 팀마다, 프로젝트마다 다르다. 근데 기준이 없으면 매번 헷갈리니까 이렇게 정리해뒀다.

| 상황                                | 추천         |
| ----------------------------------- | ------------ |
| 객체 구조 정의 (API 응답, props 등) | `interface`  |
| 유니온, 튜플, 원시 타입 별칭        | `type`       |
| 라이브러리 타입 확장                | `interface`  |
| React 컴포넌트 props                | 둘 다 통용됨 |

React 커뮤니티에서는 `type`으로 props를 정의하는 코드가 많이 보이고, 백엔드 성향이 짙은 코드에서는 `interface`가 많다. 취향 차이라고 봐도 무방하다.

중요한 건 **한 프로젝트 안에서 일관성을 유지하는 것**이다. 어디선 `type`, 어디선 `interface`가 섞이면 읽기가 불편해지고 팀원이 혼란스러워한다.

---

## 오늘 얻은 것

겉보기에는 같아 보여서 뭐가 다른지 계속 헷갈렸는데, `type`은 범용 별칭, `interface`는 객체 전용 + 확장에 특화라고 구분하니까 기준이 생겼다.

특히 선언 병합이 `interface`에만 있다는 건 처음 알았다. 라이브러리 타입을 만질 일이 생기면 자연스럽게 `interface`를 쓰게 될 것 같다.
