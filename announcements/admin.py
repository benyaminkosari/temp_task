from django.contrib import admin
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at', 'is_accepted', 'views', 'author')
    list_filter = ('is_accepted', 'created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at', 'views', 'author')

admin.site.register(Announcement, AnnouncementAdmin)
