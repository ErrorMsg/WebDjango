from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    pass
    return render(request, "login/index.html")


def login(request):
    pass
    return render(request, "login/login.html")


def register(request):
    pass
    return render(request, "login/register.html")


def logout(request):
    pass
    # return redirect("login:index")
    return render(request, "login/base.html")


def test(request):
    pass
    return render(request, "login/cb.html")

def love(request):
    pass
    return render(request, "login/love.html")