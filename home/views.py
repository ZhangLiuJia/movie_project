from django.shortcuts import render, redirect
from models import models


def index(request, *args, **kwargs):
    return render(request, "home/index.html")


def animation(request):
    return render(request, "home/animation.html")


def login(request):
    print("asdfasfasdfas")
    return render(request, "home/login.html")


def logout(request):
    return redirect("/i/login")


def register(request):
    return render(request, "home/register.html")


def user(request):
    return render(request, "home/user.html")


def pwd(request):
    return render(request, "home/pwd.html")

def coments(request):
    return render(request, "home/comments.html")

def loginlog(request):
    return render(request, "home/loginlog.html")


def moviecol(request):
    return render(request, "home/moviecol.html")


def search(request):
    return render(request, "home/search.html")


def play(request):
    return render(request, "home/play.html")
