from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    title= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200)
    class Meta :
        ordering = ['title']
        
    def __str__(self):
        return self.title
    
class Subject(models.Model):
    category=  models.ForeignKey('Category', related_name='catagory_sub', on_delete=models.SET_NULL, null= True)
    subject_outline= models.CharField(max_length=250)
    slug= models.SlugField(max_length= 250)
    
    def __str__(self):
        return self.subject_outline
    
class Course(models.Model):
    CHOICES= {
        ('Beginner', 'beginner'),
        ('Intermediate', 'intermediate'),
        ('Advanced', 'advanced'),
    }
    
    subject= models.ForeignKey('Subject', related_name='sub_course', on_delete=models.SET_NULL, null= True)
    teacher= models.ForeignKey(User, related_name='course_creator', on_delete=models.CASCADE)
    outline= models.CharField(max_length=200,blank=True, null=True)
    slug= models.SlugField(max_length=200 , unique=True)
    overview= models.TextField()
    syllabus= models.FileField()
    course_banner= models.ImageField()
    course_level=models.CharField(max_length=200 , choices= CHOICES, default='beginner')
    individual_price=models.IntegerField()
    created= models.DateTimeField(auto_now_add= True)
    
    class Meta:
        ordering= ['-created']
        
    def __str__(self):
        return self.outline
    
class Module(models.Model):
    course= models.ForeignKey(Course, related_name='module_course', on_delete=models.CASCADE)
    title= models.CharField(max_length=200,blank=True, null=True)
    description=  models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
    
class Content(models.Model):
    module= models.ForeignKey(Module, related_name='contents', on_delete= models.CASCADE)
    content_type= models.ForeignKey(ContentType, on_delete= models.CASCADE)
    
    object_id= models.PositiveIntegerField()
    item= GenericForeignKey('content_type', 'object_id')
    
class ItemBase(models.Model):
    teacher= models.ForeignKey(User, related_name=' %(course)s_related', on_delete=models.CASCADE)
    
    title= models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True)
    
    updated= models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True
        
    def __str__(self):
        return self.title
    
    
class Text(ItemBase):
    content= models.TextField()
    
class File(ItemBase):
    file= models.FileField(upload_to='files')
    
class Video(ItemBase):
    file= models.FileField(upload_to= 'videos')
    

    
    
    

    
    
    
    
    
    
    
    
    
    
    


    