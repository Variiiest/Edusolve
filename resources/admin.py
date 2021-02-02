from django.contrib import admin

# Register your models here.
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display= ('title', 'slug', 'author','publish', 'status' )
    list_filter= ('status','publish', 'created', 'author')
    serch_fields= ('title', 'overview')
    prepopulated_fields= {'slug':('title',)}
    ordering= ('status', 'publish')
    