from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import ArticleBlog, ArticleComments
from users.models import UserInfo
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.forms.models import model_to_dict


# Create your views here.
@csrf_exempt
def post(request):
    if request.method == "POST":
        post_type = request.POST.get("post_type")
        if post_type == "send":
            comment = request.POST.get("comment")
            if comment != "":
                id = int(request.POST.get("blog_id"))
                blog = ArticleBlog.objects.get(pk=id)
                user = UserInfo.objects.get(name=request.session["user_name"])
                entry = ArticleComments.objects.create(blog=blog, user=user, entry=comment)
                return HttpResponse

        elif post_type == "get":
            last_entry =  request.POST.get("last_entry")
            id = int(request.POST.get("blog_id"))
            blog = ArticleBlog.objects.get(pk=id)
            comments = ArticleComments.objects.filter(blog=blog, id__gt=id).order_by("pub_time")
            data = serializers.serialize("json", comments, user_natural_foreign_keys=True)
            return HttpResponse(data)

    else:
        return Http404