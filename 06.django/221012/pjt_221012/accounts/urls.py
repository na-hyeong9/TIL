from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("<int:pk>/", views.detail, name="detail"),
    path("logout/", views.logout, name="logout"),
]
