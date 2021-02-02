from .models import Category, Subject , Course, Module, Video , Note
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = ['id', 'title', 'slug']
    
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fields = '__all__'
  


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields= '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields= '__all__'
  
        
        
class ModuleSerializer(serializers.ModelSerializer):
    videos= VideoSerializer(many=True, read_only= True)
    notes= NoteSerializer(many=True, read_only= True)
    class Meta:
        model = Module
        fields= ['id','title', 'description', 'videos', 'notes']

class CourseSerializer(serializers.ModelSerializer):
    modules= ModuleSerializer(many=True, read_only= True)
    class Meta:
        model= Course
        fields = ['id', 'subject', 'outline', 'slug', 'overview', 'syllabus', 'course_banner', 'course_level', 'individual_price', 'created', 'modules']

