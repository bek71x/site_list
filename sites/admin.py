from django.contrib import admin

from sites.models import Site
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','site', 'body','created')
    list_filter = ('user','site')
    actions = ['enable_comments','disable_comments']

    def enable_comments(self,request,queryset):
        queryset.update(active = True)


    def disable_comments(self,request,queryset):
        queryset.update(active=False)


admin.site.register(Site)
admin.site.register(Comment, CommentAdmin)