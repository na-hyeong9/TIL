# TIL | 콜백 지옥과 Promise, async/await

> 2026.04.13

---

## 지난 편 복습

비동기는 "기다리지 않고 다음 작업을 먼저 처리하는 방식"이었다.

근데 문제가 있었다.

```js
let userData;

fetch("/api/user")
  .then((res) => res.json())
  .then((data) => { userData = data; });

console.log(userData); // undefined — 아직 안 왔음
```

비동기라서 순서 보장이 안 된다. 그래서 "데이터 받은 다음에 이걸 실행해줘"라고 명시해야 한다고 했다.

오늘은 그 방법 세 가지를 순서대로 살펴본다. **콜백 → Promise → async/await**, 왜 이렇게 발전해왔는지를 흐름으로 이해하면 된다.

---

## 1. 콜백(Callback)

콜백은 가장 원시적인 방법이다. "나중에 이거 실행해줘"하고 함수를 넘기는 것.

```js
function getUserData(callback) {
  setTimeout(function () {
    const data = { name: "김나형", age: 25 };
    callback(data); // 데이터 준비되면 콜백 실행
  }, 1000);
}

getUserData(function (data) {
  console.log(data.name); // "김나형"
});
```

진동벨에 비유하면, 벨이 울렸을 때 할 행동을 미리 적어두는 것이다. "벨 울리면 카운터로 와서 커피 받아가세요" 같은 느낌.

직관적이고 간단하다. **근데 문제가 생긴다.**

---

## 콜백 지옥(Callback Hell)

현실에서는 비동기 작업이 하나로 끝나지 않는다. 예를 들어 이런 시나리오라면?

```
1. 로그인해서 유저 ID 받기
2. 유저 ID로 게시글 목록 받기
3. 첫 번째 게시글로 댓글 받기
4. 댓글 작성자 정보 받기
```

콜백으로 구현하면 이렇게 된다.

```js
login(function (userId) {
  getPosts(userId, function (posts) {
    getComments(posts[0].id, function (comments) {
      getUser(comments[0].authorId, function (user) {
        console.log(user);
        // 여기서 또 뭔가 해야 한다면...?
      });
    });
  });
});
```

오른쪽으로 계속 파고드는 모양새다. 이걸 **콜백 지옥(Callback Hell)** 또는 **Pyramid of Doom**이라고 부른다.

```
login(
  getPosts(
    getComments(
      getUser(
        또 뭔가(
          또또 뭔가(
            ← 여기까지 도달한 나
          )
        )
      )
    )
  )
)
```

읽기도 힘들고, 에러 처리를 각 단계마다 해줘야 해서 유지보수가 악몽이 된다.

---

## 2. Promise

Promise는 ES6에서 등장한 해결책이다.

이름 그대로 **"약속"** 이다. "나중에 결과를 줄게. 성공하면 이거, 실패하면 저거 해줄게."

```js
const promise = new Promise(function (resolve, reject) {
  setTimeout(function () {
    const success = true;

    if (success) {
      resolve({ name: "김나형" }); // 성공
    } else {
      reject("에러 발생"); // 실패
    }
  }, 1000);
});

promise
  .then(function (data) {
    console.log(data.name); // 성공했을 때
  })
  .catch(function (error) {
    console.log(error); // 실패했을 때
  });
```

Promise는 세 가지 상태를 가진다.

| 상태 | 의미 |
|------|------|
| `pending` | 아직 결과가 없음 (대기 중) |
| `fulfilled` | 성공적으로 완료됨 |
| `rejected` | 실패함 |

한 번 fulfilled나 rejected가 되면 상태가 바뀌지 않는다. 결과가 확정된 것.

---

### 콜백 지옥을 Promise로 해결하면

`.then()`을 체이닝(chaining)할 수 있어서 깊이가 늘어나지 않는다.

```js
login()
  .then((userId) => getPosts(userId))
  .then((posts) => getComments(posts[0].id))
  .then((comments) => getUser(comments[0].authorId))
  .then((user) => console.log(user))
  .catch((error) => console.log(error)); // 에러는 여기서 한 번에
```

훨씬 읽기 편해졌다. 에러 처리도 `.catch()` 하나로 끝난다.

근데 아직도 `.then().then().then()...`이 이어지면 눈에 잘 안 들어오는 느낌이 있다.

---

## 3. async/await

ES2017에서 등장한 방법이다. Promise를 더 읽기 쉽게 써주는 문법이라고 보면 된다. Promise를 대체하는 게 아니라 **Promise 위에 얹힌 문법적 설탕(Syntactic Sugar)** 이다.

```js
async function getUser() {
  const userId = await login();           // 기다려
  const posts = await getPosts(userId);   // 기다려
  const comments = await getComments(posts[0].id); // 기다려
  const user = await getUser(comments[0].authorId);
  console.log(user);
}

getUser();
```

`await`는 "이거 끝날 때까지 기다려"라는 뜻이다. 동기 코드처럼 위에서 아래로 읽힌다.

단, `await`는 반드시 `async` 함수 안에서만 쓸 수 있다.

---

### 에러 처리는 try/catch로

```js
async function getUser() {
  try {
    const userId = await login();
    const posts = await getPosts(userId);
    console.log(posts);
  } catch (error) {
    console.log("에러 발생:", error); // 어디서 에러가 나든 여기서 잡힘
  }
}
```

일반 동기 코드에서 에러 잡는 것과 동일한 방식이라 익숙하게 쓸 수 있다.

---

## 세 가지 비교 정리

같은 작업을 세 가지 방식으로 쓰면 이렇다.

```js
// 콜백
getData(function(result) {
  process(result, function(final) {
    console.log(final);
  });
});

// Promise
getData()
  .then((result) => process(result))
  .then((final) => console.log(final))
  .catch((err) => console.log(err));

// async/await
async function run() {
  try {
    const result = await getData();
    const final = await process(result);
    console.log(final);
  } catch (err) {
    console.log(err);
  }
}
```

|           | 콜백          | Promise         | async/await        |
| --------- | ------------- | --------------- | ------------------ |
| 등장 시기 | 초창기        | ES6 (2015)      | ES2017 (2017)      |
| 가독성    | 중첩되면 최악 | 체이닝으로 개선 | 동기 코드처럼 읽힘 |
| 에러 처리 | 각 단계마다   | `.catch()` 하나 | `try/catch`        |
| 현재 사용 | 레거시 코드   | 병렬 처리 등    | 주로 이걸 씀       |

---

## 오늘 얻은 것

콜백 → Promise → async/await 순서로 **"어떤 불편함을 해결하려다 나왔는지"** 를 따라가니까 왜 이렇게 생겼는지가 이해됐다. 외울 필요 없이 흐름이 자연스럽게 납득이 가는 느낌.

현업에서는 async/await을 가장 많이 쓰지만, Promise를 모르면 async/await도 제대로 쓸 수 없다. 결국 셋 다 알아야 한다.

다음 편은 **이벤트 루프를 좀 더 깊게** — 콜 스택, 태스크 큐, 마이크로태스크 큐가 실제로 어떻게 돌아가는지 정리해볼 예정이다.
