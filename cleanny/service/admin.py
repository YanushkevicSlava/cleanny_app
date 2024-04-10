from django.contrib import admin
from .models import Worker, Service, Order
from django.utils.html import format_html


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'photo', 'work_story', 'experience', 'show_photo')
    fields = ['last_name', 'first_name', 'email', 'work_story', 'experience', 'photo']
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_photo.short_description = 'Фото'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    fields = ['name', 'cost']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('cleaning_time', 'services', 'first_name', 'last_name', 'surname', 'email', 'tel', 'street',
                    'housing', 'home', 'flat', 'discount')
