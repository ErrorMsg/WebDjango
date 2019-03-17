from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import ArticleBlog, ArticleComments
from users.models import UserInfo
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.forms.models import model_to_dict


div = 8

def index(request):
	articles = ArticleBlog.objects.all()
	if articles:
		return render(request, "blogs/index.html", locals())
	else:
		noarticle = True
		return render(request, "blogs/index.html", {"noarticle":noarticle})
	
def article(request, id):
	try:
		article = ArticleBlog.objects.get(pk=id)
	except:
		return Http404
	conmments = ArticleComments.objects.filter(blog=article).order_by("pub_time")
	pages = [p for p in range(len(comments)//(div+1)+1)]
	first_comments = comments[:div]
	return render(request, "blogs/article.html", {"id":id, "article":article, "uc":comments, "pages":pages})

# Create your views here.
@csrf_exempt
def post(request):
	if request.method == "POST":
		post_type = request.POST.get("post_type")
		if post_type == "send":
			entry = request.POST.get("comment")
			if entry != "":
				id = request.POST.get("article_id")
				blog = ArticleBlog.objects.get(pk=id)
				user = request.session.get("user_name", None)
				try:
					old_comments = ArticleComments.objects.filter(blog=blog,user=user,entry=entry)
					if datatime.datatime() - old_comments[-1].pub_time > 60:
						comment = ArticleComments.objects.create(blog=blog,user=user,entry=entry)
						comments = ArticleComments.objects.filter(blog=blog)
						last_comments = comments[len(comments)//div*div:]
						data = serializers.serialize("json", last_comments, use_natural_foreign_keys=True)
						return HttpResponse(data)
					else:
						return HttpResponse()
				except:
					comment = ArticleComments.objects.create(blog=blog,user=user,entry=entry)
					comments = ArticleComments.objects.filter(blog=blog)
					last_comments = comments[len(comments)//div*div:]
					data = serializers.serialize("json", last_comments, use_natural_foreign_keys=True)
					return HttpResponse(data)
			else:
				return HttpResponse()
		elif post_type == "get":
			pass
		elif post_type == "page":
			page = int(request.POST.get("page"))-1
			id = int(request.POST.get("article_id"))
			blog = ArticleBlog.objects.get(pk=id)
			comments = ArticleComments.objects.filter(blog=blog).order_by("pub_time")
			new_comments = comments[page*div:(page+1)*div]
			data = serializers.serialize("json", new_comments, use_natural_foreign_keys=True)
			return HttpResponse(data)
	else:
		return Http404