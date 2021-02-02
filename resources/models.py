from django.db import models

# Create your models here.
from django.utils import timezone 

from django.contrib.auth.models import User

class Resource(models.Model):
    STATUS_CHOICES=(
        ('draft', 'Draft'),
        ('published','Published'),
    )
    title= models.CharField(max_length= 250)
    slug=  models.CharField(max_length= 250)
    author= models.ForeignKey(User, related_name='resource_author', on_delete=models.CASCADE)
    overview= models.TextField()
    publish= models.DateTimeField(default= timezone.now)
    created= models.DateTimeField(auto_now_add= True) 
    updated= models.DateTimeField(auto_now= True)
    status= models.CharField(max_length= 10, choices= STATUS_CHOICES, default= 'draft')
    
    class Meta:
        ordering= ('-publish',)
        
    def __str__(self):
        return self.title
    
    