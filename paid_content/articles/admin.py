from django.contrib import admin

from .models import Article, User

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass