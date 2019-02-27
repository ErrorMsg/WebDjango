from django.urls import path
from . import views


app_name = 'chatroom'
urlpatterns = [
	path("test/<int:n>", views.test, name="test"),
	path("rooms/", views.rooms, name="rooms"),
	path("room/<int:n>", views.chat, name="chat"),
	path("post/", views.post, name="post"),
]