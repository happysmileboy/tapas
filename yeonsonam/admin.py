from django.contrib import admin

from .models import *
# Register your models here.



@admin.register(Drama2)
class Drama2Admin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end', 'state', 'pk')
    ordering = ['start']
    search_fields = ['title']