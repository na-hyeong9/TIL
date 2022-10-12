from django.shortcuts import render, redirect

# (views.py 내 정의한 함수 login과 구분하기 위해 auth_log로 재 명명함)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm

from django.contrib.auth.forms import AuthenticationForm

# from .models import User
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {"user": user}
    return render(request, "accounts/detail.html", context)


def login(request):
    # AuthenticationForm 폼에 저장된 정보 검증
    form = AuthenticationForm()
    if request.method == "POST":
        # AuthenticationForm은 ModelForm이 아님!
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("articles:index")
