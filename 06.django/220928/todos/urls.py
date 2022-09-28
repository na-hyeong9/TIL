from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path("", views.index, name="index"),
    path("table/", views.table, name="table"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
