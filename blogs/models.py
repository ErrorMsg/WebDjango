from django.db import models

# Create your models here.
class Blog(models.Model):
	topic = models.CharField(max_length=64, unique=True)
	ct_time = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.topic
	
	class Meta:
		ordering = ["-ct_time"]

class UserComments(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	user = models.ForeignKey("users.UserInfo", on_delete=models.CASCADE)
	entry = models.CharField(max_length=1024)
	pub_time = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.entry[:50]
		
	class Meta:
		ordering = ["-pub_time"]