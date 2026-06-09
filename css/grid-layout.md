# [CSS] - 2 - Grid, 2차원 레이아웃의 시작

> 2026.06.07

---

## 들어가며

지난 편에서 Flexbox를 정리하면서 "1차원 레이아웃에 최적화된 도구"라고 했다. 그 말인즉슨, 행과 열을 동시에 제어해야 할 때는 Flexbox가 버거워진다는 뜻이다. **CSS Grid**는 그 자리를 채운다. 가로와 세로를 한 번에 잡아주는 2차원 레이아웃 시스템이다.

---

## 기본 개념: 격자 위에 올린다

Grid도 Flexbox처럼 컨테이너와 아이템 구조다. 부모에 `display: grid`를 선언하고, 열(column)과 행(row)의 구조를 정의한다.

```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
```

`fr`은 fraction(분수)의 약자로, 남은 공간을 비율로 나눈다. 위 코드는 3등분이다. Flexbox의 `flex: 1`과 비슷한 개념이지만, 열 수를 미리 선언한다는 점이 다르다.

---

## 핵심 속성 정리

**grid-template-columns / grid-template-rows** — 트랙 정의

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr 1fr;
  grid-template-rows: auto 300px;
}
```

첫 번째 열은 고정 200px, 나머지 두 열이 남은 공간을 반씩 나눈다. 행은 첫 번째가 콘텐츠 높이에 맞게(auto), 두 번째는 300px 고정.

**gap** — 간격

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
```

`repeat(3, 1fr)`은 `1fr 1fr 1fr`과 동일하다. 반복이 잦을 때 코드가 훨씬 짧아진다. `gap`은 행과 열 간격을 한 번에 설정한다. `row-gap`, `column-gap`으로 각각 지정할 수도 있다.

**grid-column / grid-row** — 아이템 배치

```css
.item-wide {
  grid-column: 1 / 3; /* 1번 선에서 3번 선까지, 2칸 차지 */
}

.item-tall {
  grid-row: 1 / 3; /* 행 2칸 차지 */
}
```

Grid의 선(line)은 열 수보다 하나 많다. 3열 그리드면 수직선이 1, 2, 3, 4번이다. `span` 키워드로 칸 수를 직접 쓸 수도 있다.

```css
.item-wide {
  grid-column: span 2; /* 2칸 차지 */
}
```

---

## 실무 패턴

**잡지 스타일 레이아웃**

```css
.layout {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 16px;
}

.main-article {
  grid-column: span 8;
}

.sidebar {
  grid-column: span 4;
}
```

12컬럼 그리드는 웹 디자인에서 오래된 관습이다. 8+4, 6+6, 4+4+4 등 다양한 조합이 가능해 유연성이 높다.

**카드 그리드 (반응형)**

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}
```

`auto-fill`과 `minmax`의 조합이 핵심이다. "최소 280px을 유지하면서, 공간이 허락하는 만큼 컬럼을 자동으로 채워라"는 뜻이다. 미디어 쿼리 없이도 반응형이 된다.

---

## Flexbox와 함께 쓰기

Grid가 좋다고 해서 Flexbox를 버릴 필요는 없다. 둘은 역할이 다르다.

- **Grid** — 페이지 전체 레이아웃, 격자 구조, 2차원 배치
- **Flexbox** — 컴포넌트 내부, 한 방향 배열, 가운데 정렬

헤더 바 안에서 로고와 메뉴를 정렬할 땐 Flexbox, 페이지 전체의 헤더·사이드바·콘텐츠 구조를 잡을 땐 Grid. 이 두 가지를 상황에 맞게 섞어 쓰는 게 실무 방식이다.

---

## 오늘 얻은 것

CSS Grid는 "격자 위에 아이템을 올린다"는 감각으로 접근하면 이해가 빠르다. `grid-template-columns`로 열 구조를 정의하고, `gap`으로 간격을 주고, 필요한 아이템만 `span`으로 늘린다. `auto-fill + minmax` 패턴은 반응형 그리드를 미디어 쿼리 없이 해결해주는 실용적인 조합이다. 다음엔 CSS의 시각적 완성도를 높이는 **position과 z-index**를 정리할 예정이다.
