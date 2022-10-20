from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    articles = Article.objects.order_by("-pk")
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST, request.FILES)
        # 유효성 검사
        if article_form.is_valid():
            article_form.save()

            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context=context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:detail", article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context)


def delete(request, pk):
    Article.objects.get(pk=pk).delete()

    return redirect("articles:index")
