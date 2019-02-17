from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
	path("", views.poll, name ='poll'),
	path("search-form/", views.search_form, name='search_form'),
	path("search", views.search, name='search'),
	path("search-post/", views.search_post, name='search_post'),
	path("<int:question_id>/", views.detail, name='detail'),
	path("<int:question_id>/results/", views.results, name='results'),
	path("<int:question_id>/vote/", views.vote, name='vote'),
    path("test/<path:p>", views.test, name='test'),
    #url(r'^post/(?P<pk>\d+)$', views.xxx, name='xxx'),
    #path('post/<int:pk>', views.xxx, name='xxx'),
    #url(r'^article/(?P<year>[0-9]{4})/$', view.xxx),
    #path('article/<int:year>/', views.xxx),
	
	path("chatroom/<int:n>", views.chatroom, name="chatroom"),
]