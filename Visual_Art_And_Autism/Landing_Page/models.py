from django.db import models

# Create your models here.

class FirstPage(models.Model):
    #inheritance = can be reused. 
    heading = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    #picture1 = 
class Introduction(models.Model):
    heading1= models.CharField(max_length=200)
    heading2 = models.CharField(max_length=200)
    description1= models.TextField(max_length=1000)
    heading3= models.CharField(max_length=200)
    description2 = models.TextField(max_length=1000)
class Classes(models.Model):
    heading1= models.CharField(max_length=200)