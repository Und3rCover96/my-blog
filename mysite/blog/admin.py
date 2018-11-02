from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers
from .models import *

# Register your models here.
myModels=[Post]
###############################################################################
def export_as_json(ModelAdmin,request,queryset):
    response = HttpResponse(content_type = "application/json")
    serializers.serialize("json", queryset,stream=response)
    return response

export_as_json.short_description='Mark selected as json'
###############################################################################
def make_published(ModelAdmin,request,queryset):
    result=queryset.update(status = 'published')
    if result == 1:
        message_bit = "One post was"
    else:
        message_bit = "{} posts were".format(result)

    ModelAdmin.message_user(request,"{} Sucessfully marked as published".format(message_bit))


make_published.short_description = 'Mark selected posts as published'
###############################################################################
def make_draft(ModelAdmin,request,queryset):
    result=queryset.update(status = 'draft')
    if result == 1:
        message_bit = "One post was"
    else:
        message_bit = "{} posts were".format(result)

    ModelAdmin.message_user(request,"{} Sucessfully marked as draft".format(message_bit))

make_draft.short_description = 'Mark selected posts as darfts'

###############################################################################
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('publish','status')
    list_display = ('title', 'publish','status')
    search_fields = ('title', 'body')
    actions = [make_published, make_draft,export_as_json]


###############################################################################
admin.site.register(myModels, PostAdmin)
