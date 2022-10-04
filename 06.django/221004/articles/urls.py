from django.urls import path
from articles import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    # form 사용
    # path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
]
