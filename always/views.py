from django.shortcuts import render, redirect
from .form import UserForm
from models import models


def auth_login(func):
    def inner(request, *args, **kwargs):

        try:
            request.session["user"]["username"]
            return func(request, *args, **kwargs)
        except Exception as e:
            return redirect("/always/login?next=%s" % request.path_info)

    return inner


def login(request):
    error_info = {"errors": None}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = models.Admin.objects.filter(username=username, password=models.get_pwd(username, password)).first()
        if user_obj:
            request.session["user"] = {"id": user_obj.id, "username": user_obj.username}
            return redirect(request.GET.get("next") or "/always/index.html")
        error_info["errors"] = True
        error_info['username'] = username
        error_info['password'] = password

    form_obj = UserForm()
    context = {
        "form_obj": form_obj
    }
    context.update(error_info)

    return render(request, "admin/login.html", context)


def logout(request):
    request.session.pop("user", None)
    return redirect("/always/login")


@auth_login
def pwd(request):

    context = {
        "new_error": False,
        "old_error": False,
        "success": False
    }
    if request.method == "POST":
        username = request.session["user"]["username"]
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        user_obj = models.Admin.objects.filter(username=username, password=models.get_pwd(username, old_password)).first()
        if user_obj:
            if len(new_password) < 5:
                context["new_error"] = True
            else:
                user_obj.password = models.get_pwd(username, new_password)
                user_obj.save()
        else:
            context["old_error"] = True
        if not any(context.values()):
            context["success"] = True

    return render(request, "admin/pwd.html", context)


@auth_login
def index(request):
    return render(request, "admin/index.html")


@auth_login
def tag_add(request):
    context = {
        "success": False,
        "message": ""
    }
    if request.method == "POST":
        tag_name = request.POST.get("tag_name")
        if models.Tag.objects.filter(name=tag_name).first():
            context["message"] = "该标签已存在。。。。。"
        else:
            models.Tag.objects.create(name=tag_name)
            context["success"] = True

    return render(request, "admin/tag_add.html", context)


@auth_login
def tag_list(request):
    return render(request, "admin/tag_list.html")


@auth_login
def movie_add(request):
    return render(request, "admin/movie_add.html")


@auth_login
def movie_list(request):
    return render(request, "admin/movie_list.html")


@auth_login
def preview_add(request):
    return render(request, "admin/preview_add.html")

@auth_login
def preview_list(request):
    return render(request, "admin/preview_list.html")

@auth_login
def user_list(request):
    return render(request, "admin/user_list.html")

@auth_login
def user_view(request):
    return render(request, "admin/user_view.html")

@auth_login
def comment_list(request):
    return render(request, "admin/comment_list.html")

@auth_login
def moviecol_list(request):
    return render(request, "admin/moviecol_list.html")

@auth_login
def oplog_list(request):
    return render(request, "admin/oplog_list.html")

@auth_login
def adminloginlog_list(request):
    return render(request, "admin/adminloginlog_list.html")

@auth_login
def userloginlog_list(request):
    return render(request, "admin/userloginlog_list.html")

@auth_login
def auth_add(request):
    return render(request, "admin/auth_add.html")

@auth_login
def auth_list(request):
    return render(request, "admin/auth_list.html")

@auth_login
def role_add(request):
    return render(request, "admin/role_add.html")

@auth_login
def role_list(request):
    return render(request, "admin/role_list.html")

@auth_login
def admin_add(request):
    return render(request, "admin/admin_add.html")

@auth_login
def admin_list(request):
    return render(request, "admin/admin_list.html")
