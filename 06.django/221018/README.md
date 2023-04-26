# django CRUD

## like & follow









### 1. 사전 설정

settings.py에 MEDIA_ROOT를 다음과 같이 설정

```py
MEDIA_URL='/image/' #미디어 파일을 불러올 때 사용할 가상 url을 설정한다.

MEDIA_ROOT=BASE_DIR / 'media' #기본프로젝트 하위의 media에서 모든 업로드 매체를 관리한다.
#media 하위에 앱이름으로 디렉터리를 만들고 파일을 업로드하게 된다.

# INSTALLED_APPS 하위에 'imagekit' 추가
```

💡 MEDIA_URL

​	각 media 파일에 대한 **URL Prefix**. 필드명. url 속성에 의해서 참조되는 설정.

💡 MEDIA_ROOT

​	파일필드를 통한 저장 시에, **실제 파일을 저장할 ROOT 경로**.



### 2. models.py

- 작성 코드

  ```py
  from imagekit.models import ProcessedImageField
  from imagekit.processors import ResizeToFill
  
  class Article(models.Model):
  	image = ProcessedImageField(
          upload_to="images/%Y/%m/%d",
          null=True,
          blank=True,
          processors=[ResizeToFill(400, 300)],
          format="JPEG",
          options={"quality": 80},
      )
  ```

  

- 전체 코드

  ```py
  from pickle import TRUE
  from django.db import models
  from imagekit.models import ProcessedImageField
  from imagekit.processors import ResizeToFill
  
  # Create your models here.
  
  
  class Article(models.Model):
      # 제목 글자 수 제한
      title = models.CharField(max_length=20)
      # 내용
      content = models.TextField()
      # 작성 시간
      created_at = models.DateTimeField(auto_now_add=True)
      # 수정 시간
      updated_at = models.DateTimeField(auto_now=True)
      # 이미지
      image = ProcessedImageField(
          #setting 값에 지정된 상대경로를 사용하기 위해 경로 처음엔 /를 두지 않는다.
          upload_to="images/", 
          null=True,
          blank=True,
          processors=[ResizeToFill(400, 300)],
          format="JPEG",
          options={"quality": 80},
      )
  ```

  

💡 _upload_to_

​	저장할 경로를 설정하는 용도

💡 _ResizeToFill_

​	해당 크기에 채워 리사이징.(넘친 부분 잘라 크기 통일)



✔ __보고 넘어가기__

__활용 1.__ _ImageSpecField_

원본 ImageFiled로 부터 생성  (원본x, 썸네일o)

__활용 2.__ _ProcessedImageField_

원본 이미지를 재가공하여 저장 (원본x, 썸네일o)

__활용 3__. _템플릿에서 이미지 직접 처리_





### 3.templates (index.html/ detail.html)

- 변경 코드

  ```html
  ========================= index.html =========================
  
  {% for article in articles %}
              <div class="col-3">
                  <div class="card">
                      <img src="{{ article.image.url }}" 
                           class="card-img-top" alt="{{ article.title }}">
                      <div class="card-body">
                          <h5 class="card-title">
                              <a href="{% url 'articles:detail' article.pk %}">
                                  {{ article.title }}</a>
                          </h5>
                      </div>
                  </div>
              </div>
  {% endfor %}
  
  ========================= detail.html =========================
  
  {% if article.image %}
  <img src="{{ article.image.url }}" alt="{{ article.image }}" width="400" height="300">
  {% endif %}
  ```

  

- 전체 코드

  ```py
  ========================= index.html =========================
  
  % extends 'base.html' %}
  {% load static %}
  {% load django_bootstrap5 %}
  {% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  {% endblock %}
  
  
  {% block body%}
  <div class="container">
  
      <div class=" my-3 d-flex justify-content-end">
          <a class="" href="{% url 'articles:create' %}">작성하기</a>
      </div>
      <div>
          <div class="row row-cols-1 row-cols-md-3 g-4">
              {% for article in articles %}
              <div class="col-3">
                  <div class="card">
                      <img src="{{ article.image.url }}" class="card-img-top" alt="{{ article.title }}">
                      <div class="card-body">
                          <h5 class="card-title"><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a>
                          </h5>
                      </div>
                  </div>
              </div>
              {% endfor %}
          </div>
  
      </div>
  </div>
  {% endblock %}
  
  ========================= detail =========================
  
  {% extends 'base.html' %}
  {% load static %}
  {% load django_bootstrap5 %}
  {% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  {% endblock %}
  
  
  {% block body %}
  <div class="my-3 d-flex justify-content-end">
      <a href="{% url 'articles:index' %}">목록으로 돌아가기</a>
  </div>
  <h1 class="my-5"> {{ article.pk }}번 게시글</h1>
  <p>{{ article.created_at|date:"SHORT_DATETIME_FORMAT" }} | {{ article.updated_at|date:"y-m-d D" }}</p>
  {% if article.image %}
  <img src="{{ article.image.url }}" alt="{{ article.image }}" width="400" height="300">
  {% endif %}
  <p>{{article.content}}</p>
  <div class="my-3 d-flex justify-content-end">
      <a class="btn btn-link" href="{% url 'articles:update' article.pk %}">수정하기</a>
      <a class="btn btn-link" data-bs-toggle="modal" data-bs-target="#deleteModal">
          삭제
      </a>
  
      <!-- Modal -->
      <div class="modal fade" id="deleteModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
          aria-labelledby="deleteModalLabel" aria-hidden="true">
          <div class="modal-dialog">
              <div class="modal-content">
                  <div class="modal-header">
                      <h1 class="modal-title fs-5" id="deleteModalLabel">정말 삭제하시겠습니까?</h1>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                      작성했던 글이 삭제됩니다.
                  </div>
                  <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                      <a href="{% url 'articles:delete' article.pk %}" class="btn btn-primary">삭제하기</a>
                  </div>
              </div>
          </div>
      </div>
  </div>
  
  {% endblock %}
  ```



image 속성 하위엔 url 속성이 있어 이를 통해 이미지를 가져온다. >> `{{ article.image.url }}`



### 4. urls.py (라우팅)



```py
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



🎈 __참고 출처__

-  https://wayhome25.github.io/django/2017/05/10/media-file/

- https://velog.io/@duo22088/Django-Media-file-%EB%8B%A4%EB%A3%A8%EA%B8%B0