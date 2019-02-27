from django.shortcuts import render, reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from .models import Room, Chats, SyncRoom, Message
from users.models import UserInfo
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from dwebsocket.decorators import accept_websocket
import json


# Create your views here.
def test(request, n=1):
	if request.method == "POST":
		topic = request.POST.get("roomtopic")
		return render(request, "chatroom/test.html", {"id":n, "topic":topic})
	return render(request, "chatroom/test.html", {"id":n})

	
def chat(request, n=1):
	# if request.method == "POST": #chatting
		# message = request.POST.get("message")
		# room = Room.objects.get(pk=n)
		# user = UserInfo.objects.get(name=request.session["user_name"])
		# if message != "":
			# chat = Chats(room=room, user=user, said=message)
			# chat.save()
		# chats = Chats.objects.filter(room=room).order_by("said_time")
		# return render(request, "chatroom/chat.html", {"id":n, "topic":room.topic, "chats":chats})
	try:
		room = Room.objects.get(id=n)
		print("room: " + room)
		chats = Chats.objects.filter(room=room).order_by("-said_time")
		#return render(request, "chatroom/chat.html", {"id":n, "topic":room.topic, "chats":chats})
		return render(request, "chatroom/chat.html", {"id":n, "topic":room.topic})
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
	

@accept_websocket
def msg(request):
	print("websocket starts")
	if request.is_websocket():
		user = request.session.get("user_name", None)
		websocket = request.websocket
		if user is None:
			websocket.send(json.dumps({"code":400}))
		else:
			ws_message = websocket.read()
			if ws_message:
				message = json.loads(ws_message)
				message["code"] = 200
				room = Room.objects.get(pk=n)
				u = UserInfo.objects.get(name=request.session["user_name"])
				if message != "":
					chat = Chats.objects.create(room=room, user=user, said=message)
				message["user"] = user
				message["said_time"] = chat.said_time
				websocket.send(json.dumps(message))
				
		
@csrf_exempt
def post(request):
	if request.method == "POST":
		post_type = request.POST.get("post_type")
		if post_type == "send":
			message = request.POST.get("message")
			print(request.POST)
			if message != "":
				id = int(request.POST.get("room_id"))
				room = Room.objects.get(pk=id)
				user = UserInfo.objects.get(name=request.session["user_name"])
				chat = Chats.objects.create(room=room, user=user, said=message)
				#data = json.dumps(chat)
				return HttpResponse()
				#return HttpResponse(json.dumps(chat), content_type="application/json")
		elif post_type == "get":
			last_chat = int(request.POST.get("last_chat"))
			id = int(request.POST.get("room_id"))
			room = Room.objects.get(id=id)
			chats = Chats.objects.filter(room=room, id__gt=last_chat).order_by("said_time")
			data = serializers.serialize("json", chats)
			print(chats[0].user)
			return HttpResponse(data)
			#return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		raise Http404