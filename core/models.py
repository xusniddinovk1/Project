from django.contrib.auth.models import User
from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_lenght=100)
    description = models.TextField()
    image = models.ImageField(upload_to='aboutUs/')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course')
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='lessons/')
    description1 = models.TextField()
    image1 = models.ImageField(upload_to='lessons/')
    description2 = models.TextField()
    image2 = models.ImageField(upload_to='lessons/')

    def __str__(self):
        return self.title