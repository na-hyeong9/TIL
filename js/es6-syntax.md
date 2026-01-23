# [JS] 모던 자바스크립트(ES6+) 핵심 문법 정리

## 1. Intro
React나 Vue 같은 최신 프레임워크 코드를 보면 `function` 키워드보다 `const`, `=>` 같은 기호들이 더 많이 보인다.
이는 **ES6(ECMAScript 2015)** 이후 도입된 문법들로, 코드의 가독성을 높이고 생산성을 올려준다.
퍼블리셔에서 프론트엔드 개발자로 넘어가기 위해 반드시 익숙해져야 할 **실무 필수 문법 3가지**를 정리한다.



## 2. 화살표 함수 (Arrow Function)

기존 `function` 키워드를 대체하는 간결한 문법이다. 특히 `this` 바인딩 방식이 달라 콜백 함수에서 유용하다.

```javascript
// [ES5] 기존 방식
var sum = function(a, b) {
    return a + b;
};

// [ES6] 화살표 함수
// 1. 기본 형태
const sum = (a, b) => {
    return a + b;
};

// 2. 단축 형태 (본문이 한 줄이면 중괄호와 return 생략 가능)
const multiply = (a, b) => a * b;

// 3. 인자가 하나면 소괄호 생략 가능
const greet = name => console.log(`Hello, ${name}`);
```



## 3. 구조 분해 할당 (Destructuring Assignment)

객체나 배열에 저장된 값을 마치 '분해'하듯이 꺼내어 변수에 담는 방식이다. API로 받은 데이터를 처리할 때 매우 강력하다.

JavaScript

```
const user = {
    name: '홍길동',
    job: 'Web Publisher',
    skills: {
        main: 'HTML/CSS',
        sub: 'JS'
    }
};

// [ES5] 일일이 변수에 할당
// var name = user.name;
// var job = user.job;

// [ES6] 구조 분해 할당
const { name, job } = user;
console.log(name); // '홍길동'

// 중첩된 객체도 한 번에 꺼낼 수 있다 (Alias 설정 가능)
const { main: mainSkill } = user.skills;
console.log(mainSkill); // 'HTML/CSS'
```



## 4. 템플릿 리터럴 (Template Literal)

문자열을 합칠 때 `+` 연산자 지옥에서 벗어나게 해주는 문법이다. 백틱(```)을 사용한다.

JavaScript

```
const group = '퍼블리싱팀';
const name = '김단형';

// [ES5]
// console.log('안녕하세요, ' + group + '의 ' + name + '입니다.');

// [ES6]
console.log(`안녕하세요, ${group}의 ${name}입니다.`);

// 줄바꿈도 자유롭다 (HTML 마크업 짤 때 유용)
const html = `
    <div class="card">
        <h2>${name}</h2>
        <p>${group}</p>
    </div>
`;
```

## 5. 결론 (Today I Learned)

처음에는 `function`이 없어서 어색했지만, 익숙해지니 코드가 훨씬 간결해졌다.

특히 **템플릿 리터럴**은 자바스크립트 안에서 HTML 태그를 동적으로 생성할 때 가독성이 압도적으로 좋아서, 앞으로 적극적으로 활용해야겠다.