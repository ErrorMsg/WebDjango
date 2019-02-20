from django.db import models

# Create your models here.
class Room(models.Model):
	topic = models.CharField(max_length=64, unique=True)
	members = models.IntegerField()
	ct_time = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.topic[:16]
	
	class Meta:
		ordering = ["ct_time"]
		
		
class Chats(models.Model):
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	user = models.ForeignKey("users.UserInfo", on_delete=models.CASCADE)
	said = models.CharField(max_length=256)
	said_time = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.said[:50]
		
	class Meta:
		ordering = ["said_time"]
				

class SyncRoom(models.Model):
	name = models.CharField(max_length=64, unique=True)
	label = models.SlugField(unique=True)
				
				
class Message(models.Model):
	room = models.ForeignKey(SyncRoom, related_name='messages', on_delete=models.CASCADE)
	handle = models.TextField()
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
	
	def __str__(self):
		return self.message[:50]
		
	class Meta:
		ordering = ["timestamp"]