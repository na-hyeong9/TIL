from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.


def index(request):
    # 게시글 DB에서 가져온다.
    movies = Movie.objects.all()
    # Template에 전달한다.
    context = {
        "movies": movies,
    }
    return render(request, "movie/index.html", context)


def new(request):
    return render(request, "movie/new.html")


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        movie_form = MovieForm(request.POST)
        # 유효성 검사
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movie:index")
    else:
        movie_form = MovieForm()
    context = {"movie_form": movie_form}
    return render(request, "movie/new.html", context=context)


def detail(request, pk):

    movie = movie.objects.get(pk=pk)
    context = {"movie": movie}
    return render(request, "movie/detail.html", context)


def update(request, pk):
    movie = movie.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            movie_form.save()
            return redirect("movie:detail", movie.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 movie_form을 랜더링
    else:
        # GET : Form을 제공
        movie_form = MovieForm(instance=movie)
    context = {"movie_form": movie_form}
    return render(request, "movie/update.html", context)


def delete(request, pk):
    # pk에 해당하는 글 삭제
    Movie.objects.get(pk=pk).delete()

    return redirect("movie:index")
