from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/pre_delete", views.pre_delete, name="pre_delete"),
    path("<int:pk>/delete", views.delete, name="delete"),
    path("<int:pk>/follow/", views.follow, name="follow"),
]
