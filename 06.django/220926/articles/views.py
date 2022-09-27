from django.shortcuts import render

from PJT220926.settings import BASE_DIR
from articles.models import Articles

# guestbook = []

# Create your views here.
def index(request):
    # print(BASE_DIR)
    # DB에서 가져오기
    guestbook = Articles.objects.all()
    # SELECT * FROM articles;

    return render(request, "articles/index.html", {"guestbook": guestbook})


def create(request):
    content = request.GET.get("content")
    # guestbook.append(content)
    # DB에 저장
    Articles.objects.create(content=content)

    return render(request, "articles/create.html", {"content": content})
