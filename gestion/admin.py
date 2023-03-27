from django.contrib import admin
from .models import Category, Poll

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    fields = ('id', 'title')
admin.site.register(Category, CategoryAdmin)


class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    fields = ('title', 'description')
admin.site.register(Poll, PollAdmin)
