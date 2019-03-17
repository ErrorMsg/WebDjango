from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
	path("index/", views.index, name="index"),
	path("article/<int:id>/", views.article, name="article"),
	path("post/", views.post, name="post"),
]