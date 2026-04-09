# [Mobile] iOS/Android 가상 키보드 활성화 시 레이아웃 뷰포트 이슈 해결

## 1. Intro (The Problem)
Video.js 기반의 동영상 플레이어 위에서 작동하는 '실시간 댓글(Comment)' 기능을 구현하던 중, 모바일 환경에서 심각한 레이아웃 이슈를 발견했다.
댓글 입력을 위해 `input`에 포커스하면 가상 키보드가 올라오는데, 이때 **입력창이 키보드 뒤로 숨거나, 엉뚱한 위치(화면 중간)에 붕 떠버리는 현상**이 발생했다.
단순히 `position: fixed; bottom: 0;`으로는 해결되지 않는 **모바일 브라우저의 뷰포트 특성** 때문이었다.



## 2. 원인 분석: Viewport의 두 얼굴

데스크톱과 달리 모바일 브라우저는 **Layout Viewport**와 **Visual Viewport**가 분리되어 동작한다.

1.  **Layout Viewport:** 전체 문서의 크기. 키보드가 올라와도 줄어들지 않고 그대로 유지되는 경우가 많다. (특히 iOS)
2.  **Visual Viewport:** 사용자가 실제로 보고 있는 화면의 크기. 키보드가 올라오면 그만큼 줄어든다.

**[문제의 핵심]**
CSS의 `bottom: 0`은 변하지 않는 **Layout Viewport**를 기준으로 배치되므로, 키보드가 올라와서 실제 화면(Visual Viewport)이 작아졌음에도 불구하고 입력창은 여전히 "키보드 아래쪽(가려진 영역)"에 머물러 있게 된다.



## 3. 해결 과정: Visual Viewport API 활용

CSS만으로는 '줄어든 화면 높이'를 실시간으로 알 수 없기에, 자바스크립트의 **Visual Viewport API**를 도입하여 스타일을 동적으로 보정했다.

### 핵심 로직
1.  `window.visualViewport`의 `resize` 이벤트를 감지한다.
2.  키보드가 올라와서 뷰포트 높이(`height`)가 변하면, 그 높이를 계산한다.
3.  입력창의 `bottom` 값을 **"전체 높이 - 현재 보이는 높이"** 만큼 위로 올려준다.

```javascript
if (window.visualViewport) {
  window.visualViewport.addEventListener('resize', handleResize);
  window.visualViewport.addEventListener('scroll', handleResize); // 중요!
}

function handleResize() {
  const commentBox = document.querySelector('.comment-input-wrap');
  
  // 전체 브라우저 높이 - 현재 눈에 보이는 높이 = 키보드 높이(오차 포함)
  // 이 차이만큼 입력창을 위로 밀어 올림
  const offset = window.innerHeight - window.visualViewport.height;
  
  commentBox.style.bottom = `${offset}px`;
}
```



### 💡 왜 'scroll' 이벤트까지 감지하는가?

단순히 키보드가 올라오는 것(`resize`)만 감지하면 될 것 같지만, **iOS(Safari)** 환경을 위해 `scroll` 이벤트가 필수적이다.

1. **스크롤 시 위치 이탈 방지:** iOS에서는 키보드가 열린 상태에서 화면을 스크롤하면, `fixed` 요소가 Visual Viewport를 따라오지 못하고 붕 뜨거나 덜덜거리는(Jittering) 현상이 발생한다.

2. **핀치 줌(Pinch Zoom) 대응:** 사용자가 화면을 확대(Zoom)하거나 이동할 때도 입력창이 시야에서 사라지지 않고 키보드 상단에 계속 붙어있게 하려면 `scroll` 이벤트로 실시간 위치를 잡아줘야 한다.

   

## 4. 추가 대응: iOS Safe Area

아이폰(iOS)의 경우 하단 제스처 바(Home Indicator) 영역이 있어서, 키보드가 없을 때도 입력창이 바닥에 너무 딱 붙는 문제가 있었다.

이는 CSS 환경 변수로 간단히 해결했다.

```css
.comment-input-wrap {
  /* 기본적으로 제스처 바 위쪽에 위치하도록 설정 */
  padding-bottom: env(safe-area-inset-bottom, 0px);
}
```



## 5. 결론 (Today I Learned)

처음에는 "왜 CSS가 안 먹지?"라고 당황했지만, 모바일 브라우저가 키보드를 처리하는 방식(Resizing vs Pushing)이 OS마다 다르다는 것을 알게 되었다.

**Visual Viewport API**를 통해 '사용자가 실제로 보는 화면'을 기준으로 UI를 제어하고, 특히 **iOS의 스크롤 특성까지 방어적으로(Defensive) 코딩**함으로써 모든 모바일 환경에서 일관된 입력 경험을 제공할 수 있게 되었다