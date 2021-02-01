from django.urls import path 

from .import views 
urlpatterns=[
    path('categories/', views.CategoryListView.as_view(), name= 'category_list'),
    path('category/<pk>/', views.CategoryDetailView.as_view(), name= 'category_detail'),
    path('subjects/', views.SubjectListView.as_view(), name= 'subject_list'),
    path('subject/<pk>/', views.SubjectDetailView.as_view(), name= 'subject_detail'),
    path('courses/', views.CourseListView.as_view(), name= 'subject_list'),
    path('course/<pk>/', views.CourseDetailView.as_view(), name= 'subject_detail'),
] 

