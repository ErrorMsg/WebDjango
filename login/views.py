from django.shortcuts import render, redirect
from users.models import UserInfo
from chatroom.models import Room
from .forms import UserForm, RegisterForm, AuthForm, ResetForm
import hashlib


def pw_encrypt(pw, k="pw_encrypt"):
	h = hashlib.sha256()
	pw = k + pw + k
	h.update(pw.encode())
	return h.hexdigest()

# Create your views here.
def index(request):
	pass
	return render(request, "login/index.html")


def login_origin(request, tried=1):
	if request.method == "POST":
		warning = "Please enter username and password!"
		username = request.POST.get("username")
		password = request.POST.get("password")
		if username and password:
			username = username.strip()
			try:
				user = UserInfo.objects.get(user=username)
				if user.pw == password:
					return redirect("/index/")
				else:
					warning = "Incorrect password!"
			except:
				warning = "Incorrect username!"
		return render(request, "login/login.html", {"warning":warning, "tried_times":tried})
	return render(request, "login/login.html")

def login(request):
	if request.session.get("is_login", None):
		return redirect("login:index")
	tried = request.session.get("tried_times", 1)
	if tried > 5:
		warning = "You have reach max tried times, please try again later!"
		login_form = UserForm()
		return render(request, "login/login.html", locals())
	if request.method == "POST":
		warning = "Please enter username and password!"
		login_form = UserForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data["username"]
			password = login_form.cleaned_data["password"]
			try:
				user = UserInfo.objects.get(name=username)
				#if user.pw == pw_encrypt(password):
				if user.pw == password:
					request.session["is_auth"] = True
					request.session["is_login"] = True
					request.session["user_id"] = user.id
					request.session["user_name"] = user.name
					request.session["tried_times"] += 1
					return redirect("login:index")
				else:
					warning = "Incorrect password!"
			except:
				warning = "Incorrect username!"
		return render(request, "login/login.html", locals())
	login_form = UserForm()
	request.session["tried_times"] = 0
	return render(request, "login/login.html", locals())

def register(request):
	if request.session.get("is_login", None):
		return redirect("login:index")
	if request.method == "POST":
		warning = "Please fill all informations!"
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			username = register_form.cleaned_data["username"]
			password1 = register_form.cleaned_data["password1"]
			password2 = register_form.cleaned_data["password2"]
			email = register_form.cleaned_data["email"]
			sex = register_form.cleaned_data["sex"]
			if password1 != password2:
				warning = "Passwords not match!"
				return render(request, "login/register.html", locals())
			else:
				user = UserInfo.objects.filter(name=username)
				if user:
					warning = "Username exists, please try another!"
					return render(request, "login/register.html", locals())
				mail = UserInfo.objects.filter(mail=email)
				if mail:
					warning = "Email exists, please try another!"
					return render(request, "login/register.html", locals())
			new_user = UserInfo.objects.create(name=username, pw=pw_encrypt(password), mail=email, sex=sex)
			#new_user.name = username
			#new_user.pw = password1
			#new_user.mail = email
			#new_user.sex = sex
			#new_user.save()
			return redirect("login:index")
	register_form = RegisterForm()
	return render(request, "login/register.html", locals())


def logout(request):
	if not request.session.get("is_login", None):
		return redirect("login:index")
	username = request.session.user_name
	rooms = Room.objects.filter(user=username)
	for room in rooms:
		room.member -= 1
		rooms.save()
	request.session.flush()
	return redirect("login:index")


def reset(request):
	if not request.session.get("is_auth", None):
		if request.method == "POST":
			auth_form = AuthForm(request.POST)
			if auth_form.is_valid():
				username = auth_form.cleaned_data["username"]
				email = auth_form.cleaned_data["email"]
				user = UserInfo.objects.get(name=username)
				if email != user.mail:
					warning = "Auth failed, username and email not match!"
					return render(request, "login/reset.html", locals())
				else:
					request.session["is_auth"] = True
					reset_form = ResetForm()
					return render(request, "login/reset.html", locals())
		else:
			warning = "Please login or authenticate first!"
			auth_form = AuthForm(request.POST)
			return render(request, "login/reset.html", locals())
	if request.method == "POST":
		reset_form = ResetForm(request.POST)
		if reset_form.is_valid():
			password0 = reset_form.cleaned_data["password0"]
			password1 = reset_form.cleaned_data["password1"]
			password2 = reset_form.cleaned_data["password2"]
			user = UserInfo.objects.get(name=request.session.user_name)
			if not request.session.get("is_login", None):
				if password1 == user.pw:
					warning = "New password same as current password!"
					return render(request, "login/reset.html", locals())
				elif password1 != password2:
					warning = "New password doesn't match!"
					return render(request, "login/reset.html", locals())
				else:
					user.pw = password1
					user.save()
					warning = "Password changed successfully!"
					return render(request, "login/reset.html", locals())
			if password0 == user.pw:
				if password0 == password1:
					warning = "New password same as current password!"
					return render(request, "login/reset.html", locals())
				elif password1 != password2:
					warning = "New password doesn't match!"
					return render(request, "login/reset.html", locals())
				else:
					user.pw = password1
					user.save()
					warning = "Password changed successfully!"
					return render(request, "login/reset.html", locals())
			else:
				warning = "Current password incorrect!"
				return render(request, "login/reset.html", locals())
	reset_form = ResetForm()
	return render(request, "login/reset.html", locals())
	
def test(request):
	pass
	return render(request, "login/cb.html")

def love(request):
	sweet = "Love you, Micky"
	return render(request, "login/love.html", locals())
	
def card(request, id=1):
	pass
	return render(request, "login/card.html", {'id':id})