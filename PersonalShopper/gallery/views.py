from django.shortcuts import render


# Create your views here.

def bags(request):
    return render(request, 'gallery/bags.html')

def dress(request):
    return render(request, 'gallery/dress.html')

def shoes(request):
    return render(request, 'gallery/shoes.html')
