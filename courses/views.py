from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import generics 

from .models import Category, Subject, Course
from .serializers import CategorySerializer, SubjectSerializer, CourseSerializer


class CategoryListView(generics.ListAPIView):
    queryset= Category.objects.all()
    
    serializer_class= CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryDetailView(generics.RetrieveAPIView):
    queryset= Category.objects.all()
    serializer_class= CategorySerializer
    
class SubjectListView(generics.ListAPIView):
    queryset= Subject.objects.all()
    
    serializer_class= SubjectSerializer
    

class SubjectDetailView(generics.RetrieveAPIView):
    queryset= Subject.objects.all()
    serializer_class= SubjectSerializer
    


class CourseListView(generics.ListAPIView):
    queryset= Course.objects.all()
    
    serializer_class= CourseSerializer
    

class CourseDetailView(generics.RetrieveAPIView):
    queryset= Course.objects.all()
    serializer_class= CourseSerializer
    
