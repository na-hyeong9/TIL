# [CSS] - 3 - position과 z-index, 쌓임 맥락의 이해

> 2026.06.08

---

## 들어가며

Flexbox와 Grid가 흐름(flow) 안에서 아이템을 배치하는 도구라면, `position`은 그 흐름 바깥으로 나가는 탈출구다. 팝업, 툴팁, 고정 헤더, 드롭다운 — 이 모든 것이 `position` 없이는 만들 수 없다. 그리고 그것들이 화면 위에서 서로 겹칠 때, `z-index`가 누가 앞에 보일지를 결정한다.

---

## position의 네 가지 값

**static** — 기본값이다. 모든 요소는 기본적으로 `static`이고, `top / right / bottom / left` 속성이 아무 효과도 없다.

**relative** — 자신의 원래 위치를 기준으로 이동한다. 중요한 건, 자리를 실제로 비우지 않는다는 점이다. 다른 요소는 여전히 그 요소가 원래 자리에 있다고 인식한다.

```css
.badge {
  position: relative;
  top: -4px;
  left: 2px;
}
```

**absolute** — 가장 가까운 `position`이 설정된 조상 요소를 기준으로 위치를 잡는다. 조상 중에 아무도 없으면 뷰포트를 기준으로 삼는다. 문서 흐름에서 완전히 빠져나와 자리를 차지하지 않는다.

```css
.tooltip {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
}
```

이 패턴이 자주 쓰인다. 부모에 `position: relative`를 주고, 자식 툴팁을 부모 기준으로 띄우는 방식이다.

**fixed** — 뷰포트를 기준으로 고정된다. 스크롤해도 위치가 변하지 않는다. 고정 헤더나 플로팅 버튼에 쓴다.

```css
.floating-btn {
  position: fixed;
  bottom: 24px;
  right: 24px;
}
```

---

## z-index: 쌓임 순서

같은 위치에 여러 요소가 겹쳤을 때, `z-index`가 높을수록 앞에 그려진다. 단, `z-index`는 `position`이 `static`이 아닌 요소에만 적용된다.

```css
.modal-overlay {
  position: fixed;
  z-index: 100;
}

.modal-dialog {
  position: relative;
  z-index: 200;
}
```

---

## 쌓임 맥락(Stacking Context)

여기서 많은 사람이 막히는 개념이 나온다. `z-index: 9999`를 줬는데도 다른 요소 뒤로 숨어버리는 현상, 다들 한 번쯤 겪어봤을 것이다.

원인은 **쌓임 맥락**이다. `position`과 `z-index`가 조합되거나, `opacity < 1`, `transform`, `filter` 등 특정 속성이 붙으면 그 요소는 자체적인 쌓임 맥락을 형성한다. 맥락 안의 `z-index`는 해당 맥락 내부에서만 의미를 가진다.

```css
.parent {
  position: relative;
  z-index: 1;
  /* 새로운 쌓임 맥락 생성 */
}

.child {
  position: absolute;
  z-index: 9999;
  /* z-index 9999지만, .parent 맥락 안에서만 유효 */
}
```

`.child`가 아무리 높은 `z-index`를 가져도, 다른 요소가 `.parent`보다 높은 `z-index`를 가지면 그 요소 아래로 깔린다. 맥락의 경계를 넘을 수 없다.

**디버깅 팁**: z-index가 말을 안 들으면 부모 중에 쌓임 맥락을 만드는 속성(`transform`, `opacity`, `will-change` 등)이 있는지 먼저 확인한다.

---

## 실무 패턴: 모달 구조

```css
.modal-backdrop {
  position: fixed;
  inset: 0; /* top/right/bottom/left: 0 의 단축 */
  background: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}

.modal-box {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1001;
}
```

`inset: 0`은 화면 전체를 덮는 배경에 자주 쓰는 패턴이다. `transform: translate(-50%, -50%)`은 정중앙 배치의 고전적인 방법으로, top/left를 50%로 잡고 자신의 크기의 절반만큼 역방향으로 당기는 원리다.

---

## 오늘 얻은 것

`position`은 흐름에서 벗어나는 도구이고, `z-index`는 그 위에서 쌓임 순서를 제어한다. 핵심은 **쌓임 맥락**이다. `z-index` 값만 높이면 된다고 생각하면 반드시 막히는 벽이 생긴다. 조상 요소에 쌓임 맥락을 만드는 속성이 있는지 확인하는 습관이 디버깅 시간을 줄여준다. 다음엔 요소의 크기와 간격을 결정하는 **box model과 box-sizing**을 정리할 예정이다.
