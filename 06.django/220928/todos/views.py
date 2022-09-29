from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime
from django.utils.dateformat import DateFormat


# Create your views here.
def index(request):
    # 모든 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    todos = Todo.objects.all().order_by("priority")

    # 2. template에 보내준다.
    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


def table(request):
    # 1. parameter로 날라온 데이터를 받아서
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    # created_at = DateFormat(datetime.now()).format("Ymd")

    # 2. DB에 저장
    Todo.objects.create(
        content=content,
        priority=priority,
        deadline=deadline,
    )

    context = {
        "content": content,
        "priority": priority,
        "deadline": deadline,
    }

    return redirect("todos:index")


def edit(request, pk):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    todo = Todo.objects.get(pk=pk)
    context = {
        "todo": todo,
    }

    return redirect("todos:index")


def update(request, pk):
    todo = Todo.objects.get(id=pk)

    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    todo.content = content
    todo.priority = priority
    todo.deadline = deadline

    todo.save()

    return redirect("todos:index")


def delete(request, pk):
    # pk에 해당하는 글 삭제
    Todo.objects.get(id=pk).delete()

    return redirect("todos:index")
