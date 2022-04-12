from django.shortcuts import render
import random

def make(count, lo_num):
    lotto_num = lo_num
    for _ in range(count):
        lotto_num.append(random.randint(1,45))
    ans_lotto= list(set(lotto_num))
    count=abs(len(ans_lotto)-6)
    if count == 0 :
        return ans_lotto
    else:
        return make(count, ans_lotto)

def lotto(request):
    lotto_num = []
    count = 6
    lotto_num = make(count, lotto_num)
    context_num = {'lotto_num' : lotto_num}
    return render(request, 'index.html', context_num)