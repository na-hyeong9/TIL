# [CSS] - 6 - Color와 Background, 색과 배경의 기초

> 2026.07.01

---

## 지난 편에서

line-height와 letter-spacing으로 텍스트의 가독성을 조정하는 법을 다뤘다. 이번엔 방향을 틀어 — 화면을 구성하는 색과 배경 속성들을 정리한다. 보기엔 단순해 보여도 생각보다 많은 선택지가 숨어 있다.

---

## color: 텍스트 색

`color`는 텍스트와 텍스트 장식(밑줄 등)의 색을 결정한다. 값으로는 키워드, hex, rgb, hsl 등을 쓸 수 있다.

```css
p { color: #333; }
p { color: rgb(51, 51, 51); }
p { color: hsl(0, 0%, 20%); }
```

요즘은 `hsl`을 선호하는 경향이 있다. 색조(Hue), 채도(Saturation), 명도(Lightness)를 직관적으로 조절할 수 있어서다. `hsl(210, 80%, 50%)`처럼 쓰면 "파란 계열, 채도 높고, 중간 밝기"가 바로 떠오른다. hex는 간결하지만 값만 봐서는 무슨 색인지 알기 어렵다.

`currentColor` 키워드도 알아두면 유용하다. 요소에 설정된 `color` 값을 그대로 참조한다.

```css
.icon {
  color: tomato;
  border: 1px solid currentColor; /* 테두리도 tomato 색 */
}
```

---

## background-color: 배경 색

가장 기본적인 배경 속성이다. 투명도가 있는 색을 쓸 때는 `rgba` 혹은 `hsl`의 alpha 인자를 사용한다.

```css
.box { background-color: rgba(0, 0, 0, 0.4); }
.box { background-color: hsl(0 0% 0% / 0.4); }  /* 최신 문법 */
```

`opacity`와 헷갈리지 말아야 한다. `opacity: 0.4`는 요소 전체를 반투명하게 만들어서 자식 요소까지 영향을 준다. 배경만 반투명하게 하고 싶다면 `background-color`에 alpha를 주는 게 맞다.

---

## background-image와 gradient

배경에 이미지를 넣거나, 그라디언트를 사용할 수 있다.

```css
/* 이미지 */
.hero { background-image: url('/images/hero.jpg'); }

/* 그라디언트 */
.card { background-image: linear-gradient(135deg, #667eea, #764ba2); }
```

`linear-gradient`는 방향과 색상 목록을 받는다. 방향은 각도(`135deg`)나 키워드(`to right`, `to bottom right`)로 쓴다. 원형은 `radial-gradient`, 원뿔형은 `conic-gradient`다. 그라디언트는 이미지 값이므로 `background-color`가 아니라 `background-image`에 써야 한다.

---

## background-size, position, repeat

이미지를 배경으로 쓸 때 함께 자주 쓰이는 속성들이다.

```css
.hero {
  background-image: url('/images/hero.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
```

- `cover` — 컨테이너를 꽉 채우되 비율을 유지한다. 이미지 끝이 잘릴 수 있다.
- `contain` — 이미지 전체가 보이도록 맞춘다. 여백이 생길 수 있다.
- `center` — 이미지의 기준점을 가운데로 잡는다.
- `no-repeat` — 기본값인 반복을 막는다.

`background` 단축 속성으로 한 줄에 쓸 수도 있다.

```css
.hero {
  background: url('/images/hero.jpg') center/cover no-repeat;
}
```

순서는 `[image] [position]/[size] [repeat]`. 처음엔 낯설지만 익숙해지면 간결하다.

---

## CSS 변수로 색 관리하기

색을 프로젝트 전반에서 일관되게 쓰려면 CSS 커스텀 프로퍼티로 관리하는 게 좋다.

```css
:root {
  --color-text: #1a1a1a;
  --color-primary: hsl(220, 90%, 56%);
  --color-bg: #f9f9f9;
}

body {
  color: var(--color-text);
  background-color: var(--color-bg);
}
```

변수 이름을 구체적인 색 대신 역할 기반으로(`--color-primary`, `--color-text`) 지으면 다크모드 대응이나 테마 변경이 훨씬 수월해진다. Tailwind나 CSS-in-JS를 써도 이 사고방식은 배경에 깔려 있다.

---

## 오늘 얻은 것

`color`는 텍스트 색, `background-color`는 배경 색. 단순한 출발점 뒤에 투명도 처리, 그라디언트, 이미지 배경 제어, CSS 변수를 통한 색 시스템까지 꽤 넓은 영역이 이어진다. `hsl`과 CSS 변수를 조합하면 색을 체계적으로 다룰 수 있다. 다음엔 CSS에서 **transition과 animation**을 다룰 예정이다.
