from django.shortcuts import render

# Create your views here.


def BlogIndex(request):
    return render(request, 'basic/index.html')
