from django.db import models

class Deepthought(models.Model):
    title = models.CharField(max_length=100)
    thought = models.CharField(max_length=500)

# Create your models here.
