from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.


# class Teacher(AbstractUser):
#     # Additional fields can be added if needed
#     pass


class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()