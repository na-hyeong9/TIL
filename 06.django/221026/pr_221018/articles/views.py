import imp
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm, PostSearchForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView
from django.db.models import Q
from django.http import JsonResponse


# Create your views here.


def index(request):
    articles = Article.objects.order_by("-pk")
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST, request.FILES)
        # 유효성 검사
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            article.user = request.user
            article.save()

            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        "article": article,
        # 역참조 (article에 포함된 comment data를 전부 불러온다.)
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article_form.save()
                return redirect("articles:detail", article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {"article_form": article_form}
        return render(request, "articles/form.html", context)
    else:
        messages.warning(request, "작성자만 수정할 수 있습니다.")
        return redirect("articles:detail", article.pk)


@login_required
def delete(request, pk):
    Article.objects.get(pk=pk).delete()

    return redirect("articles:index")


@login_required
def comment_create(request, pk):
    # 특정 게시물 가져오기
    article = Article.objects.get(pk=pk)
    # comment 폼 가져오기
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect("articles:detail", article.pk)


@login_required
def comment_update(request, pk):
    if request.method == "POST":
        # 특정 게시물 가져오기
        article = Article.objects.get(pk=pk)
        comment_update = article.comment_set.all()
        # comment 폼 가져오기
    return redirect("articles:detail", article.pk)


@login_required
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect("articles:detail", article_pk)


@login_required
def like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in article.like_users.all(): 
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가하고 
        article.like_users.add(request.user)
        is_liked = True
    # 상세 페이지로 redirect
    context = {'isLiked': is_liked, 'likeCount': article.like_users.count()}
    return JsonResponse(context)
