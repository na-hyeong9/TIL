# django meta

> models.Model 클래스의 내부에 클래스를 배치

```python
from django.db import models


class Post(models.Model): 
    title = models.CharField(max_length=128)
    content = models.TextField() 

    # 이것 
    class Meta: 
        pass
```

- _아무것도 적용되지 않는 기본 문법_

  

### ordering 작성법

> 객체의 기본 정렬 방법을 변경할 때 사용

```python
from django.db import models

class Post(models.Model): 
    title = models.CharField(max_length=128)
    content = models.TextField() 

    class Meta: 
        # 오름차순 
        # ordering = ['title']

        # 내림차순 
        ordering  =  [ '-title' ]
```

- 하이픈 유무로 변경 (아래와 같이 출력된다.)

  'title'

  ```bash
  >>> Post.objects.all()
  <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>]>
  ```

  '-title'

  ```bash
  >>> Post.objects.all()
  <QuerySet [<Post: Post object (3)>, <Post: Post object (2)>, <Post: Post object (1)>]>
  ```

### db_table을 작성하는 방법

> db의 이름을 변경

```python
from django.db import models


class Post(models.Model): 
    no = models.IntegerField() 
    name = models.CharField( max_length = 128 )

    class Meta : 
        # 테이블 이름을 mypost로 변경 
        db_table = 'mypost'
```

- 위와 같이 정의하면 모델이 참조하는 테이블 이름이 설정 값으로 저장

- 변경 후 python manage.py makemigrations 실행하면 테이블 이름을 변경하는 마이그레이션 파일 생성

  => migrate를 실행 후 테이블 이름 변경

✔ migrate 필수



### verbose_name, verbose_name_plural을 작성법

> 관리 사이트의 모델의 표기 방법을 변경

```python
from django.db import models


class Post(models.Model): 
    title = models.CharField(max_length=128)
    content = models.TextField() 

    class Meta: 
        verbose_name = '포스트'  # 단수형 
        verbose_name_plural = '포스트 그룹'  # 복수형
 
```

- verbose_name == 모델 단수형 이름 지정
- verbose_name_plural == 모델 복수형 이름 지정

= > 관리 사이트에서 모델을 볼 때 참조
