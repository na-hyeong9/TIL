from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def index(request):
    # 게시글 DB에서 가져온다.
    articles = Article.objects.order_by("-pk")
    # Template에 전달한다.
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


def new(request):
    return render(request, "articles/form.html")


@login_required
def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST, request.FILES)
        # 유효성 검사
        if article_form.is_valid():
            article_form.save()
            messages.success(request, "글 작성이 완료되었습니다.")

            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context=context)


def detail(request, pk):

    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
            messages.success(request, "글이 수정되었습니다.")
            return redirect("articles:detail", article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context)


def delete(request, pk):
    Article.objects.get(pk=pk).delete()

    return redirect("articles:index")
