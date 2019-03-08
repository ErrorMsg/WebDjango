from django.urls import path
from . import views

app_name = "cards"

urlpatterns = [
	path("test/", views.test, name="test"),
	path("index/", views.index, name="index"),
	path("card/<int:id>", views.card, name="card"),
	path("post/", views.post, name="post"),
]