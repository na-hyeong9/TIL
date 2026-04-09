# [CSS] 프로젝트의 시작: 견고한 Reset CSS와 공통 스타일 전략

## 1. Intro
HTML 구조를 잡았다면, 다음 단계는 브라우저마다 제각각인 기본 스타일을 초기화(Reset)하고 우리 프로젝트만의 규칙(Base)을 세우는 것이다.
단순히 구글링한 `reset.css`를 붙여넣기보다, **"왜 이 속성을 초기화해야 하는가?"**를 고민하며 나만의 실무용 베이스 코드를 정리해 본다.



## 2. 실무용 Reset & Base 코드 (Snippet)

실무에서 자주 사용하는 핵심 초기화 코드와 공통 스타일을 조합했다.

```css
@charset "utf-8";

/* 1. Box Model 초기화: 모든 요소의 크기를 테두리 포함으로 설정 */
*,
*::before,
*::after {
    box-sizing: border-box; 
}

/* 2. 여백 및 폰트 초기화 */
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
}

/* 3. HTML5 시멘틱 태그 블록 처리 (구형 브라우저 대응) */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section, main {
    display: block;
}

/* 4. 본문 기본 스타일 & 폰트 렌더링 최적화 */
body {
    line-height: 1.5;
    color: #000;
    background-color: #fff;
    /* 텍스트 렌더링을 선명하게 (Mac OS 대응) */
    -webkit-font-smoothing: antialiased; 
    -moz-osx-font-smoothing: grayscale;
    /* 긴 단어가 잘리는 것 방지 */
    word-break: keep-all; 
}

/* 5. 링크 및 리스트 초기화 */
a {
    color: inherit;
    text-decoration: none;
}
ol, ul, li {
    list-style: none;
}

/* 6. 이미지 및 미디어 반응형 대응 */
img, video, canvas, svg {
    max-width: 100%;
    height: auto;
    vertical-align: middle; /* 이미지 하단 미세한 여백 제거 */
}

/* 7. 버튼 및 폼 요소 초기화 */
button {
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    font: inherit;
    color: inherit;
}
button:disabled {
    cursor: not-allowed;
}
```



## 3. 핵심 포인트 분석 (Key Insights)

### 1) `box-sizing: border-box`의 중요성

기본값(content-box)을 사용하면 padding이나 border를 줄 때마다 width 값을 다시 계산해야 한다.

직관적인 레이아웃 설계를 위해 모든 요소(*)에 border-box를 적용하여, 설정한 width가 최종 크기가 되도록 통일한다.

### 2) `word-break: keep-all`

한글 웹 사이트에서 필수적인 속성이다. 기본값(normal)일 경우 단어 중간에서 줄바꿈이 일어나 가독성을 해친다.

keep-all을 적용하면 단어 단위로 줄바꿈이 되어 훨씬 깔끔한 텍스트 UI를 제공할 수 있다. (단, 영문 사이트에서는 break-word 고려)

### 3) 접근성을 해치지 않는 `outline` 관리

많은 Reset CSS에서 *:focus { outline: none; }을 습관적으로 넣곤 한다.

하지만 이는 **키보드 사용자(탭 키 이동)**가 현재 포커스 위치를 알 수 없게 만드는 치명적인 접근성 오류다.

디자인상 outline이 보기 싫다면, 반드시 대안 스타일(border 색상 변경이나 box-shadow)을 :focus 가상 클래스에 정의해주어야 한다.

### 4) 이미지 하단 여백 제거 (`vertical-align: middle`)

`img` 태그는 인라인 요소(Inline)이기 때문에 베이스라인(baseline)에 맞춰 정렬되면서 하단에 약 3~4px의 알 수 없는 여백이 생긴다. 이를 `vertical-align: middle` (또는 top)로 설정하여 해결한다.



## 4. 결론 (Today I Learned)

초기 세팅은 건물의 '지반 공사'와 같다.

무심코 복사해서 쓰던 코드들이 어떤 역할을 하는지 정확히 알고 쓰는 것이 중요하다. 특히 **접근성(outline)**과 **크로스 브라우징(main 태그, 폰트 스무딩)**을 고려한 나만의 Reset CSS를 갖추는 것은 전문성 있는 퍼블리셔의 기본 소양이다.

