from django.contrib import admin

from checker.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'status_code')
    search_fields = ('url',)
    ordering = ('url',)
