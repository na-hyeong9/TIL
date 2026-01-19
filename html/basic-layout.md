# [HTML] 기초 레이아웃: 시멘틱 태그와 웹 접근성

## 1. Intro
경력이 쌓일수록 화려한 CSS 기교보다 중요한 것이 **견고한 HTML 구조**임을 느낀다.
단순히 화면을 그리는 것을 넘어, 검색엔진(SEO)과 스크린 리더 사용자를 고려한 **'의미 있는(Semantic) 마크업'**의 정석을 정리해 본다.



## 2. 기본 레이아웃 구조 (Boilerplate)

웹 페이지의 가장 표준적인 시멘틱 구조는 다음과 같다.

```html
<body>
    <header>
        <h1>
            <a href="/">
                <img src="logo.png" alt="사이트 이름">
            </a>
        </h1>
        <nav>
            <h2 class="blind">메인 메뉴</h2>
            <ul>
                <li><a href="#">메뉴1</a></li>
                <li><a href="#">메뉴2</a></li>
            </ul>
        </nav>
    </header>

    <main id="content">
        <section>
            <h2>섹션 제목</h2>
            <p>섹션 설명 텍스트...</p>
            
            <article>
                <h3>아티클 제목</h3>
                <p>본문 내용...</p>
            </article>
        </section>

        <aside>
            <h2>관련 링크</h2>
            <ul>...</ul>
        </aside>
    </main>

    <footer>
        <address>Copyright © Company. All rights reserved.</address>
    </footer>
</body>
```



## 3. 실무 퍼블리싱 핵심 포인트 (Key Points)

단순히 태그만 외우는 것이 아니라, 실무에서 놓치기 쉬운 디테일을 챙겨야 한다.

### 1) 제목 태그(Heading)의 위계 준수

- 디자인 시안에 제목이 없더라도, 논리적 구조를 위해 `<h2~6>` 태그를 반드시 마크업하고 **IR(Image Replacement) 기법**이나 `.blind` 클래스로 숨김 처리해야 한다.
- 스크린 리더는 Heading 태그를 따라 문서를 탐색하기 때문에 `h2` 없이 `h3`가 바로 나오는 구조는 피해야 한다.

### 2) `section` vs `article` 구분 기준

- **`<article>`**: 뉴스 기사, 블로그 포스트, 쇼핑몰 상품 카드처럼 뚝 떼어내서 다른 곳에 붙여도 말이 되는 **독립적인 콘텐츠**.
- **`<section>`**: 서로 관련 있는 내용을 묶어주는 **일반적인 구획**. (반드시 내부에 제목 태그가 있어야 함)
- **`<div>`**: 의미 없이 단순히 스타일링(CSS)을 위해 묶어야 할 때 사용.

### 3) 메인 태그(`main`)와 IE 이슈

- `<main>` 태그는 Internet Explorer 11에서 블록 요소로 인식되지 않는 버그가 있다.

- 반드시 CSS Reset 파일에 `main { display: block; }`을 선언하거나, 태그에 `role="main"` 속성을 추가하여 호환성을 확보해야 한다.

  

## 4. 결론

"기초가 튼튼해야 무너지지 않는다." `div`로만 짜여진 코드는 나중에 유지보수하기도 힘들고, 무엇보다 웹의 본질인 '정보 전달'에 취약하다. 습관적인 `div` 사용을 줄이고, **"이 콘텐츠의 역할은 무엇인가?"**를 먼저 고민하는 습관을 들이자.
