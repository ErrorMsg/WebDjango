from django.http import HttpResponse
from django.shortcuts import render

user_list = []


def hello(request):
    # return HttpResponse("hello world test")
    if request.method == "POST":
        user = request.POST['ur']
        pw = request.POST['pw']
        user_list.append({user: pw})
        context = {"title": "new", "name": user + ": " + pw, "data": user_list}
    else:
        context = {"title": "new", "data": []}
    return render(request, 'hello.html', context)


def index(request):
    # return HttpResponse("this is index")
    context = {"info": "please enter first: "}
    return render(request, 'index.html', context)
