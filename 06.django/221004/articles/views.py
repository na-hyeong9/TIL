from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    # 게시글 DB에서 가져온다.
    articles = Article.objects.order_by("-pk")
    # Template에 전달한다.
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


def new(request):
    return render(request, "articles/new.html")


def create(request):
    # DB에 저장하는 로직
    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # Article.objects.create(title=title, content=content)
    # return redirect("articles:index")
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        # 유효성 검사
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/new.html", context=context)


def detail(request, pk):

    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article_form = ArticleForm(instance=article)
    context = {"article_form": article_form}
    return render(request, "articles/update.html", context)
