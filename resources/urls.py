from django.urls import path 

from .import views 
urlpatterns=[
    path('resources/', views.ResourceListView.as_view(), name= 'resource_list'),
    path('resources/<pk>/', views.ResourceDetailView.as_view(), name= 'resource_detail'),
    
]