from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class Teacher(AbstractUser):
    phone_number = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='teachers')
    user_permissions = models.ManyToManyField(Permission, related_name='teachers')


class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name='class_teacher',
    )
    students = models.ManyToManyField('Student')


class Student(models.Model):
    GENDER_CHOICES = [
        (1, 'Мальчик'),
        (2, 'Девочка'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(auto_now_add=False)
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.SET_NULL,
        null=True,
        related_name='student'
    )
    address = models.CharField(max_length=100)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=1)
    pictures = models.ImageField(upload_to='photos', blank=True, null=True)


class School(models.Model):
    name = models.CharField(max_length=100)
    classes = models.ManyToManyField(SchoolClass)
