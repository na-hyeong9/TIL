from django.shortcuts import render

# Create your views here.
def index(request):
    # 요청을 index에 보낸다.
    return render(request, "practices/index.html")


def ping(request):
    return render(request, "practices/ping.html")


def pong(request):

    name = request.GET.get("peang")
    context = {"name": name}
    return render(request, "practices/pong.html", context)
