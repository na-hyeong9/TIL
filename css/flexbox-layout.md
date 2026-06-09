# [CSS] - 1 - Flexbox, 웹 레이아웃의 기본

> 2026.06.07

---

## 들어가며

TypeScript 시리즈를 잠시 접고, 이번엔 CSS 레이아웃의 핵심인 **Flexbox**를 정리한다. 오랫동안 웹 레이아웃은 `float`와 `position`으로 힘겹게 만들었다. Flexbox가 등장하면서 그 고통이 상당 부분 사라졌다.

---

## 기본 개념: 컨테이너와 아이템

Flexbox는 **컨테이너**와 **아이템**의 관계로 작동한다. 부모에 `display: flex`를 선언하는 순간, 직계 자식 요소들이 flex 아이템이 된다.

```css
.container {
  display: flex;
}
```

이 한 줄로 자식들은 가로로 나란히 배열된다. 핵심 개념은 두 가지 축이다. **주축(main axis)**은 기본적으로 가로 방향, **교차축(cross axis)**은 그에 수직인 세로 방향이다.

---

## 컨테이너 속성

**justify-content** — 주축 방향 정렬

```css
.container {
  display: flex;
  justify-content: space-between;
}
```

`flex-start`, `flex-end`, `center`, `space-between`, `space-around`가 주로 쓰인다. 헤더에서 로고와 메뉴를 양 끝에 두고 싶을 때 `space-between`이 정답이다.

**align-items** — 교차축 방향 정렬

```css
.container {
  display: flex;
  align-items: center;
}
```

수직 가운데 정렬이 이렇게 단순해진 것이 Flexbox가 가져온 가장 큰 변화 중 하나다. `float` 시절에는 `position: absolute`에 `transform: translateY(-50%)`까지 써야 했다.

**flex-direction** — 주축 방향 변경

```css
.container {
  display: flex;
  flex-direction: column;
}
```

`row`(기본), `column`, `row-reverse`, `column-reverse`를 쓸 수 있다. 모바일 레이아웃에서 가로 배열을 세로로 바꿔야 할 때 `column`이 자주 등장한다.

---

## 아이템 속성

**flex** — 공간 배분

```css
.item {
  flex: 1;
}

.item.wide {
  flex: 2; /* 다른 아이템의 2배 공간 차지 */
}
```

`flex`는 `flex-grow`, `flex-shrink`, `flex-basis`의 단축 속성이다. 실무에서는 `flex: 1`만으로도 충분한 경우가 많다. 남은 공간을 균등하게 나눠가진다는 의미다.

---

## 실무 패턴

헤더처럼 로고와 내비게이션을 양 끝에 두는 패턴:

```css
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 24px;
}
```

카드 리스트를 일정 간격으로 배치하면서 줄바꿈도 처리하는 패턴:

```css
.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
```

`flex-wrap`을 쓰면 아이템이 컨테이너 너비를 초과할 때 다음 줄로 넘어간다. `gap` 속성은 `margin`을 각 아이템에 개별로 줄 필요 없이 간격을 일괄 설정해준다.

---

## 오늘 얻은 것

Flexbox는 1차원 레이아웃(한 방향 배열)에 최적화된 도구다. `justify-content`로 주축을, `align-items`로 교차축을 다루고, `flex: 1`로 공간을 나눈다. 패턴 몇 가지만 익히면 대부분의 UI 레이아웃을 다룰 수 있다. 다음엔 2차원 레이아웃을 다루는 **CSS Grid**를 살펴볼 예정이다.
