from ast import Num
from random import random
from django.shortcuts import render
import random
# Create your views here.

def oddeven(request, num):

    if (num % 2) == 0:
        oddeven = '짝수'
    if num == 0:
        oddeven = '0'
    if (num % 2) != 0:
        oddeven = '홀수'
        
    context = {
        'num' : num,
        'oddeven' : oddeven,
    }
    
    return render(request,'is-odd-even.html',context)  
 
def calculate(request, num1, num2):
    
    context = {
        'num1' : num1,
        'num2' : num2,
        'addnum' : num1 + num2,
        'minnum' : num1 - num2,
        'divnum' : num1 // num2,
        'mulnum' : num1 * num2,
    }
    return render(request, 'calculate.html',context)

def pl_form(request):
    return render(request, 'pl_form.html')

def pastLife(request):
    inputname = request.GET.get('inputname') 
    pastLifes = [
        {'name': '고양이', 'src':'https://t1.daumcdn.net/cfile/tistory/9982424C5F56648032'},
        {'name': '강아지', 'src':'https://images.mypetlife.co.kr/content/uploads/2021/10/19151330/corgi-g1a1774f95_1280-1024x682.jpg'},
        {'name': '들꽃', 'src':'https://www.jungto.org/upfile/image/dd18c83bff21556a845404d7bea61f2e.jpg'},
        {'name': '나무', 'src':'https://t1.daumcdn.net/cfile/tistory/994141415EE3015401'},
        {'name': '에디슨', 'src':'https://blog.kakaocdn.net/dn/cIlyCU/btqNDolEgGp/XMItujcup7kRWisxAmitu0/img.png'},
        {'name': '백설공주', 'src':'https://t1.daumcdn.net/thumb/R720x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/aRXQ/image/pSGrtnoPwyz7Qsshw6bwAeNGUvc.jpg'},
        {'name': '별', 'src':'https://www.sciencetimes.co.kr/wp-content/uploads/2018/02/%EC%9A%B0%EC%A3%BC%EC%9D%B8%EB%AC%B81.jpg'},
        {'name': '오리', 'src':'https://myanimals.co.kr/wp-content/uploads/2018/12/domestic-duck-species.jpg'},
        {'name': '미남', 'src':'https://img.insight.co.kr/static/2022/03/20/700/img_20220320103541_4t9j4217.webp'},
        {'name': '신데렐라', 'src':'https://t1.daumcdn.net/cfile/blog/274C524F561399AB30'},
        {'name': '난쟁이', 'src':'https://t1.daumcdn.net/cfile/tistory/121DE0504DBCBFB025'},
        {'name': '골룸', 'src':'http://ojsfile.ohmynews.com/STD_IMG_FILE/2015/1014/IE001881023_STD.jpg'},
         ]
        
    context = {
        'name' : inputname,
        'pastLife' : random.choice(pastLifes),
        
    }
    return render(request, 'pastLife.html', context)