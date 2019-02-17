from django.urls import path
from . import views

app_name = "cards"

urlpatterns = [
	path("test/", views.test, name="test"),
	path("card/", views.card, name="card"),
]