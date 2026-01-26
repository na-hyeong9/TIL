# [CSS] SCSS로 칼퇴를 부르는 스타일링 자동화 (Mixin & 변수)

## 1. Intro
CSS 프로젝트가 커질수록 반복되는 코드(색상 코드, 미디어 쿼리, 중앙 정렬 등)를 관리하기 힘들어진다.
실무에서 **SCSS(Sass)**를 사용하는 가장 큰 이유는 이러한 반복 작업을 **변수(Variables)**와 **믹스인(Mixins)**으로 모듈화하여 유지보수 효율을 극대화하기 위함이다.
자주 사용하는 나만의 SCSS 패턴을 정리해 본다.



## 2. 변수(Variables)로 디자인 토큰 관리

디자인 시스템의 색상이나 폰트 크기 등을 변수로 정의해두면, 나중에 "메인 컬러 좀 바꿔주세요"라는 요청이 왔을 때 한 줄만 수정하면 된다.

```scss
/* _variables.scss */

// 1. 색상 팔레트 (Color Palette)
$color-primary: #3498db;
$color-secondary: #2ecc71;
$color-danger: #e74c3c;
$color-gray-100: #f8f9fa;
$color-gray-900: #212529;

// 2. 폰트 및 레이아웃
$font-main: 'Pretendard', sans-serif;
$z-index-modal: 1000;
$z-index-nav: 100;

// 사용 예시
.btn-submit {
    background-color: $color-primary; // #3498db
    color: $color-gray-100;
    font-family: $font-main;
}
```



## 3. 믹스인(Mixin)으로 반복 코드 줄이기

가장 강력한 기능이다. 자주 쓰는 CSS 덩어리를 함수처럼 만들어두고 필요할 때 불러(`@include`) 쓴다.

### 1) 만능 중앙 정렬 (Flexbox)

매번 `display: flex`, `justify-content...` 치는 귀찮음을 해결한다.

```SCSS
@mixin flex-center {
    display: flex;
    justify-content: center;
    align-items: center;
}

// 사용 예시
.modal-body {
    @include flex-center;
    height: 100%;
}
```



### 2) 텍스트 말줄임 (...) 처리

한 줄 말줄임과 여러 줄 말줄임을 인자값으로 제어한다.

```scss
@mixin ellipsis($lines: 1) {
    @if ($lines == 1) {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    } @else {
        display: -webkit-box;
        overflow: hidden;
        text-overflow: ellipsis;
        -webkit-line-clamp: $lines;
        -webkit-box-orient: vertical;
    }
}

// 사용 예시
.title {
    @include ellipsis(1); // 한 줄 넘어가면 ...
}
.desc {
    @include ellipsis(3); // 3줄 넘어가면 ...
}
```

### 3) 반응형 미디어 쿼리

복잡한 미디어 쿼리 구문을 직관적인 이름으로 관리한다.

```scss
$mobile: 768px;
$tablet: 1024px;

@mixin mobile {
    @media (max-width: $mobile) {
        @content;
    }
}

// 사용 예시
.container {
    width: 1200px;
    
    @include mobile {
        width: 100%; // 모바일 화면에서는 100%로 변경
        padding: 0 20px;
    }
}
```



## 4. 결론 (Today I Learned)

SCSS를 도입하고 나서 CSS 라인 수가 획기적으로 줄었고, 디자인 수정 요청에 대응하는 속도가 훨씬 빨라졌다.

단순히 기능을 쓰는 것을 넘어, 팀원들과 **"어떤 변수명을 쓸지", "어떤 공통 믹스인을 만들지"** 약속(Convention)을 정하는 과정이 협업에 큰 도움이 된다는 것을 느꼈다.