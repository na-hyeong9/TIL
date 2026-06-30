# [CSS] - 5 - Typography: line-height와 letter-spacing

> 2026.06.30

---

## 지난 편에서

box model에서 요소의 크기가 어떻게 계산되는지 살펴봤다. 이번엔 방향을 틀어 — 텍스트 자체를 어떻게 제어하는지를 다룬다. 레이아웃을 잡는 것만큼 중요한 게 가독성이고, 가독성의 핵심은 line-height와 letter-spacing이다.

---

## line-height: 줄 간격

`line-height`는 줄과 줄 사이의 간격이다. 글자 크기(font-size)를 기준으로 줄이 차지하는 전체 높이를 결정한다.

```css
/* 단위 있는 값 */
p { line-height: 24px; }

/* 단위 없는 값 (권장) */
p { line-height: 1.6; }
```

단위 없는 값을 쓰는 게 좋다. `1.6`이면 font-size의 1.6배라는 뜻인데, 자식 요소에서 font-size가 바뀌어도 비율이 그대로 따라온다. 반면 `24px`처럼 고정값을 쓰면 자식의 font-size가 달라졌을 때 줄 간격이 어긋난다.

본문 텍스트는 보통 `1.5~1.8` 사이를 쓴다. 제목(heading)은 `1.1~1.3` 정도가 적당하다. 줄이 짧을수록 촘촘해도 읽기 편하고, 줄이 길면 넓게 벌려야 시선 이동이 수월하다.

---

## letter-spacing: 자간

`letter-spacing`은 글자 사이의 간격이다.

```css
h1 { letter-spacing: -0.02em; }
p  { letter-spacing: 0.01em; }
```

`em` 단위를 쓰면 font-size에 비례해서 자간이 잡힌다. 제목처럼 큰 글자는 자간이 넓어 보여서 살짝 좁히는 게 일반적이고(`-0.02em` 정도), 본문은 기본값(0)이나 아주 조금 넓히는 쪽이 읽기 편하다.

한 가지 주의할 점: 한글에는 `letter-spacing`이 마지막 글자에도 적용된다. 오른쪽 정렬이나 가운데 정렬일 때 미묘한 우측 여백이 생기는 이유다.

---

## font-size와 rem

`line-height`와 `letter-spacing`을 `em`으로 쓰면 font-size가 기준이 된다. 그 font-size 자체는 `rem`으로 잡는 게 현대 CSS의 관례다.

```css
:root { font-size: 16px; } /* 1rem = 16px */

h1 { font-size: 2rem; }    /* 32px */
p  { font-size: 1rem; }    /* 16px */
```

`rem`은 루트(html) 요소의 font-size를 기준으로 한다. `em`이 부모를 기준으로 해서 중첩될수록 복잡해지는 것과 달리, `rem`은 항상 같은 기준이라 예측하기 쉽다. `:root`에 `font-size: 62.5%`를 줘서 `1rem = 10px`로 맞추는 패턴도 있지만, 사용자의 브라우저 기본 글꼴 크기 설정을 무시하게 되므로 접근성 측면에서 `16px` 기준을 그대로 두는 편이 요즘 추세다.

---

## 오늘 얻은 것

`line-height`는 단위 없이 쓰고, `letter-spacing`은 `em`으로 쓰면 font-size 변화에 유연하게 대응한다. 제목과 본문의 line-height, letter-spacing을 구분해서 쓰는 것만으로 가독성이 크게 달라진다. 텍스트도 레이아웃처럼 수치 하나하나에 이유가 있다. 다음엔 CSS에서 **Color와 Background** 속성을 정리할 예정이다.
