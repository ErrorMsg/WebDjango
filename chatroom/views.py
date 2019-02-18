from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Room, Chats

# Create your views here.
def test(request, n=1):
	if request.method == "POST":
		topic = request.POST.get("roomtopic")
		return render(request, "chatroom/test.html", {"id":n, "topic":topic})
	return render(request, "chatroom/test.html", {"id":n})


def chat(request, n=1):
	if request.method == "POST": #chatting
		pass
	
	try:
		room = Room.objects.get(id=n)
		chats = Chats.objects.filter(room=room).order_by("said_time")
		return render(requets, "chatroom/chat.html", {"id":n, "topic":room.topic, "chats":chats})
	except:
		raise Http404("no such room")
	
def rooms(request): #index room page
	if not request.session.get("is_login", None):
		warning = "Please login first!"
		return render(request, "chatroom/rooms.html", locals())
	if request.method == "POST":
		topic = request.POST.get("roomtopic")
		try:
			room = Room.objects.get(topic=topic)
			room.members += 1
			room.save()
			return HttpResponseRedirect(reverse("chatroom:chat", args=(room.id,)))
		except:
			room = Room.objects.create(topic=topic, members=1)
			return HttpResponseRedirect(reverse("chatroom:chat", args=(room.id,)))
	rooms = Room.objects.all().order_by("ct_time")
	return render(request, "chatroom/rooms.html")