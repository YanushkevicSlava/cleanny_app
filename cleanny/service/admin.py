from django.contrib import admin
from .models import Worker
from django.utils.html import format_html


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'photo', 'show_photo')
    fields = ['last_name', 'first_name', 'email', 'photo']
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_photo.short_description = 'Фото'
