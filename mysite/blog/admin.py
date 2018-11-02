from django.contrib import admin
from .models import *

# Register your models here.
myModels=[Post]
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('publish','status')
    search_fields = ('title', 'body')

admin.site.register(myModels, PostAdmin)
