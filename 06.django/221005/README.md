# django CRUD

## Django Staticfiles 활용한 정적 파일(css / image) 다루기

### 1. 생성한 앱 폴더에 static 파일생성

<img src="README.assets/image-20221005170703635.png" alt="image-20221005170703635" style="zoom:150%;" />



### 2. 적용할 template에 주석 달기

```hmtl
{% load static %}

# static 이용하여 ulr 참조하기
{% static 'static 'css/style.css' %}
{% static 'images/h2.jpg' %}
```



![code](README.assets/code.png)



## template base.html 적용하기

### 1.  template폴더 생성하여 html 생성

> 경로는 보통 project안의 폴더로 생성한다.

<img src="README.assets/image-20221005172112333.png" alt="image-20221005172112333" style="zoom:150%;" />



### 2. project의 templates에 참조할 주소 입력

> 경로 확인 필수

![code1](README.assets/code1.png)



### 3. base.html

```
#block을 통해 다른 파일의 block 구간에 사용된다.
{block [name]}
.
.
.
{endblock}
```

![code2.](README.assets/code2..png)



### 4. html 파일에 적용

```html
{% extends 'base.html' %}

# css
{% block css %}
.
.
.
{% endblock %}

# body
{% block body%}
.
.
.
{% endblock %}
```



![code](README.assets/code.png)
