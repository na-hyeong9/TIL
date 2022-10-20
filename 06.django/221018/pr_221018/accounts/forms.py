from django.forms import ModelForm
from django.contrib.auth.models import User  # django에서 기본 제공하는 model이 있음.

from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:

        # get_user_model : 클래스
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "email",
        )


class SignupForm(ModelForm):  # 회원가입을 제공하는 class이다.

    username = forms.CharField(
        max_length=20,
        min_length=6,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        max_length=16,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "8글자 이상, 16글자 이하로 작성해주세요."}
        ),
    )
    password_confirm = forms.CharField(
        max_length=16,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "8글자 이상, 16글자 이하로 작성해주세요."}
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    field_order = [
        "username",
        "password",
        "password_confirm",
        "last_name",
        "first_name",
        "email",
    ]
    # field_order는 만들어지는 입력양식의 순서, password 바로 밑에 password_check 양식을 추가하기 위해 사용

    class Meta:
        model = User
        widgets = {"password": forms.PasswordInput}
        fields = ["username", "password", "last_name", "first_name", "email"]


# User model에 정의된 username, passwordm last_name, first_name, email을 입력양식으로


class LoginForm(ModelForm):
    username = forms.CharField(
        max_length=20,
        min_length=6,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        max_length=16,
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = User
        widgets = {"password": forms.PasswordInput}
        fields = ["username", "password"]
