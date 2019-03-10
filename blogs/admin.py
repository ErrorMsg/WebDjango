from django.contrib import admin
from .models import ArticleBlog, CardBlog, ArticleComments, CardComments

class ArticleCommentInline(admin.TabularInline):
	model = ArticleComments
	ordering = ["-pub_time"]
	readonly_fields = (("user", "entry", "pub_time",))
	
class ArticleBlogAdmin(admin.ModelAdmin):
	list_display = ["topic", "short_description"]
	inlines = [
		ArticleCommentInline,
	]


class CardCommentInline(admin.TabularInline):
	model = CardComments
	ordering = ["-pub_time"]
	readonly_fields = (("user", "entry", "pub_time",))


class CardBlogAdmin(admin.ModelAdmin):
	inlines = [
		CardCommentInline,
	]

# Register your models here.
admin.site.register(ArticleBlog, ArticleBlogAdmin)
admin.site.register(CardBlog, CardBlogAdmin)