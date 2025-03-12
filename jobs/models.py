from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=200)

class Authors(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)


class Location(models.Model):
    street = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)
    state = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    postal_code = models.CharField(max_length=200, blank=False)

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='')
    date_time = models.DateTimeField( default=timezone.now)
    expiry = models.DateTimeField( null=True)
    salary = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=True, max_length=40, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skills)

    def save(self, *args, **kwargs):
        if not self.id:
            print(f"Saving slug: {slugify(str(self.title))}")
            self.slug = slugify(str(self.title))
        return super(JobPost, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} with salary {self.salary}"
