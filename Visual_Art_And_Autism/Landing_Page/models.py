from django.db import models

# Create your models here.

class FirstPage(models.Model):
    #inheritance = can be reused. 
    heading = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    #picture1 = 