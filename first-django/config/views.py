from django.shortcuts import render
import random

def lotto(request):
    lotto_num = []
    for _ in range(6):
        lotto_num.append(random.randint(1,45))
    context_num = {'lotto_num' : lotto_num}
    return render(request, 'index.html', context_num)