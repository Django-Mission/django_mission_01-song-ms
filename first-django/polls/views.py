from django.shortcuts import render
import random

def index(request):
    foods = ['apple', 'banana', 'coconut', ]
    info = {
       'name': 'Harry'
    }
    context = {
        'info': info,
        'foods': foods,
    }
    # lotto_num = []
    # for _ in range(7):
    #     lotto_num.append(random.randint(1,45))
    # random.sample(lotto_num,7)
    return render(request, 'templates/index.html', context)