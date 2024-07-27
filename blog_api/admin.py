from django.contrib import admin
from .models import *

# Register your models here.

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}



admin.site.register(Category)
admin.site.register(blog,blogAdmin)
