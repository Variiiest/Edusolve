from django.shortcuts import render
from rest_framework import generics 

from .models import Resource
from .serializers import ResourceSerializer


class ResourceListView(generics.ListAPIView):
    queryset=Resource.objects.all()
    
    serializer_class= ResourceSerializer
    

class ResourceDetailView(generics.RetrieveAPIView):
    queryset= Resource.objects.all()
    serializer_class=ResourceSerializer