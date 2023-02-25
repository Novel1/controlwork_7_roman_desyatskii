from django.contrib import admin

from webapp.models import GuestBook


# Register your models here.


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'author', 'text', 'status', 'created_at')
    list_filter = ('id', 'email', 'author', 'text', 'status', 'created_at')
    search_fields = ('email', 'author', 'text', 'status')
    fields = ('email', 'author', 'text', 'status', 'created_at')
    readonly_fields = ('id', 'created_at')


admin.site.register(GuestBook, ToDoAdmin)
