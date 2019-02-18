from django.shortcuts import render
from users.models import UserInfo
from blogs.models import Blog, UserComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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