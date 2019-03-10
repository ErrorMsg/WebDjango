from django.shortcuts import render
from django.http import Http404, HttpResponse
from users.models import UserInfo
from blogs.models import CardBlog, CardComments
from .models import HeroCard, BasicCard, EquipCard, WisdomCard, BadCard
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import datetime

div = 4

# Create your views here.
def init(): #add card into blog
	heros = HeroCard.objects.all()
	basics = BasicCard.objects.all()
	equips = EquipCard.objects.all()
	wisdoms = WisdomCard.objects.all()
	bads = BadCard.objects.all()
	if heros:
		for hero in heros:
			blog = CardBlog.objects.get_or_create(topic=hero.name, type="card")
	if basics:
		for basic in basics:
			blog = CardBlog.objects.get_or_create(topic=basic.name, type="card")
	if equips:
		for equip in equips:
			blog = CardBlog.objects.get_or_create(topic=equip.name, type="card")
	if wisdoms:
		for wisdom in wisdoms:
			blog = CardBlog.objects.get_or_create(topic=wisdom.name, type="card")
	if bads:
		for bad in bads:
			blog = CardBlog.objects.get_or_create(topic=wisdom.name, type="card")

def test(request):
	#init()
	t = [i+1 for i in range(6)]
	return render(request, "cards/test.html", {"pages":t})
	
def index(request):
	heros = HeroCard.objects.all()
	basics = BasicCard.objects.all()
	equips = EquipCard.objects.all()
	wisdoms = WisdomCard.objects.all()
	bads = BadCard.objects.all()
	if heros or basics or equips or wisdoms or bads:
		nocards = False
	return render(request, "cards/index.html", locals())

def card2(request, id):
	return HttpResponse(id)
	
def card(request, id):
	if id < 1:
		id = 1
	elif id > len(CardBlog.objects.all()):
		id = len(CardBlog.objects.all())
	try:
		blog = CardBlog.objects.get(pk=id)
	except:
		raise Http404
	if HeroCard.objects.filter(name=blog.topic):
		card = HeroCard.objects.get(name=blog.topic)
	elif BasicCard.objects.filter(name=blog.topic):
		card = BasicCard.objects.get(name=blog.topic)
	elif EquipCard.objects.filter(name=blog.topic):
		card = EquipCard.objects.get(name=blog.topic)
	elif WisdomCard.objects.filter(name=blog.topic):
		card = WisdomCard.objects.get(name=blog.topic)
	elif BadCard.objects.filter(name=blog.topic):
		card = BadCard.objects.get(name=blog.topic)
	#user = UserInfo.objects.get(pk=1)
	comments = CardComments.objects.filter(blog=blog).order_by("pub_time")
	# if request.method == "POST":
		# #names.append("new_user")
		# #comments.append(request.POST.get('comment'))
		# #return render(request, "cards/card.html", {'id':id, 'names':names, 'comments':comments})
		# entry = request.POST.get('comment')
		# #uc = CardComments.objects.create(blog=blog, user=user, entry=entry)
		# c = CardComments(blog=blog, user=user, entry=entry)
		# try:
			# old_c = CardComments.objects.filter(blog=blog, user=user, entry=entry)
			# if c.pub_time - old_c.pub_time > 3:
				# c.save()
				# return render(request, "cards/card.html", {"id":id, "uc":comments})
			# return
		# except:
			# c.save()
			# comments = CardComments.objects.order_by("pub_time")
			# paginator = Paginator(comments, 4)
			# try:
				# comments = paginator.page(page_num)
			# except PageNotAnInteger:
				# comments = paginator.page(1)
			# except EmptyPage:
				# comments = paginator.page(paginator.num_pages)
			# return render(request, "cards/card.html", {"id":id, "uc":comments})
	pages = [p for p in range(len(comments)//(div+1)+1)]
	first_comments = comments[:div]
	return render(request, "cards/card.html", {"id":id, "card":card, "uc":comments, "pages":pages})

@csrf_exempt
def post(request):
	if request.method == "POST":
		post_type = request.POST.get("post_type")
		if post_type == "send":
			entry = request.POST.get("comment")
			if entry != "":
				id = request.POST.get("card_id")
				blog = CardBlog.objects.get(pk=id)
				user = request.session.get("user_name", None)
				try:
					old_comments = CardComments.objects.filter(blog=blog,user=user,entry=entry)
					if datatime.datatime() - old_comments[-1].pub_time > 60:
						comment = CardComments.objects.create(blog=blog,user=user,entry=entry)
						comments = CardComments.objects.filter(blog=blog)
						last_comments = comments[len(comments)//div*div:]
						data = serializers.serialize("json", last_comments, use_natural_foreign_keys=True)
						return HttpResponse(data)
					else:
						return HttpResponse()
				except:
					comment = CardComments.objects.create(blog=blog,user=user,entry=entry)
					comments = CardComments.objects.filter(blog=blog)
					last_comments = comments[len(comments)//div*div:]
					data = serializers.serialize("json", last_comments, use_natural_foreign_keys=True)
					return HttpResponse(data)
			else:
				return HttpResponse()
		elif post_type == "get":
			pass
		elif post_type == "page":
			page = int(request.POST.get("page"))-1
			id = int(request.POST.get("card_id"))
			blog = CardBlog.objects.get(pk=id)
			comments = CardComments.objects.filter(blog=blog).order_by("pub_time")
			new_comments = comments[page*div:(page+1)*div]
			data = serializers.serialize("json", new_comments, use_natural_foreign_keys=True)
			return HttpResponse(data)
	else:
		return Http404