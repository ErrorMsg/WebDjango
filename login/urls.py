from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
	path("reset/", views.reset, name="reset"),
    path("test/", views.test, name="test"),
    path("loveyoumicky/", views.love, name="love"),
	path("card/", views.card, name="card"),
]