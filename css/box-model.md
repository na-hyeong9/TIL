# [CSS] - 4 - box model과 box-sizing, 크기와 간격의 원리

> 2026.06.30

---

## 지난 편에서

`position`과 `z-index`로 요소가 흐름에서 벗어나거나 겹쳤을 때 어떻게 처리하는지 살펴봤다. 이번엔 한 발 물러서서 — 요소의 크기는 도대체 어떻게 계산되는가를 다룬다.

---

## box model이란

브라우저가 모든 HTML 요소를 네 겹의 상자로 취급한다는 개념이다.

1. **content** — 텍스트나 이미지 등 실제 내용이 담기는 영역
2. **padding** — 내용물과 테두리 사이의 내부 여백
3. **border** — 테두리 선
4. **margin** — 이 요소와 다른 요소 사이의 외부 여백

`width`와 `height`는 기본적으로 content 영역에만 적용된다. 여기서 혼란이 시작된다.

---

## box-sizing: content-box vs border-box

`width: 200px`을 줬는데 실제로 200px이 아닌 상황, 다들 한 번쯤 겪어봤을 것이다.

**content-box (기본값)**

```css
.box {
  width: 200px;
  padding: 20px;
  border: 2px solid black;
}
/* 실제 점유 너비: 200 + 20*2 + 2*2 = 244px */
```

`width`가 content 영역만을 의미하기 때문에 `padding`과 `border`가 바깥으로 더해진다. 직관과 다르다.

**border-box**

```css
.box {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 2px solid black;
}
/* 실제 점유 너비: 200px */
```

`border-box`를 쓰면 `width` 안에 `padding`과 `border`까지 포함된다. 설정한 값이 그대로 전체 크기가 된다. 훨씬 직관적이라 현대 CSS에서는 거의 전역으로 설정한다.

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

리셋 CSS에서 이걸 가장 먼저 적어두는 이유가 여기에 있다.

---

## margin collapse

`padding`과 달리 `margin`에는 특이한 규칙이 있다. 세로 방향(block 방향)에서 인접한 두 요소의 margin은 합산되지 않고, 더 큰 값 하나로 겹쳐진다.

```css
.a { margin-bottom: 24px; }
.b { margin-top: 16px; }
/* .a와 .b 사이 간격: 24px (합인 40px이 아님) */
```

Flexbox나 Grid 컨테이너 안에서는 이 규칙이 적용되지 않는다. 세로 여백이 예상보다 작게 나올 때 collapse부터 의심해볼 만하다.

---

## 오늘 얻은 것

box model은 브라우저가 모든 요소의 크기를 계산하는 기본 단위다. `box-sizing: border-box`를 전역으로 설정하면 크기 계산이 직관적으로 바뀌고, 리셋 CSS에서 이걸 먼저 잡는 이유이기도 하다. margin collapse는 세로 방향 margin이 합산 대신 겹치는 동작이며, Flexbox/Grid 안에서는 발생하지 않는다. 다음엔 텍스트를 다루는 **Typography, line-height와 letter-spacing**을 정리할 예정이다.
