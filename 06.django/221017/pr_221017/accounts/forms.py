from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:

        # get_user_model : 클래스
        model = get_user_model()
        fields = (
            "username",
            "password",
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


# 1. 모델(django modul) 불러오기
# 2. 받아온 모델을 폼으로 ... 사용 (커스텀)
# 3. get_user_model()
# 참조 https://velog.io/@duo22088/User-%EB%AA%A8%EB%8D%B8-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
