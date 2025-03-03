from django.db import models
from django.utils import timezone


# Create your models here.

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='')
    date_time = models.DateTimeField( default=timezone.now)
    salary = models.IntegerField(default=0)


    def __str__(self):
        return self.title

