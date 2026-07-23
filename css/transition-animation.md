# [CSS] - 7 - Transition과 Animation, 움직임의 기초

> 2026.07.23

---

## 지난 편에서

color와 background로 화면을 채우는 정적인 속성들을 정리했다. 이번엔 정적인 상태에서 벗어나 — 상태가 바뀔 때 어떻게 부드럽게 움직이는지를 다룬다. `transition`과 `animation`, 둘 다 "움직임"을 만들지만 쓰는 맥락이 다르다.

---

## transition: 상태 변화의 다리

`transition`은 속성값이 바뀔 때 그 변화를 부드럽게 이어준다. hover, 클래스 토글처럼 시작과 끝 상태만 있는 경우에 적합하다.

```css
.button {
  background-color: #667eea;
  transition: background-color 0.2s ease-in-out;
}

.button:hover {
  background-color: #4c51bf;
}
```

`transition`은 `property duration timing-function delay` 순서의 단축 속성이다. `property`를 `all`로 두면 편하지만, 의도치 않은 속성까지 애니메이션되어 성능에 영향을 줄 수 있어서 필요한 속성만 명시하는 게 낫다.

```css
.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}
```

여러 속성은 쉼표로 나열하고, 속성마다 다른 duration을 줄 수도 있다.

---

## animation: 스스로 움직이는 시퀀스

`transition`은 시작과 끝만 있지만, `animation`은 중간 단계를 `@keyframes`로 세밀하게 정의할 수 있다. hover 같은 트리거 없이도 로드되자마자 스스로 실행된다.

```css
@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.toast {
  animation: fade-in-up 0.4s ease-out forwards;
}
```

`animation` 단축 속성은 `name duration timing-function delay iteration-count direction fill-mode`를 받는다. 이 중 실무에서 자주 쓰는 건 `iteration-count`(반복 횟수, `infinite`도 가능)와 `fill-mode`다. `fill-mode: forwards`를 안 주면 애니메이션이 끝난 뒤 요소가 시작 상태로 튕겨 돌아가버려서, 최종 상태를 유지하고 싶을 때는 꼭 챙겨야 한다.

---

## 언제 무엇을 쓸까

- 특정 상호작용(hover, focus, 클래스 추가/제거)에 대한 반응 → `transition`
- 여러 단계를 거치는 시퀀스, 반복 재생, 트리거 없이 자동 실행 → `animation`

두 개념이 겹쳐 보이지만, `transition`은 "상태 A에서 B로"라는 단순한 보간이고 `animation`은 "정해진 시퀀스를 재생"이라는 차이로 구분하면 헷갈리지 않는다.

---

## 오늘 얻은 것

`transition`은 상태 변화를 잇는 다리, `animation`은 독립적으로 재생되는 시퀀스다. `fill-mode: forwards`를 빼먹지 않는 것과, `all` 대신 필요한 속성만 명시하는 것이 실무에서 자주 놓치는 포인트였다. 다음엔 JavaScript 쪽에서 **이벤트 위임(event delegation)**을 다뤄볼 예정이다.
