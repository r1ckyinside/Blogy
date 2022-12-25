from django.contrib import admin
from .models import Newspaper


@admin.register(Newspaper)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
