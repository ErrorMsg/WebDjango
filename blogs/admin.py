from django.contrib import admin
from .models import Blog, UserComments

class CommentInline(admin.TabularInline):
	model = UserComments
	ordering = ["-pub_time"]
	readonly_fields = (("user", "entry", "pub_time",))
	
class BlogAdmin(admin.ModelAdmin):
	inlines = [
		CommentInline,
	]

# Register your models here.
admin.site.register(Blog, BlogAdmin)