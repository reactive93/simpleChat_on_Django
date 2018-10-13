from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from chat.models import Post


class PostInline(admin.StackedInline):
    model = Post
    can_delete = False
    verbose_name_plural = 'Post'


class UserAdmin(BaseUserAdmin):
    inlines = (PostInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)