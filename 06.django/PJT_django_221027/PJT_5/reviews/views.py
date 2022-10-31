from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import Reviewform

# Create your views here.


def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = Reviewform(request.POST, request.FILES)
        # 유효성 검사
        if review_form.is_valid():
            article = review_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            article.user = request.user
            article.save()

            return redirect("reviews:index")
    else:
        review_form = Reviewform()
    context = {"review_form": review_form}
    return render(request, "reviews/create.html", context=context)
