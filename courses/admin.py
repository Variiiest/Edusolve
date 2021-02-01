from django.contrib import admin
from .models import Category, Subject, Course, Module

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulted_fields ={'slug':('title',)}

@admin.register(Subject)  
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_outline',)
    prepopulted_fields ={'slug':('title','subject_outline')}
    
class ModuleInline(admin.StackedInline):
    model= Module
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display= ('subject', 'teacher', 'outline')
    list_filter= ['created', 'subject']
    search_fields=['outline','overview']
    prepopulted_fields= {'slug':{'outline'}}
    inlines= [ModuleInline]
