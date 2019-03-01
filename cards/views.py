from django.shortcuts import render
from django.http import Http404, HttpResponse
from users.models import UserInfo
from blogs.models import Blog, UserComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import datetime

# Create your views here.
def test(request):
	pass
	return render(request, "cards/cb.html")

def card(request, id=1):
	blog = Blog.objects.get(pk=id)
	user = UserInfo.objects.get(pk=1)
	comments = UserComments.objects.order_by("pub_time")
	if request.method == "POST":
		#names.append("new_user")
		#comments.append(request.POST.get('comment'))
		#return render(request, "cards/card.html", {'id':id, 'names':names, 'comments':comments})
		entry = request.POST.get('comment')
		#uc = UserComments.objects.create(blog=blog, user=user, entry=entry)
		c = UserComments(blog=blog, user=user, entry=entry)
		try:
			old_c = UserComments.objects.filter(blog=blog, user=user, entry=entry)
			if c.pub_time - old_c.pub_time > 3:
				c.save()
				return render(request, "cards/card.html", {'id':id, 'uc':comments})
			return
		except:
			c.save()
			comments = UserComments.objects.order_by("pub_time")
			paginator = Paginator(comments, 4)
			try:
				comments = paginator.page(page_num)
			except PageNotAnInteger:
				comments = paginator.page(1)
			except EmptyPage:
				comments = paginator.page(paginator.num_pages)
			return render(request, "cards/card.html", {'id':id, 'uc':comments})
	return render(request, "cards/card.html", {'id':id, 'uc':comments})

@csrf_exempt
def post(request):
	if request.method == "POST":
		post_type = request.POST.get("post_type")
		if post_type == "send":
			pass
		elif post_type == "get":
			pass
		elif post_type == "page":
			page = request.POST.get("page")*10
			id = int(request.POST.get("card_id"))
			blog = Blog.objects.get(pk=id)
			comments = UserComments.objects.filter(blog=blog, id__gt=page).order_by("pub_time")
			data = serializers.serialize("json", comments, user_natural_foreign_keys=True)
			return HttpResponse(data)
	else:
		return Http404