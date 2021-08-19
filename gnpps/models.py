from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to="img/%y")

class services(models.Model):
    
    caption=models.CharField(max_length=20)
    details=models.TextField(max_length=300, default='some_value')
    picture=models.ImageField(upload_to="img/%y", default='default.jpg')
    
    
    
    def __str__(self):
        return self.caption 
        
class faq(models.Model):
    question=models.CharField(max_length=300)
    answer=models.TextField(max_length=2000)
    
