from random import random
from unicodedata import name
from django.shortcuts import render
import random
# Create your views here.
def index(request):
    # 환영하는 페이지를 보여준다.

    names = ['김나형', '김단형', '김라형', '김비빅', '김밥']

    name = random.choice(names)

    context = {
        # 변수명: 값
        'name': name,
        'img' : 'https://post-phinf.pstatic.net/MjAyMDAzMDNfMTcg/MDAxNTgzMTkwNjA3ODQ5.kUXPHqGJ2xPDSu_3FiEoFC3kY9QyQ_g9CziCGrFSDuEg.LpCfOTbc5qth9d-GKzGv9jwj2VKhcqmPHp5cp1KJYEsg.JPEG/IM_food02.jpg?type=w1200',    
    }

    return render(request, 'index.html', context)


def welcome(request, name):
    #사람들이 /welcome/본인이름 을 입력하면, 환영 인사와 이름을 동시에 보여준다.
    context = {
        'name' : name,
        'greetings' : [
            '안녕하세요', 'hello', 'nihao', '안녕하세요르단' 
        ],
        'images' : [
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOc9RybR9H4toSFo1rD_8uWzc5zoT5H_vRUw&usqp=CAU',
            'https://shop1.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop1.daumcdn.net%2Fshophow%2Fp%2FL17896346500.jpg%3Fut%3D20220618033429',
            'http://imagescdn.gettyimagesbank.com/500/201510/a10288231.jpg',
            'https://post-phinf.pstatic.net/MjAyMDAzMDNfMTcg/MDAxNTgzMTkwNjA3ODQ5.kUXPHqGJ2xPDSu_3FiEoFC3kY9QyQ_g9CziCGrFSDuEg.LpCfOTbc5qth9d-GKzGv9jwj2VKhcqmPHp5cp1KJYEsg.JPEG/IM_food02.jpg?type=w1200',
        ]
    }
    return render(request, 'welcome.html', context)

def dinner(request):
    foods = ['김밥', '백순대', '삼겹살', '곱창', '샐러드', '굶기', '마라탕']
    foodsImg = [
            'https://i.pinimg.com/736x/e9/4f/c5/e94fc5631e6f40709adc7189a9456896.jpg',
            'https://d12zq4w4guyljn.cloudfront.net/20200425103822275_photo_35da6924a831.jpg',
            'https://post-phinf.pstatic.net/MjAyMDAzMDNfMTcg/MDAxNTgzMTkwNjA3ODQ5.kUXPHqGJ2xPDSu_3FiEoFC3kY9QyQ_g9CziCGrFSDuEg.LpCfOTbc5qth9d-GKzGv9jwj2VKhcqmPHp5cp1KJYEsg.JPEG/IM_food02.jpg?type=w1200',
            'https://cdn.imweb.me/thumbnail/20200602/10bbf2a2a65d0.jpg',
            'http://www.homecuisine.co.kr/files/attach/images/1462/071/011/32c4476fe171e8e9e06e172024185d84.JPG',
            'https://mblogthumb-phinf.pstatic.net/MjAyMDEwMDNfMjMz/MDAxNjAxNjYwMzI2NDQx.6FpzVHI50rEVzUsWAVBBXvGXmW3ol6X4P1l0wiMJQiUg.I6LNh53Nn0DPgZm-zd_-FoTe2TLI5IQdZq4cukbY3kwg.JPEG.bo752/1594461482406.jpg?type=w2',
            'https://image.wingeat.com/item/templates/3c00c09a19d6480d960720b544ec1939-w666-v2.jpg'
        ]

    food = random.choice(foods)
    i = foods.index(food)
    foodImg = foodsImg[i]

    context = {
        # 변수명: 값
        'food': food,
        'foodImg' : foodImg
    }

    return render(request, 'dinner.html',context)