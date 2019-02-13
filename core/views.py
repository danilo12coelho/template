from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html', )


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def forgot(request):
    return render(request, 'forgot-password.html')


def erro(request):
    return render(request, '404.html')


def base(request):
    return render(request, 'base.html')


def blanck(request):
    return render(request, 'blank.html')


def tables(request):
    return render(request, 'tables.html')
