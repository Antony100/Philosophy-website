from django.contrib import admin

from .models import Post, PostsInSession, Session, SessionEventDate


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'status', 'tag_list', 'id']
    list_filter = ['status', 'created']
    search_fields = ['title', 'body']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


    def tag_list(self, obj):
        return u", ".join(o for o in obj.tags.names())


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['created']
    search_fields = ['id', 'title']
    ordering = ['publish']


@admin.register(PostsInSession)
class PostInSessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'post_id', 'session', 'session_id', 'status']
    list_filter = ['created', 'session_id', 'post_id']
    search_fields = ['id', 'title', 'created', 'session_id', 'post_id']
    ordering = ['publish']

@admin.register(SessionEventDate)
class SessionEventAdmin(admin.ModelAdmin):
    list_display = ['event_date']
