# [TypeScript] - 6 - React props에서 타입 조합하기

> 2026.06.25

---

## 지난 편에서

제네릭, 유틸리티 타입, 맵드 타입, 조건부 타입을 차례로 정리했다. 이번엔 그것들이 실제 React 컴포넌트에서 어떻게 조합되는지 살펴본다. 추상적으로 배운 것들이 코드에서 어떤 모습을 하는지 확인하는 시간이다.

---

## 베이스 props 확장하기

공통 props가 있고, 각 컴포넌트가 그걸 확장해야 하는 상황은 흔하다.

```ts
type BaseProps = {
  className?: string;
  children?: React.ReactNode;
};

type ButtonProps = BaseProps & {
  onClick: () => void;
  disabled?: boolean;
};
```

`&`로 교차 타입을 만들면 `ButtonProps`는 `BaseProps`의 모든 필드를 포함한다. 상속보다 간단하고, 여러 타입을 한번에 합칠 수도 있다.

---

## 제네릭 컴포넌트

리스트 컴포넌트처럼 어떤 데이터든 받아야 할 때 제네릭을 쓴다.

```ts
type ListProps<T> = {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
};

function List<T>({ items, renderItem }: ListProps<T>) {
  return <ul>{items.map((item, i) => <li key={i}>{renderItem(item)}</li>)}</ul>;
}
```

`T`가 뭔지 몰라도 `items`와 `renderItem`의 타입이 일치한다는 걸 컴파일 타임에 보장할 수 있다.

---

## 유틸리티 타입으로 props 변형하기

이미 정의된 타입의 일부만 필요하거나, 일부를 선택적으로 만들어야 할 때가 있다.

```ts
type User = {
  id: number;
  name: string;
  email: string;
};

// 편집 폼 — id는 필수, 나머지는 선택
type EditFormProps = Pick<User, 'id'> & Partial<Omit<User, 'id'>>;
```

`Omit`으로 `id`를 제외한 나머지를 뽑고, `Partial`로 선택적으로 만든 뒤, `Pick<User, 'id'>`와 합쳤다. 원본 `User` 타입을 건드리지 않고 용도에 맞는 props를 만들어냈다.

---

## 조건부 타입으로 props 분기하기

버튼 컴포넌트가 `href`를 받으면 앵커로, 아니면 버튼으로 동작해야 할 때 조건부 타입이 유용하다.

```ts
type ButtonOrLinkProps =
  | ({ href: string } & React.AnchorHTMLAttributes<HTMLAnchorElement>)
  | ({ href?: never } & React.ButtonHTMLAttributes<HTMLButtonElement>);
```

`href`가 있으면 앵커 속성이, 없으면 버튼 속성이 타입으로 보장된다. `never`를 쓰는 게 핵심인데, `href`가 있는 경우와 없는 경우를 명확히 나눠준다.

---

## 오늘 얻은 것

각각 배울 때는 추상적이던 것들이 React props에서 만나면 구체적인 문제를 푸는 도구가 된다. `&`로 합치고, 제네릭으로 재사용성을 높이고, `Pick`/`Omit`/`Partial`로 기존 타입을 변형하고, 유니온으로 조건에 따라 props를 분기한다. 타입을 먼저 설계하면 컴포넌트 API가 저절로 명확해지는 경험을 할 수 있다.

다음엔 TypeScript 시리즈에서 잠깐 벗어나 **CSS** 쪽을 다뤄볼 예정이다.
