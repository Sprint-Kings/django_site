from django.shortcuts import render

def base(request):
    return render(request, 'supermegasite/base.html')

def shop(request):
    return render(request, 'supermegasite/shop.html')



