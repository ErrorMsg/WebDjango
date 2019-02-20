from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Room, Chats, SyncRoom, Message
from users.models import UserInfo

# Create your views here.
def test(request, n=1):
	if request.method == "POST":
		topic = request.POST.get("roomtopic")
		return render(request, "chatroom/test.html", {"id":n, "topic":topic})
	return render(request, "chatroom/test.html", {"id":n})


def chat(request, n=1):
	if request.method == "POST": #chatting
		message = request.POST.get("message")
		room = Room.objects.get(pk=n)
		user = UserInfo.objects.get(name=request.session["user_name"])
		if message != "":
			chat = Chats(room=room, user=user, said=message)
			chat.save()
		chats = Chats.objects.filter(room=room).order_by("said_time")
		return render(request, "chatroom/chat.html", {"id":n, "topic":room.topic, "chats":chats})
	try:
		room = Room.objects.get(id=n)
		chats = Chats.objects.filter(room=room).order_by("said_time")
		return render(request, "chatroom/chat.html", {"id":n, "topic":room.topic, "chats":chats})
	except Room.DoesNotExist:
		raise Http404("no such room")
	except Chats.DoesNotExist:
		return render(request, "chatroom/chat.html", {"id":n, "topic":room.topic})
		
	
def rooms(request): #index room page
	if not request.session.get("is_login", None):
		warning = "Please login first!"
		return render(request, "chatroom/rooms.html", locals())
	if request.method == "POST":
		topic = request.POST.get("roomtopic")
		if topic.startswith("#"):
			try:
				id = int(topic[1:])
				room = Room.objects.get(pk=id)
				room.members += 1
				room.save()
				return HttpResponseRedirect(reverse("chatroom:chat", args=(id,)))
			except:
				warning = "Room number can't be found!"
				return render(request, "chatroom/rooms.html", {"warning":warning})
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
	
	
def chat_room(request, label):
	room, created = SyncRoom.objects.get_or_create(label=label)
	messages = reversed(room.messages.order_by('-timestamp')[:50])
	return render(request, "chatroom/syncroom.html", locals())