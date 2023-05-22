# 실행방법과 실습환경

### 코드 작성과 실행

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <script> # JS 이외 나머지 html
            alert('Hello world'); 
        </script>
    </body>
</html>
```



1. 메모장에 복사한 뒤 -> 다른 이름으로 저장 (모든파일)

![image-20230522204818671](C:\Users\skgud\AppData\Roaming\Typora\typora-user-images\image-20230522204818671.png)



2. 웹에서 window(ctrl+o) ios(command+o) 후 파일 열기

![image-20230522210342005](C:\Users\skgud\AppData\Roaming\Typora\typora-user-images\image-20230522210342005.png)



3. 완료

![image-20230522210633251](C:\Users\skgud\AppData\Roaming\Typora\typora-user-images\image-20230522210633251.png)



### 크롬 개발자도구 - 콘솔 사용법

- 도구 단축키

  __F12__ or __ctrl+shift+i__ 로 실행

![image-20230522210948077](C:\Users\skgud\AppData\Roaming\Typora\typora-user-images\image-20230522210948077.png)



### console.log

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <script>
            console.log('Hello world');
        </script>
    </body>
</html>
```

![image-20230522212020395](C:\Users\skgud\AppData\Roaming\Typora\typora-user-images\image-20230522212020395.png)



### 주석

> 코드 설명
>
> 코드를 일지적으로 중지

```javascript
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <script type="text/javascript">
            /*
            	여러줄
            	여러줄
            	여러줄
            	여러줄
            */
            // <- 주석
        </script>
    </body>
</html>
```



### 줄바꿈과 여백

> 세미콜론을 활용

```html
<html>
    <body>
        <script type="text/javascript">
        	var a = 1;
        </script>
    </body>
</html>
```

