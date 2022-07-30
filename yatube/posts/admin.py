from django.contrib import admin

from .models import Comment, Follow, Group, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'author', 'text', 'created')
    search_field = ('text', 'post')
    list_filter = ('created',)
    list_editable = ('post', 'author', 'text')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'author')
    list_editable = ('user', 'author')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', 'image')
    search_fields = ('text',)
    list_filter = ('pub_date', 'author', 'group')
    empty_value_display = '-пусто-'
    list_editable = ('text', 'author', 'group', 'image')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
