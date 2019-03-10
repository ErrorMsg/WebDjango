from django.db import models
from ckeditor.fields import RichTextField

blog_choices = (
	("article", "article"),
	("card", "card"),
)

# Create your models here.
class Blog(models.Model):
	topic = models.CharField(max_length=64, unique=True)
	ct_time = models.DateTimeField(auto_now_add=True)
	#type = models.CharField(max_length=10, choices=blog_choices)
	
	def __str__(self):
		return self.topic
	
	class Meta:
		abstract = True
		ordering = ["-ct_time"]


class ArticleBlog(Blog):
	mbody = RichTextField()
	type = "articleblog"

	def __str__(self):
		return self.topic

	def short_description(self):
		if len(self.mbody) > 100:
			return self.mbody[:100] + "..."
		else:
			return self.mbody


class CardBlog(Blog):
	type = "cardblog"

	def __str__(self):
		return self.topic


class ArticleComments(models.Model):
	blog = models.ForeignKey(ArticleBlog, on_delete=models.CASCADE)
	user = models.ForeignKey("users.UserInfo", on_delete=models.CASCADE)
	entry = models.CharField(max_length=1024)
	pub_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.entry[:50]

	class Meta:
		ordering = ["-pub_time"]

class CardComments(models.Model):
	blog = models.ForeignKey(CardBlog, on_delete=models.CASCADE)
	user = models.ForeignKey("users.UserInfo", on_delete=models.CASCADE)
	entry = models.CharField(max_length=1024)
	pub_time = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.entry[:50]
		
	class Meta:
		ordering = ["-pub_time"]