from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("仮のトップページ")

def index(request):
    return render(request, "app/index.html")
